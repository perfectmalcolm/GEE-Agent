# ==============================================================================
# RAG STORE — Retrieval Augmented Generation for Kenya Flood Intelligence
# ==============================================================================
#
# This module stores curated Kenya-specific flood knowledge as an in-memory
# retrieval store. It is intentionally lightweight so the project can run without
# an external vector database.
#
# Used by:
# - gee_agent.tools.query_flood_knowledge_base()
# - gee_agent.tools.get_region_flood_profile()
# - gee_agent.tools.get_flood_dataset_details()
#
# Scope:
# - Kenya only
# - Flood monitoring
# - Google Earth Engine datasets
# - Early warning and community response
# ==============================================================================

from gee_agent.flood_config import (
    FLOOD_DATASETS,
    KENYA_REGIONS,
    FLOOD_THRESHOLDS,
    ALERT_TEMPLATES,
    KENYA_RESPONSE_CONTACTS,
    KENYA_MONITORING_PRIORITIES,
)


# ==============================================================================
# Kenya Flood Knowledge Base
# ------------------------------------------------------------------------------
# Add more documents here as the project grows. Each document should remain
# Kenya-specific and should help the agent answer practical flood-monitoring,
# risk-assessment, or early-warning questions.
# ==============================================================================

FLOOD_KNOWLEDGE_BASE = [
    {
        "id": "ken_001",
        "title": "Tana River Basin Flood Patterns",
        "region": "Kenya",
        "locations": ["Tana River Basin", "Garissa", "Hola", "Garsen", "Bura", "Upper Tana"],
        "content": """
            The Tana River Basin is Kenya's largest river system and one of the
            country's most important flood monitoring regions. Flooding is commonly
            associated with intense rainfall in the upper catchments around Mount Kenya,
            the Aberdare ranges, and central Kenya highlands. Runoff from the upper
            catchment can move downstream and affect Garissa, Tana River County, and
            low-lying settlements along the river.

            The main flood seasons are the long rains from March to May and the short
            rains from October to December. Flood risk increases when heavy rainfall
            persists for several days, when soils are already saturated, or when river
            levels are above normal.

            Useful datasets for this basin include GPM IMERG for rainfall monitoring,
            SMAP for soil moisture, Sentinel-1 SAR for flood extent detection, MERIT DEM
            for terrain context, JRC Global Surface Water for permanent water masking,
            WorldPop for exposed population, and the Global Flood Database for historical
            flood footprints.
        """,
        "tags": [
            "kenya",
            "tana",
            "tana river",
            "garissa",
            "gpm",
            "smap",
            "sentinel-1",
            "riverine flooding",
        ],
    },
    {
        "id": "ken_002",
        "title": "Lake Victoria Basin and Western Kenya Flood Risk",
        "region": "Kenya",
        "locations": ["Kisumu", "Siaya", "Busia", "Homa Bay", "Migori", "Nyando", "Nzoia", "Yala"],
        "content": """
            The Kenya side of the Lake Victoria Basin is exposed to riverine flooding,
            lowland inundation, and lakeshore flooding. Important flood-prone river
            systems include the Nzoia, Yala, Nyando, Sondu-Miriu, and Kuja rivers.
            Low-lying settlements near Budalangi, Ahero, lower Nyando, lower Nzoia,
            and lakeshore areas require close monitoring during the rainy seasons.

            Flood impacts are often worsened by saturated soils, high river inflows,
            backwater effects from Lake Victoria, and settlement or agricultural activity
            in floodplains. Monitoring should combine rainfall accumulation, soil moisture,
            detected flood extent, permanent water baseline, and population exposure.

            Sentinel-1 SAR is especially useful for mapping flood extent in western Kenya
            because it can observe the surface through cloud cover during rainy periods.
        """,
        "tags": [
            "kenya",
            "lake victoria",
            "kisumu",
            "budalangi",
            "nyando",
            "nzoia",
            "yala",
            "floodplain",
            "sar",
        ],
    },
    {
        "id": "ken_003",
        "title": "Nairobi Urban Flash Flooding",
        "region": "Kenya",
        "locations": ["Nairobi", "Mathare", "Kibera", "Mukuru", "Ngong River", "Nairobi River"],
        "content": """
            Nairobi is exposed to rapid urban flooding caused by intense rainfall,
            high impervious surface cover, drainage limitations, blocked channels, and
            settlement in low-lying or riparian areas. Key river corridors include the
            Nairobi River, Ngong River, Mathare River, and Mbagathi River.

            Urban flash floods can develop quickly after intense rainfall. Monitoring
            should prioritise short-duration rainfall intensity, drainage hotspots,
            exposed settlements, road underpasses, and river-adjacent communities.

            For Nairobi, satellite rainfall data should be complemented with ground
            observations, local drainage information, county reports, and community
            feedback because street-level flooding can occur at a finer scale than many
            satellite products can detect.
        """,
        "tags": [
            "kenya",
            "nairobi",
            "urban flooding",
            "flash flood",
            "mathare",
            "kibera",
            "mukuru",
            "drainage",
        ],
    },
    {
        "id": "ken_004",
        "title": "Athi-Galana-Sabaki River System Flood Monitoring",
        "region": "Kenya",
        "locations": ["Athi River", "Nairobi", "Machakos", "Makueni", "Kilifi", "Malindi", "Sabaki"],
        "content": """
            The Athi-Galana-Sabaki river system links upstream urban and semi-urban
            runoff with downstream flood risk toward the coast. Heavy rainfall around
            Nairobi, Kiambu, Machakos, and Kajiado can contribute to elevated downstream
            river flows. In the lower basin, flood risk may affect communities near the
            Galana and Sabaki rivers.

            Monitoring should combine GPM IMERG rainfall totals, Sentinel-1 SAR flood
            mapping, permanent water baseline, terrain information, and exposed population
            estimates. Urban runoff from Nairobi and surrounding areas can produce rapid
            flood response, while downstream river flooding may develop over a longer period.
        """,
        "tags": [
            "kenya",
            "athi",
            "galana",
            "sabaki",
            "machakos",
            "kilifi",
            "nairobi",
            "riverine flooding",
        ],
    },
    {
        "id": "ken_005",
        "title": "Ewaso Ng'iro North Basin Flash Flood Risk",
        "region": "Kenya",
        "locations": ["Laikipia", "Isiolo", "Samburu", "Marsabit", "Wajir", "Ewaso Ng'iro"],
        "content": """
            The Ewaso Ng'iro North Basin includes semi-arid and arid landscapes where
            intense rainfall can produce fast runoff, seasonal river flooding, and
            dangerous flash floods. Communities, roads, livestock routes, and settlements
            near seasonal channels can be highly exposed even when rainfall events are
            short-lived.

            Flood intelligence in this basin should focus on rainfall intensity,
            soil moisture where available, dry river channels, road crossings, and
            local observations. Because the landscape can shift from dry conditions to
            dangerous flows quickly, warnings should be clear and action-oriented.
        """,
        "tags": [
            "kenya",
            "ewaso ngiro",
            "isiolo",
            "samburu",
            "laikipia",
            "marsabit",
            "wajir",
            "flash flood",
            "dryland flooding",
        ],
    },
    {
        "id": "ken_006",
        "title": "Coastal Kenya Flood Risk",
        "region": "Kenya",
        "locations": ["Mombasa", "Kilifi", "Kwale", "Lamu", "Tana River", "Taita-Taveta"],
        "content": """
            Coastal Kenya is exposed to flooding from heavy rainfall, river discharge,
            low-lying settlements, poor drainage in urban areas, and floodplain inundation.
            Important monitoring zones include Mombasa, Kilifi, Kwale, Lamu, lower Tana,
            and the lower Galana-Sabaki system.

            Coastal flood monitoring should combine rainfall estimates, SAR-based flood
            extent detection, elevation data, permanent water masks, and population
            exposure. Urban drainage information and county-level response reports are
            also important for interpreting flood impacts.
        """,
        "tags": [
            "kenya",
            "coastal kenya",
            "mombasa",
            "kilifi",
            "kwale",
            "lamu",
            "tana river",
            "galana",
            "sabaki",
        ],
    },
    {
        "id": "ken_007",
        "title": "Kenya Flood Seasons and Monitoring Calendar",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            Kenya's flood risk is commonly elevated during the long rains from March
            to May and the short rains from October to December. Flood risk can also
            increase during unusually strong seasonal rainfall, tropical moisture surges,
            or climate anomalies that enhance rainfall over East Africa.

            For operational monitoring, the agent should track rainfall accumulation,
            rainfall intensity, soil saturation, river anomalies, flood extent, and
            population exposure. The highest-risk outputs are practical warnings that
            identify the affected county or basin, explain the likely flood type, and
            recommend immediate protective actions.
        """,
        "tags": [
            "kenya",
            "rainy season",
            "long rains",
            "short rains",
            "monitoring calendar",
            "seasonal flooding",
        ],
    },
    {
        "id": "gee_001",
        "title": "GPM IMERG for Kenya Rainfall Monitoring",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            GPM IMERG is useful for near-real-time rainfall monitoring in Kenya. In
            Google Earth Engine, the dataset key used in this project is
            rainfall_realtime, with the Earth Engine ID NASA/GPM_L3/IMERG_V06.

            For flood early warning, rainfall should be aggregated to daily totals and
            also monitored over shorter windows where possible. Heavy daily rainfall,
            repeated rainfall over several days, or intense rainfall over urban areas
            can trigger flood risk. The data should be clipped to Kenya regions such
            as Tana River Basin, Athi River Basin, Lake Victoria Basin, Nairobi, and
            coastal Kenya.
        """,
        "tags": [
            "gee",
            "gpm",
            "imerg",
            "rainfall",
            "kenya",
            "earth engine",
            "rainfall_realtime",
        ],
    },
    {
        "id": "gee_002",
        "title": "Sentinel-1 SAR for Kenya Flood Extent Mapping",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            Sentinel-1 SAR is one of the most important datasets for flood extent
            detection because radar can observe the surface during cloudy weather and
            at night. In this project, the dataset key is flood_extent_sar, with the
            Earth Engine ID COPERNICUS/S1_GRD.

            For Kenya flood mapping, Sentinel-1 can support inundation detection along
            the Tana River, Lake Victoria floodplains, lower Nyando, lower Nzoia,
            Nairobi riparian corridors, and coastal lowlands. A typical workflow compares
            current backscatter with a pre-flood baseline, masks permanent water using
            JRC Global Surface Water, and removes obvious false detections where possible.
        """,
        "tags": [
            "gee",
            "sentinel-1",
            "sar",
            "flood extent",
            "kenya",
            "earth engine",
            "flood_extent_sar",
        ],
    },
    {
        "id": "gee_003",
        "title": "SMAP Soil Moisture for Kenya Flood Readiness",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            SMAP soil moisture data helps identify catchments that are already saturated
            before or during rainfall events. In this project, the dataset key is
            soil_moisture, with the Earth Engine ID NASA_USDA/HSL/SMAP10KM_soil_moisture.

            Soil moisture is useful because saturated ground produces more runoff when
            additional rain falls. The dataset is most suitable for basin-level screening
            rather than local street-level decisions because of its coarse spatial
            resolution. It should be combined with rainfall, terrain, river information,
            and local reports.
        """,
        "tags": [
            "gee",
            "smap",
            "soil moisture",
            "kenya",
            "earth engine",
            "soil_moisture",
            "runoff",
        ],
    },
    {
        "id": "gee_004",
        "title": "Permanent Water and Historical Flood Baselines for Kenya",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            Permanent water and historical flood datasets help separate normal water
            bodies from unusual floodwater. In this project, permanent_water refers to
            JRC/GSW1_4/GlobalSurfaceWater and historical_floods refers to
            GLOBAL_FLOOD_DB/MODIS_EVENTS/V1.

            JRC Global Surface Water is useful for masking lakes, rivers, dams, and
            wetlands that are normally water-covered. The Global Flood Database helps
            identify areas that have been flooded historically and can support baseline
            risk mapping, model training, and validation.
        """,
        "tags": [
            "gee",
            "permanent water",
            "historical floods",
            "jrc",
            "global flood database",
            "kenya",
            "baseline",
        ],
    },
    {
        "id": "gee_005",
        "title": "Population Exposure Mapping for Kenya Flood Response",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            Population exposure mapping helps estimate how many people may be affected
            by floodwater or flood-prone zones. In this project, the population dataset
            key refers to WorldPop/GP/100m/pop.

            For Kenya flood response, population exposure can support prioritisation of
            alerts and response in densely populated or highly vulnerable areas such as
            Nairobi informal settlements, Kisumu lakeshore areas, Garissa, Budalangi,
            Mombasa, and other flood-prone towns. These estimates are useful for planning
            but should not be treated as exact household counts.
        """,
        "tags": [
            "gee",
            "worldpop",
            "population",
            "exposure",
            "kenya",
            "response planning",
        ],
    },
    {
        "id": "ews_001",
        "title": "People-Centred Flood Early Warning in Kenya",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            A people-centred flood early warning system should connect risk knowledge,
            monitoring, warning communication, and response capability. For Kenya, this
            means the system should not only detect hazardous rainfall or flood extent,
            but also explain who may be exposed, what actions are recommended, and how
            communities can respond.

            Practical warning outputs should be simple, location-specific, and actionable.
            They should identify the county or basin, describe the risk level, mention
            the triggering condition where available, and recommend immediate steps such
            as avoiding flooded roads, moving away from riverbanks, preparing to evacuate,
            or following county and national emergency guidance.

            Recommended communication channels include SMS, WhatsApp, community radio,
            county disaster offices, local administration, community volunteers, and
            trusted local organisations.
        """,
        "tags": [
            "ews",
            "early warning",
            "kenya",
            "community",
            "sms",
            "radio",
            "response",
        ],
    },
    {
        "id": "ews_002",
        "title": "Kenya Flood Alert Interpretation",
        "region": "Kenya",
        "locations": ["Kenya"],
        "content": """
            This project uses four practical flood alert levels: Watch, Warning, Alert,
            and Extreme. A Watch means conditions may develop into flood risk. A Warning
            means flooding is possible or likely in vulnerable places. An Alert means
            flooding is likely or already occurring in exposed areas. Extreme means severe
            flooding is expected or ongoing and immediate protective action is required.

            Rainfall and soil moisture thresholds are screening values, not final official
            warnings. A complete decision should consider observed rainfall, forecast
            rainfall, soil saturation, river levels, terrain, drainage conditions, local
            reports, and official advisories.
        """,
        "tags": [
            "ews",
            "alert levels",
            "watch",
            "warning",
            "alert",
            "extreme",
            "kenya",
        ],
    },
]


# ==============================================================================
# Utility Functions
# ==============================================================================

def _normalise_text(value: str) -> str:
    """Converts text to a lowercase searchable string."""
    return str(value or "").lower().strip()


def _tokenise(query: str) -> set:
    """Creates simple search tokens from a query."""
    stopwords = {
        "the", "and", "for", "with", "from", "that", "this", "what", "which",
        "into", "about", "show", "give", "tell", "need", "using", "where",
        "when", "how", "does", "will", "can", "are", "is", "of", "in", "to",
        "a", "an", "on", "by", "or", "as", "at",
    }
    return {
        token.strip(".,;:!?()[]{}\"'").lower()
        for token in query.split()
        if len(token.strip(".,;:!?()[]{}\"'")) > 2
        and token.strip(".,;:!?()[]{}\"'").lower() not in stopwords
    }


def _score_document(doc: dict, query: str) -> float:
    """
    Scores a document's relevance to a query using lightweight keyword matching.

    This avoids external embedding calls and keeps the demo simple. The scoring is
    intentionally transparent and easy to adjust.
    """
    query_lower = _normalise_text(query)
    query_terms = _tokenise(query)

    title = _normalise_text(doc.get("title"))
    region = _normalise_text(doc.get("region"))
    content = _normalise_text(doc.get("content"))
    tags = [_normalise_text(tag) for tag in doc.get("tags", [])]
    locations = [_normalise_text(location) for location in doc.get("locations", [])]

    score = 0.0

    # Title matches are highly important.
    for term in query_terms:
        if term in title:
            score += 4.0

    # Tag and location matches are also strong signals.
    for tag in tags:
        if tag and tag in query_lower:
            score += 3.0

    for location in locations:
        if location and location in query_lower:
            score += 3.0

    # Content matches add context.
    for term in query_terms:
        if len(term) > 3:
            score += content.count(term) * 0.5

    # Kenya-only boost for Kenya queries.
    if "kenya" in query_lower and region == "kenya":
        score *= 1.4

    # Basin-specific boosts.
    basin_terms = ["tana", "athi", "victoria", "nyando", "nzoia", "ewaso", "nairobi", "coastal"]
    for basin in basin_terms:
        if basin in query_lower and basin in (title + " " + content):
            score += 4.0

    return score


def _format_list(items) -> str:
    """Formats a list safely for display."""
    if not items:
        return "Not specified"
    return ", ".join(str(item) for item in items)


# ==============================================================================
# RAG Retrieval Functions
# ==============================================================================

def retrieve_flood_knowledge(query: str, top_k: int = 3) -> str:
    """
    Retrieves the most relevant Kenya flood knowledge documents for a query.

    Args:
        query: User question or search query.
        top_k: Number of top documents to return.

    Returns:
        A formatted string of relevant Kenya flood knowledge passages.
    """
    if not query or not query.strip():
        return (
            "No query was provided. Ask about a Kenya flood-risk region, dataset, "
            "threshold, alert level, or early-warning method."
        )

    scored_docs = []
    for doc in FLOOD_KNOWLEDGE_BASE:
        score = _score_document(doc, query)
        if score > 0:
            scored_docs.append((score, doc))

    scored_docs.sort(key=lambda item: item[0], reverse=True)
    top_docs = scored_docs[:max(1, top_k)]

    if not top_docs:
        return (
            "No specific Kenya flood knowledge was found for this query. "
            "Try asking about Tana River Basin, Lake Victoria Basin, Nairobi urban "
            "flooding, Athi River Basin, Ewaso Ng'iro Basin, GPM IMERG, Sentinel-1, "
            "SMAP, or Kenya flood alert thresholds."
        )

    result = f"Retrieved {len(top_docs)} Kenya flood knowledge document(s):\n\n"

    for index, (score, doc) in enumerate(top_docs, start=1):
        result += f"{index}. {doc['title']}\n"
        result += f"Region: {doc.get('region', 'Kenya')}\n"
        result += f"Locations: {_format_list(doc.get('locations', []))}\n"
        result += f"Relevance Score: {score:.2f}\n"
        result += f"Knowledge:\n{doc['content'].strip()}\n"
        result += f"Tags: {_format_list(doc.get('tags', []))}\n\n"

    return result.strip()


def get_dataset_info(dataset_key: str) -> str:
    """
    Returns pre-curated information about a specific flood dataset.

    Args:
        dataset_key: Key from FLOOD_DATASETS, e.g. rainfall_realtime,
                     soil_moisture, flood_extent_sar, elevation,
                     permanent_water, population, historical_floods, landcover.

    Returns:
        Formatted dataset information string.
    """
    if not dataset_key:
        available = ", ".join(FLOOD_DATASETS.keys())
        return f"No dataset key was provided. Available dataset keys: {available}"

    dataset_key = dataset_key.strip()

    if dataset_key not in FLOOD_DATASETS:
        available = ", ".join(FLOOD_DATASETS.keys())
        return f"Dataset key '{dataset_key}' was not found. Available dataset keys: {available}"

    ds = FLOOD_DATASETS[dataset_key]

    key_bands = _format_list(ds.get("key_bands", []))

    return f"""
Dataset: {ds.get('name', 'Unnamed dataset')}
Dataset Key: {dataset_key}
GEE ID: {ds.get('gee_id', 'Not specified')}
Resolution: {ds.get('resolution', 'Not specified')}
Update Frequency: {ds.get('update_frequency', 'Not specified')}
Coverage: {ds.get('coverage', 'Not specified')}
Primary Variable: {ds.get('primary_variable', 'Not specified')}
Key Bands: {key_bands}
Use Case: {ds.get('use_case', 'Not specified')}
Kenya Application: {ds.get('kenya_application', 'Not specified')}
Limitations: {ds.get('limitations', 'Not specified')}
Catalog URL: {ds.get('catalog_url', 'Not specified')}
    """.strip()


def get_region_info(region_name: str) -> str:
    """
    Returns Kenya flood-risk information for a configured region.

    Args:
        region_name: Region key or partial name, e.g. tana_river_basin,
                     Nairobi, Lake Victoria, Nyando, Coastal Kenya.

    Returns:
        Formatted Kenya region information string.
    """
    if not region_name:
        available = ", ".join(KENYA_REGIONS.keys())
        return f"No region name was provided. Available Kenya regions: {available}"

    region_query = _normalise_text(region_name)
    matched_key = None
    matched_region = None

    # Exact key match.
    if region_query in KENYA_REGIONS:
        matched_key = region_query
        matched_region = KENYA_REGIONS[region_query]
    else:
        # Fuzzy key/name/county/river/town match.
        for key, region in KENYA_REGIONS.items():
            searchable_parts = [
                key,
                region.get("name", ""),
                " ".join(region.get("counties", [])),
                " ".join(region.get("major_rivers", [])),
                " ".join(region.get("main_towns", [])),
            ]
            searchable = _normalise_text(" ".join(searchable_parts))

            if region_query in searchable:
                matched_key = key
                matched_region = region
                break

    if matched_region is None:
        available = ", ".join(KENYA_REGIONS.keys())
        return f"Kenya region '{region_name}' was not found. Available regions: {available}"

    bbox = matched_region.get("bbox", [])
    bbox_text = (
        f"[{bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}]"
        if len(bbox) == 4
        else "Not specified"
    )

    return f"""
Region: {matched_region.get('name', matched_key)}
Region Key: {matched_key}
Risk Level: {matched_region.get('risk_level', 'Not specified')}
Monitoring Priority: {matched_region.get('monitoring_priority', 'Not specified')}
Counties: {_format_list(matched_region.get('counties', []))}
Major Rivers: {_format_list(matched_region.get('major_rivers', []))}
Main Towns: {_format_list(matched_region.get('main_towns', []))}
Flood Type: {_format_list(matched_region.get('flood_type', []))}
Peak Risk Months: {_format_list(matched_region.get('peak_risk_months', []))}
Bounding Box: {bbox_text}
Recommended Datasets: {_format_list(matched_region.get('recommended_datasets', []))}
Notes: {matched_region.get('notes', 'Not specified')}
    """.strip()


def list_kenya_knowledge_topics() -> str:
    """
    Lists available Kenya knowledge-base topics.
    """
    result = "Available Kenya flood knowledge topics:\n\n"
    for doc in FLOOD_KNOWLEDGE_BASE:
        result += f"- {doc['title']} ({doc['id']})\n"
    return result.strip()


# ==============================================================================
# Risk Evaluation Function
# ==============================================================================

def evaluate_flood_risk(rainfall_mm: float, soil_moisture: float = None) -> str:
    """
    Evaluates flood risk level based on daily rainfall and optional soil moisture.

    Args:
        rainfall_mm: Daily rainfall in millimetres.
        soil_moisture: Soil moisture fraction from 0 to 1, optional.

    Returns:
        Formatted Kenya flood risk assessment.
    """
    try:
        rainfall_mm = float(rainfall_mm)
    except (TypeError, ValueError):
        return "Rainfall value must be a valid number in mm/day."

    if soil_moisture is not None:
        try:
            soil_moisture = float(soil_moisture)
        except (TypeError, ValueError):
            return "Soil moisture value must be a valid number between 0 and 1."

    rainfall_thresholds = FLOOD_THRESHOLDS["rainfall"]

    if rainfall_mm >= rainfall_thresholds["extreme"]:
        level = "extreme"
    elif rainfall_mm >= rainfall_thresholds["alert"]:
        level = "alert"
    elif rainfall_mm >= rainfall_thresholds["warning"]:
        level = "warning"
    elif rainfall_mm >= rainfall_thresholds["watch"]:
        level = "watch"
    else:
        return f"""
NORMAL MONITORING
Rainfall: {rainfall_mm:.1f} mm/day
Status: Below flood watch threshold of {rainfall_thresholds['watch']} mm/day.
Recommended Action: Continue routine monitoring, especially if more rainfall is forecast or soils are already wet.
        """.strip()

    upgrade_note = ""

    if soil_moisture is not None:
        soil_thresholds = FLOOD_THRESHOLDS["soil_moisture"]

        if soil_moisture >= soil_thresholds["extreme"] and level in ["watch", "warning", "alert"]:
            level = "extreme"
            upgrade_note = (
                f"Soil moisture is very high ({soil_moisture:.2f}), so the risk has "
                "been upgraded because saturated soil greatly increases runoff."
            )
        elif soil_moisture >= soil_thresholds["alert"] and level in ["watch", "warning"]:
            level = "alert"
            upgrade_note = (
                f"Soil moisture is high ({soil_moisture:.2f}), so the risk has "
                "been upgraded because additional rainfall may quickly become runoff."
            )
        elif soil_moisture >= soil_thresholds["warning"] and level == "watch":
            level = "warning"
            upgrade_note = (
                f"Soil moisture is elevated ({soil_moisture:.2f}), so the risk has "
                "been upgraded from watch to warning."
            )

    template = ALERT_TEMPLATES[level]

    guidance = template.get("community_guidance", [])
    guidance_text = "\n".join(f"- {item}" for item in guidance) if guidance else "- Follow official updates."

    result = f"""
{template.get('emoji', '')} {template.get('level', level.upper())}
Severity: {template.get('severity', 'Not specified')}
Meaning: {template.get('meaning', 'Not specified')}

Observed Indicators:
- Rainfall: {rainfall_mm:.1f} mm/day
- Rainfall threshold for this level: {rainfall_thresholds[level]} mm/day
"""

    if soil_moisture is not None:
        result += f"- Soil moisture: {soil_moisture:.2f} fraction of saturation\n"

    if upgrade_note:
        result += f"\nRisk Upgrade Note: {upgrade_note}\n"

    result += f"""
Recommended Action:
{template.get('action', 'Follow official guidance and monitor conditions closely.')}

Community Guidance:
{guidance_text}

Recommended Monitoring Datasets:
- GPM IMERG for rainfall accumulation
- SMAP for soil moisture
- Sentinel-1 SAR for flood extent confirmation
- JRC Global Surface Water for baseline water masking
- WorldPop for population exposure estimates

Emergency References:
- National emergency numbers: {_format_list(KENYA_RESPONSE_CONTACTS.get('national_emergency_numbers', []))}
- Local support: {_format_list(KENYA_RESPONSE_CONTACTS.get('recommended_local_contacts', []))}
    """

    return result.strip()


# ==============================================================================
# Monitoring Priority Summary
# ==============================================================================

def get_kenya_monitoring_priorities() -> str:
    """
    Returns the project's Kenya flood monitoring priorities.
    """
    primary_indicators = "\n".join(
        f"- {item}" for item in KENYA_MONITORING_PRIORITIES.get("primary_indicators", [])
    )
    priority_outputs = "\n".join(
        f"- {item}" for item in KENYA_MONITORING_PRIORITIES.get("priority_outputs", [])
    )

    return f"""
Kenya Flood Monitoring Priorities

Primary Indicators:
{primary_indicators}

Priority Outputs:
{priority_outputs}

Decision Notes:
{KENYA_MONITORING_PRIORITIES.get('decision_notes', 'Not specified')}
    """.strip()
