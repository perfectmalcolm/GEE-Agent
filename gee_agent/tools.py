# ==============================================================================
# TOOLS — Kenya Flood Intelligence Agent
# ==============================================================================
#
# This module contains all custom tool functions used by the ADK sub-agents.
#
# Scope:
# - Kenya only
# - Google Earth Engine flood datasets
# - Kenya flood-region profiles
# - Kenya flood-risk assessment
# - Kenya alert generation
# - Webpage fetching for dataset pages and public reports
#
# Used by:
# - gee_agent.agent.gee_search_agent
# - gee_agent.agent.flood_knowledge_agent
# - gee_agent.agent.risk_assessment_agent
# - gee_agent.agent.web_fetch_agent
# ==============================================================================

from datetime import datetime, timezone
from urllib.parse import quote_plus

import requests

from gee_agent.flood_config import (
    FLOOD_DATASETS,
    KENYA_REGIONS,
    ALERT_TEMPLATES,
    KENYA_RESPONSE_CONTACTS,
)

from gee_agent.rag_store import (
    retrieve_flood_knowledge,
    get_dataset_info,
    get_region_info,
    evaluate_flood_risk,
)


# ==============================================================================
# Helper Functions
# ==============================================================================

def _format_list(items) -> str:
    """
    Safely formats a list, tuple, or single value into a readable string.
    """
    if not items:
        return "Not specified"

    if isinstance(items, (list, tuple, set)):
        return ", ".join(str(item) for item in items)

    return str(items)


def _safe_float(value, field_name: str) -> float:
    """
    Converts a value to float and raises a clear error if conversion fails.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field_name} must be a valid number.")


def _normalise_alert_level(alert_level: str) -> str:
    """
    Normalises alert level values and defaults to watch if invalid.
    """
    if not alert_level:
        return "watch"

    level = str(alert_level).strip().lower()

    valid_levels = set(ALERT_TEMPLATES.keys())
    if level not in valid_levels:
        return "watch"

    return level


def _get_region_counties(region_key_or_name: str) -> list:
    """
    Attempts to get affected counties from a configured Kenya region.
    """
    if not region_key_or_name:
        return []

    query = str(region_key_or_name).lower().strip()

    for key, region in KENYA_REGIONS.items():
        region_name = region.get("name", "").lower()
        counties = region.get("counties", [])
        towns = region.get("main_towns", [])
        rivers = region.get("major_rivers", [])

        searchable = " ".join(
            [key, region_name]
            + [str(item).lower() for item in counties]
            + [str(item).lower() for item in towns]
            + [str(item).lower() for item in rivers]
        )

        if query in searchable or searchable in query:
            return counties

    return []


# ==============================================================================
# Google Earth Engine Catalog Tools
# ==============================================================================

def search_gee_catalog(query: str) -> str:
    """
    Searches the Google Earth Engine dataset catalog for datasets matching a query.

    Args:
        query: Search terms, e.g. "rainfall Kenya flood", "Sentinel-1 flood Kenya".

    Returns:
        A short text response containing the catalog search URL and returned page text.
    """
    if not query or not str(query).strip():
        return "Please provide a search query, for example: 'rainfall flood Kenya'."

    search_query = f"{query} Kenya flood"
    search_url = (
        "https://developers.google.com/s/results/earth-engine/datasets"
        f"?q={quote_plus(search_query)}"
    )

    try:
        headers = {"User-Agent": "Mozilla/5.0 (KenyaFloodIntelligenceAgent/1.0)"}
        response = requests.get(search_url, timeout=10, headers=headers)
        response.raise_for_status()

        page_text = response.text[:5000]

        return f"""
Google Earth Engine catalog search completed.

Search Query: {search_query}
Search URL: {search_url}

Returned Page Text Preview:
{page_text}
        """.strip()

    except requests.exceptions.Timeout:
        return (
            "GEE catalog search timed out. Try a more specific query such as "
            "'GPM IMERG rainfall Kenya' or 'Sentinel-1 flood extent Kenya'."
        )

    except requests.exceptions.RequestException as exc:
        return f"GEE catalog search failed: {exc}"


def search_flood_datasets(region: str = "Kenya") -> str:
    """
    Returns pre-curated flood-relevant Google Earth Engine datasets for Kenya.

    Args:
        region: Optional Kenya region, basin, county, or general text.
                This project is Kenya-only, so the region is interpreted within Kenya.

    Returns:
        Formatted list of flood-relevant datasets with GEE IDs and use cases.
    """
    region_text = region or "Kenya"

    result = f"Pre-curated Google Earth Engine flood datasets for {region_text}:\n\n"

    for index, (key, ds) in enumerate(FLOOD_DATASETS.items(), start=1):
        result += f"{index}. {ds.get('name', 'Unnamed dataset')}\n"
        result += f"   Dataset Key: {key}\n"
        result += f"   GEE ID: {ds.get('gee_id', 'Not specified')}\n"
        result += f"   Resolution: {ds.get('resolution', 'Not specified')}\n"
        result += f"   Update Frequency: {ds.get('update_frequency', 'Not specified')}\n"
        result += f"   Coverage: {ds.get('coverage', 'Not specified')}\n"
        result += f"   Key Bands: {_format_list(ds.get('key_bands', []))}\n"
        result += f"   Use Case: {ds.get('use_case', 'Not specified')}\n"

        kenya_application = ds.get("kenya_application")
        if kenya_application:
            result += f"   Kenya Application: {kenya_application}\n"

        limitations = ds.get("limitations")
        if limitations:
            result += f"   Limitations: {limitations}\n"

        result += f"   Catalog URL: {ds.get('catalog_url', 'Not specified')}\n\n"

    return result.strip()


def fetch_webpage_text(url: str) -> str:
    """
    Fetches readable text from a webpage URL.

    Args:
        url: URL of a dataset page, report, weather advisory, or public reference.

    Returns:
        Page text preview or a clear error message.
    """
    if not url or not str(url).strip():
        return "Please provide a valid URL to fetch."

    url = str(url).strip()

    if not url.startswith(("http://", "https://")):
        return "Invalid URL. The URL must start with http:// or https://."

    try:
        headers = {"User-Agent": "Mozilla/5.0 (KenyaFloodIntelligenceAgent/1.0)"}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "unknown")
        page_text = response.text[:7000]

        return f"""
Fetched webpage successfully.

URL: {url}
Content Type: {content_type}

Page Text Preview:
{page_text}
        """.strip()

    except requests.exceptions.Timeout:
        return f"Request timed out for URL: {url}"

    except requests.exceptions.RequestException as exc:
        return f"Failed to fetch URL {url}: {exc}"


# ==============================================================================
# RAG-Powered Knowledge Tools
# ==============================================================================

def query_flood_knowledge_base(query: str) -> str:
    """
    Queries the internal Kenya flood knowledge base.

    Args:
        query: Natural language question about Kenya floods, datasets, regions,
               alert levels, or early-warning methods.

    Returns:
        Retrieved Kenya flood knowledge passages ranked by relevance.
    """
    if not query or not str(query).strip():
        return (
            "Please provide a Kenya flood-related query, for example: "
            "'Tana River Basin flood patterns' or 'Sentinel-1 flood mapping Kenya'."
        )

    return retrieve_flood_knowledge(query, top_k=3)


def get_flood_dataset_details(dataset_key: str) -> str:
    """
    Returns detailed information about a specific pre-curated flood dataset.

    Args:
        dataset_key: One of the keys in FLOOD_DATASETS, for example:
                     rainfall_realtime, soil_moisture, flood_extent_sar,
                     elevation, permanent_water, population, historical_floods,
                     or landcover.

    Returns:
        Full dataset metadata including GEE ID, resolution, bands, Kenya use case,
        limitations, and catalog URL.
    """
    return get_dataset_info(dataset_key)


def get_region_flood_profile(region_name: str) -> str:
    """
    Returns the flood-risk profile for a configured Kenya region.

    Args:
        region_name: Region key, basin, county, river, or town name.
                     Examples: tana_river_basin, Tana River, Nairobi,
                     Lake Victoria, Nyando, Nzoia, Ewaso Ng'iro, Coastal Kenya.

    Returns:
        Kenya region flood-risk profile with counties, rivers, flood type,
        bounding box, notes, and recommended datasets.
    """
    return get_region_info(region_name)


def list_available_regions() -> str:
    """
    Lists all configured Kenya flood monitoring regions.

    Returns:
        Formatted list of Kenya monitoring regions with risk level, counties,
        flood type, and region keys.
    """
    result = "Configured Kenya flood monitoring regions:\n\n"

    for index, (key, region) in enumerate(KENYA_REGIONS.items(), start=1):
        result += f"{index}. {region.get('name', key)}\n"
        result += f"   Region Key: {key}\n"
        result += f"   Risk Level: {region.get('risk_level', 'Not specified')}\n"
        result += f"   Monitoring Priority: {region.get('monitoring_priority', 'Not specified')}\n"
        result += f"   Counties: {_format_list(region.get('counties', []))}\n"
        result += f"   Major Rivers: {_format_list(region.get('major_rivers', []))}\n"
        result += f"   Flood Type: {_format_list(region.get('flood_type', []))}\n"
        result += f"   Peak Risk Months: {_format_list(region.get('peak_risk_months', []))}\n"
        result += f"   Recommended Datasets: {_format_list(region.get('recommended_datasets', []))}\n"
        result += f"   Notes: {region.get('notes', 'Not specified')}\n\n"

    return result.strip()


# ==============================================================================
# Flood Risk Assessment Tools
# ==============================================================================

def assess_flood_risk(rainfall_mm: float, soil_moisture_fraction: float = None) -> str:
    """
    Evaluates Kenya flood risk based on rainfall and optional soil moisture.

    Args:
        rainfall_mm: Observed or forecast daily rainfall in millimetres.
        soil_moisture_fraction: Optional soil moisture fraction from 0.0 to 1.0.

    Returns:
        Risk assessment with alert level, thresholds, recommended actions,
        monitoring datasets, and emergency references.
    """
    try:
        rainfall_value = _safe_float(rainfall_mm, "rainfall_mm")
    except ValueError as exc:
        return str(exc)

    soil_value = None
    if soil_moisture_fraction is not None:
        try:
            soil_value = _safe_float(soil_moisture_fraction, "soil_moisture_fraction")
        except ValueError as exc:
            return str(exc)

        if soil_value < 0 or soil_value > 1:
            return "soil_moisture_fraction must be between 0.0 and 1.0."

    return evaluate_flood_risk(rainfall_value, soil_value)


def generate_flood_alert(
    region: str,
    rainfall_mm: float,
    alert_level: str,
    affected_counties: list = None,
) -> str:
    """
    Generates a professional Kenya flood alert message.

    Args:
        region: Affected Kenya region, basin, county, or location.
        rainfall_mm: Observed or forecast rainfall in mm/day.
        alert_level: One of: watch, warning, alert, extreme.
        affected_counties: Optional list of affected Kenyan counties.

    Returns:
        Formatted alert card with SMS-style message, radio-style message,
        recommended actions, data sources, and emergency references.
    """
    if not region or not str(region).strip():
        region = "Kenya flood-risk area"

    try:
        rainfall_value = _safe_float(rainfall_mm, "rainfall_mm")
    except ValueError as exc:
        return str(exc)

    level = _normalise_alert_level(alert_level)
    template = ALERT_TEMPLATES[level]

    if affected_counties is None:
        affected_counties = _get_region_counties(region)

    counties_text = _format_list(affected_counties) if affected_counties else "To be confirmed from local reports"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    community_guidance = template.get("community_guidance", [])
    guidance_text = "\n".join(f"- {item}" for item in community_guidance) if community_guidance else "- Follow official updates."

    emergency_numbers = _format_list(KENYA_RESPONSE_CONTACTS.get("national_emergency_numbers", []))
    local_contacts = _format_list(KENYA_RESPONSE_CONTACTS.get("recommended_local_contacts", []))

    sms_message = (
        f"{template.get('level', level.upper())}: Flood risk in {region}. "
        f"Rainfall: {rainfall_value:.0f} mm/day. "
        f"{template.get('action', 'Follow official guidance.')} "
        f"Emergency: {emergency_numbers}."
    )

    radio_message = (
        f"Tahadhari ya mafuriko imetolewa kwa eneo la {region}. "
        f"Mvua ya takribani milimita {rainfall_value:.0f} kwa siku imeripotiwa au kutabiriwa. "
        f"Tafadhali epuka kuvuka barabara au mito iliyojaa maji, songa maeneo ya juu ikiwa uko "
        f"eneo hatarishi, na fuata maelekezo ya mamlaka za eneo lako."
    )

    alert_card = f"""
{template.get('emoji', '')} {template.get('level', level.upper())}
Issued: {timestamp}
Region: {region}
Affected Counties: {counties_text}
Rainfall: {rainfall_value:.1f} mm/day
Severity: {template.get('severity', 'Not specified')}

Meaning:
{template.get('meaning', 'Not specified')}

Recommended Action:
{template.get('action', 'Follow official guidance and monitor conditions closely.')}

Community Guidance:
{guidance_text}

SMS-Style Alert:
"{sms_message}"

Radio-Style Message in Swahili:
"{radio_message}"

Recommended Data Sources for Confirmation:
- GPM IMERG rainfall estimates through Google Earth Engine
- SMAP soil moisture where available
- Sentinel-1 SAR flood extent mapping
- JRC Global Surface Water baseline
- WorldPop population exposure estimates
- County and national official advisories

Emergency References:
- National emergency numbers: {emergency_numbers}
- Local support contacts: {local_contacts}

Note:
This alert is decision-support information for Kenya flood monitoring. It should be
verified with official forecasts, local observations, river gauges, and county-level
emergency information where available.
    """.strip()

    return alert_card
