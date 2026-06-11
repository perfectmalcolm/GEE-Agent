# ==============================================================================
# KENYA FLOOD INTELLIGENCE AGENT - Geographic, Dataset & Threshold Configuration
# ==============================================================================
#
# This configuration file is Kenya-only.
# It supports:
# - Kenya flood-risk region lookup
# - Flood threshold assessment
# - Google Earth Engine dataset discovery
# - Community alert generation
#
# Used by:
# - gee_agent.agent
# - gee_agent.tools
# - gee_agent.rag_store
# ==============================================================================


# ==============================================================================
# Kenya Flood Monitoring Regions
# ------------------------------------------------------------------------------
# bbox format: [min_lon, min_lat, max_lon, max_lat]
# Coordinates are approximate monitoring extents for screening and early warning.
# ==============================================================================

KENYA_REGIONS = {
    "tana_river_basin": {
        "name": "Tana River Basin",
        "counties": [
            "Nyeri",
            "Kirinyaga",
            "Murang'a",
            "Tharaka-Nithi",
            "Embu",
            "Kitui",
            "Meru",
            "Tana River",
            "Garissa",
        ],
        "major_rivers": ["Tana River", "Thiba River", "Mathioya River", "Sagana River"],
        "main_towns": ["Garissa", "Hola", "Garsen", "Bura", "Embu"],
        "bbox": [36.5, -3.2, 41.2, 1.2],
        "risk_level": "HIGH",
        "flood_type": ["Riverine flooding", "Flash flooding", "Lowland inundation"],
        "peak_risk_months": ["March", "April", "May", "October", "November", "December"],
        "monitoring_priority": "Very high",
        "notes": (
            "Kenya's largest river basin and one of the most important flood-risk "
            "zones. Downstream areas in Garissa and Tana River counties are highly "
            "exposed during heavy rainfall and upstream runoff events."
        ),
        "recommended_datasets": [
            "rainfall_realtime",
            "soil_moisture",
            "flood_extent_sar",
            "elevation",
            "permanent_water",
            "population",
            "historical_floods",
        ],
    },

    "athi_river_basin": {
        "name": "Athi River Basin",
        "counties": [
            "Nairobi",
            "Kiambu",
            "Machakos",
            "Kajiado",
            "Makueni",
            "Taita-Taveta",
            "Kilifi",
            "Kwale",
        ],
        "major_rivers": ["Athi River", "Nairobi River", "Ngong River", "Mbagathi River", "Galana River"],
        "main_towns": ["Nairobi", "Athi River", "Machakos", "Malindi", "Kilifi"],
        "bbox": [36.3, -4.7, 40.4, -0.8],
        "risk_level": "HIGH",
        "flood_type": ["Urban flooding", "Flash flooding", "Riverine flooding"],
        "peak_risk_months": ["March", "April", "May", "October", "November", "December"],
        "monitoring_priority": "Very high",
        "notes": (
            "Important for Nairobi urban flood monitoring and downstream flood-risk "
            "tracking along the Athi-Galana-Sabaki system. Rapid runoff from built-up "
            "areas can produce dangerous flash-flood conditions."
        ),
        "recommended_datasets": [
            "rainfall_realtime",
            "flood_extent_sar",
            "elevation",
            "permanent_water",
            "population",
        ],
    },

    "lake_victoria_basin": {
        "name": "Lake Victoria Basin",
        "counties": [
            "Kisumu",
            "Siaya",
            "Homa Bay",
            "Migori",
            "Busia",
            "Kakamega",
            "Vihiga",
            "Bungoma",
            "Kericho",
            "Nandi",
            "Bomet",
            "Nyamira",
            "Kisii",
        ],
        "major_rivers": ["Nzoia River", "Yala River", "Nyando River", "Sondu-Miriu River", "Kuja River"],
        "main_towns": ["Kisumu", "Busia", "Siaya", "Homa Bay", "Migori"],
        "bbox": [33.8, -1.6, 35.8, 1.3],
        "risk_level": "HIGH",
        "flood_type": ["Lake backwater flooding", "Riverine flooding", "Lowland inundation"],
        "peak_risk_months": ["March", "April", "May", "October", "November", "December"],
        "monitoring_priority": "Very high",
        "notes": (
            "Flood risk is associated with river inflows, low-lying lakeshore "
            "settlements, saturated soils, and lake-level rise. The Nyando, Nzoia, "
            "Yala, and Sondu-Miriu sub-basins are important monitoring targets."
        ),
        "recommended_datasets": [
            "rainfall_realtime",
            "soil_moisture",
            "flood_extent_sar",
            "permanent_water",
            "population",
            "historical_floods",
        ],
    },

    "ewaso_ngiro_basin": {
        "name": "Ewaso Ng'iro North Basin",
        "counties": [
            "Laikipia",
            "Samburu",
            "Isiolo",
            "Marsabit",
            "Meru",
            "Nyeri",
            "Wajir",
            "Garissa",
        ],
        "major_rivers": ["Ewaso Ng'iro River", "Isiolo River", "Nanyuki River"],
        "main_towns": ["Isiolo", "Nanyuki", "Archer's Post", "Wajir"],
        "bbox": [36.4, 0.0, 40.8, 3.8],
        "risk_level": "MEDIUM",
        "flood_type": ["Flash flooding", "Seasonal river flooding", "Dryland channel flooding"],
        "peak_risk_months": ["March", "April", "May", "October", "November", "December"],
        "monitoring_priority": "High",
        "notes": (
            "Semi-arid and arid catchments can experience fast runoff response after "
            "intense rainfall. Flood impacts can be severe where communities, roads, "
            "livestock routes, and seasonal river channels intersect."
        ),
        "recommended_datasets": [
            "rainfall_realtime",
            "soil_moisture",
            "flood_extent_sar",
            "elevation",
            "population",
        ],
    },

    "nairobi_urban_flood_zone": {
        "name": "Nairobi Urban Flood Zone",
        "counties": ["Nairobi", "Kiambu", "Machakos", "Kajiado"],
        "major_rivers": ["Nairobi River", "Ngong River", "Mathare River", "Mbagathi River"],
        "main_towns": ["Nairobi", "Ruiru", "Athi River", "Kitengela", "Ngong"],
        "bbox": [36.55, -1.55, 37.15, -1.05],
        "risk_level": "HIGH",
        "flood_type": ["Urban flooding", "Drainage overflow", "Flash flooding"],
        "peak_risk_months": ["March", "April", "May", "October", "November", "December"],
        "monitoring_priority": "Very high",
        "notes": (
            "High exposure because of dense settlement, impervious surfaces, drainage "
            "constraints, informal settlements near riparian zones, and rapid runoff "
            "during intense storms."
        ),
        "recommended_datasets": [
            "rainfall_realtime",
            "flood_extent_sar",
            "elevation",
            "population",
            "permanent_water",
        ],
    },

    "coastal_kenya_flood_zone": {
        "name": "Coastal Kenya Flood Zone",
        "counties": ["Mombasa", "Kilifi", "Kwale", "Tana River", "Lamu", "Taita-Taveta"],
        "major_rivers": ["Tana River", "Galana River", "Sabaki River", "Umba River"],
        "main_towns": ["Mombasa", "Malindi", "Kilifi", "Lamu", "Voi", "Garsen"],
        "bbox": [38.2, -4.8, 41.7, -1.5],
        "risk_level": "HIGH",
        "flood_type": ["Coastal flooding", "Riverine flooding", "Urban flooding", "Lowland inundation"],
        "peak_risk_months": ["March", "April", "May", "October", "November", "December"],
        "monitoring_priority": "High",
        "notes": (
            "Flood risk is linked to heavy rainfall, low-lying coastal settlements, "
            "river discharge, drainage limitations, and exposed transport corridors."
        ),
        "recommended_datasets": [
            "rainfall_realtime",
            "flood_extent_sar",
            "elevation",
            "permanent_water",
            "population",
        ],
    },

    "nzoia_yala_nyando_basin": {
        "name": "Nzoia-Yala-Nyando Floodplain",
        "counties": ["Busia", "Siaya", "Kisumu", "Kakamega", "Vihiga", "Bungoma", "Nandi", "Kericho"],
        "major_rivers": ["Nzoia River", "Yala River", "Nyando River"],
        "main_towns": ["Budalangi", "Siaya", "Kisumu", "Ahero", "Muhoroni"],
        "bbox": [34.0, -0.6, 35.6, 1.2],
        "risk_level": "HIGH",
        "flood_type": ["Riverine flooding", "Floodplain inundation", "Lake backwater flooding"],
        "peak_risk_months": ["March", "April", "May", "October", "November", "December"],
        "monitoring_priority": "Very high",
        "notes": (
            "One of the most important floodplain monitoring zones in western Kenya. "
            "Budalangi, lower Nzoia, lower Nyando, and low-lying lakeshore areas "
            "require close monitoring during heavy rainfall seasons."
        ),
        "recommended_datasets": [
            "rainfall_realtime",
            "soil_moisture",
            "flood_extent_sar",
            "permanent_water",
            "population",
            "historical_floods",
        ],
    },
}


# ==============================================================================
# Kenya Flood Threshold Configuration
# ------------------------------------------------------------------------------
# Thresholds are practical early-warning screening values.
# They should be calibrated later using observed Kenya rainfall, river gauge,
# soil moisture, flood extent, and verified impact records.
# ==============================================================================

FLOOD_THRESHOLDS = {
    "rainfall": {
        "unit": "mm/day",
        "description": "Daily rainfall accumulation used for initial flood-risk screening.",
        "watch": 25,
        "warning": 50,
        "alert": 75,
        "extreme": 100,
    },

    "soil_moisture": {
        "unit": "fraction_of_saturation",
        "description": "Surface or root-zone soil saturation indicator.",
        "watch": 0.75,
        "warning": 0.85,
        "alert": 0.92,
        "extreme": 0.97,
    },

    "river_anomaly": {
        "unit": "z_score",
        "description": "River level or river discharge anomaly above historical mean.",
        "watch": 1.5,
        "warning": 2.0,
        "alert": 2.5,
        "extreme": 3.0,
    },

    "flood_extent_change": {
        "unit": "percent_change_from_baseline",
        "description": "Increase in detected open-water or flood-like pixels against baseline.",
        "watch": 10,
        "warning": 25,
        "alert": 40,
        "extreme": 60,
    },
}


# ==============================================================================
# Google Earth Engine Flood-Relevant Dataset Registry
# ------------------------------------------------------------------------------
# These datasets have broad spatial coverage but should be clipped, filtered,
# and interpreted for Kenya regions only in this project.
# ==============================================================================

FLOOD_DATASETS = {
    "rainfall_realtime": {
        "gee_id": "NASA/GPM_L3/IMERG_V06",
        "name": "GPM IMERG — Global Precipitation Measurement",
        "resolution": "Approximately 10 km",
        "update_frequency": "30 minutes",
        "coverage": "Broad coverage; filter to Kenya monitoring regions",
        "key_bands": ["precipitationCal", "precipitationUncal"],
        "primary_variable": "Rainfall intensity and accumulation",
        "use_case": (
            "Primary rainfall monitoring dataset for detecting heavy rainfall "
            "that may trigger flash floods, riverine floods, and urban floods in Kenya."
        ),
        "kenya_application": (
            "Useful for rainfall accumulation over Tana River Basin, Athi River Basin, "
            "Lake Victoria Basin, Nairobi, and other configured Kenya regions."
        ),
        "limitations": (
            "Satellite rainfall estimates may require validation with Kenya ground "
            "station data where available."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/NASA_GPM_L3_IMERG_V06",
    },

    "soil_moisture": {
        "gee_id": "NASA_USDA/HSL/SMAP10KM_soil_moisture",
        "name": "SMAP — Soil Moisture Active Passive",
        "resolution": "Approximately 10 km",
        "update_frequency": "Daily",
        "coverage": "Broad coverage; filter to Kenya monitoring regions",
        "key_bands": ["ssm", "susm", "smp"],
        "primary_variable": "Surface and subsurface soil moisture",
        "use_case": (
            "Soil saturation monitoring for identifying catchments where additional "
            "rainfall may quickly turn into runoff and flooding."
        ),
        "kenya_application": (
            "Useful before and during rainy seasons to assess flood readiness in "
            "western Kenya, Tana River Basin, Ewaso Ng'iro Basin, and other areas."
        ),
        "limitations": (
            "Coarse resolution means it is better for basin-level screening than "
            "street-level flood detection."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/NASA_USDA_HSL_SMAP10KM_soil_moisture",
    },

    "flood_extent_sar": {
        "gee_id": "COPERNICUS/S1_GRD",
        "name": "Sentinel-1 SAR GRD — Flood Extent Mapping",
        "resolution": "10 m",
        "update_frequency": "Typically 6-12 days depending on orbit and location",
        "coverage": "Broad coverage; filter to Kenya monitoring regions",
        "key_bands": ["VV", "VH", "angle"],
        "primary_variable": "Radar backscatter for flood-water detection",
        "use_case": (
            "Cloud-penetrating flood extent mapping during storm periods when optical "
            "satellite imagery may be blocked by clouds."
        ),
        "kenya_application": (
            "Useful for mapping inundation along Tana River, Budalangi, Nyando, "
            "Nairobi riparian corridors, and coastal lowlands."
        ),
        "limitations": (
            "Requires careful preprocessing, terrain correction, speckle handling, "
            "and comparison with pre-flood baseline imagery."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD",
    },

    "elevation": {
        "gee_id": "MERIT/DEM/v1_0_3",
        "name": "MERIT DEM — Multi-Error-Removed Improved Terrain",
        "resolution": "Approximately 90 m",
        "update_frequency": "Static",
        "coverage": "Broad coverage; filter to Kenya monitoring regions",
        "key_bands": ["dem"],
        "primary_variable": "Terrain elevation",
        "use_case": (
            "Supports flow direction analysis, low-lying area identification, "
            "floodplain screening, and downstream inundation interpretation."
        ),
        "kenya_application": (
            "Useful for identifying low-lying areas in Tana River, Lake Victoria "
            "floodplains, coastal Kenya, and urban drainage zones."
        ),
        "limitations": (
            "Not detailed enough for engineering-grade drainage design or local "
            "street-level flood modelling."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/MERIT_DEM_v1_0_3",
    },

    "permanent_water": {
        "gee_id": "JRC/GSW1_4/GlobalSurfaceWater",
        "name": "JRC Global Surface Water",
        "resolution": "30 m",
        "update_frequency": "Annual",
        "coverage": "Broad coverage; filter to Kenya monitoring regions",
        "key_bands": ["occurrence", "change_abs", "seasonality", "max_extent"],
        "primary_variable": "Permanent and seasonal surface water occurrence",
        "use_case": (
            "Provides a baseline water mask for separating normal water bodies from "
            "new floodwater."
        ),
        "kenya_application": (
            "Useful near Lake Victoria, Tana River, Athi-Galana-Sabaki system, "
            "wetlands, dams, and seasonal water bodies."
        ),
        "limitations": (
            "Annual updates mean it should be combined with Sentinel-1 for active "
            "flood event mapping."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater",
    },

    "population": {
        "gee_id": "WorldPop/GP/100m/pop",
        "name": "WorldPop — Population Density",
        "resolution": "100 m",
        "update_frequency": "Annual",
        "coverage": "Broad coverage; filter to Kenya monitoring regions",
        "key_bands": ["population"],
        "primary_variable": "Estimated population count",
        "use_case": (
            "Supports estimation of exposed population within flood-prone or "
            "flood-detected areas."
        ),
        "kenya_application": (
            "Useful for prioritising warnings and response in Nairobi, Kisumu, "
            "Garissa, Budalangi, Mombasa, and other populated flood-risk locations."
        ),
        "limitations": (
            "Population estimates are modelled and should be used for planning-level "
            "exposure assessment, not exact household counts."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/WorldPop_GP_100m_pop",
    },

    "historical_floods": {
        "gee_id": "GLOBAL_FLOOD_DB/MODIS_EVENTS/V1",
        "name": "Global Flood Database — MODIS Events",
        "resolution": "250 m",
        "update_frequency": "Historical event archive",
        "coverage": "Broad coverage; filter to Kenya historical flood events",
        "key_bands": ["flooded", "duration", "clear_views", "jrc_perm_water"],
        "primary_variable": "Historical flood footprints and duration",
        "use_case": (
            "Historical flood footprint reference for baseline risk mapping, model "
            "training, validation, and flood-prone area screening."
        ),
        "kenya_application": (
            "Useful for comparing current flood-detected areas with historical flood "
            "patterns in Kenya."
        ),
        "limitations": (
            "MODIS resolution is coarse and historical coverage may miss smaller "
            "urban or localised flash-flood events."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/GLOBAL_FLOOD_DB_MODIS_EVENTS_V1",
    },

    "landcover": {
        "gee_id": "GOOGLE/DYNAMICWORLD/V1",
        "name": "Dynamic World — Near Real-Time Land Cover",
        "resolution": "10 m",
        "update_frequency": "Near real-time Sentinel-2 based observations",
        "coverage": "Broad coverage; filter to Kenya monitoring regions",
        "key_bands": [
            "water",
            "trees",
            "grass",
            "flooded_vegetation",
            "crops",
            "built",
            "bare",
            "snow_and_ice",
            "label",
        ],
        "primary_variable": "Land cover class probabilities",
        "use_case": (
            "Supports interpretation of exposed built-up areas, cropland, vegetation, "
            "and water-like surfaces in flood-risk zones."
        ),
        "kenya_application": (
            "Useful for exposure screening in urban areas, floodplains, agricultural "
            "zones, and riparian corridors."
        ),
        "limitations": (
            "Optical imagery can be affected by cloud cover, so it should complement "
            "Sentinel-1 SAR rather than replace it."
        ),
        "catalog_url": "https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1",
    },
}


# ==============================================================================
# Kenya Alert Message Templates
# ------------------------------------------------------------------------------
# These templates are intentionally simple so that gee_agent.tools can generate
# SMS, radio, dashboard, or response-team messages from the same alert level.
# ==============================================================================

ALERT_TEMPLATES = {
    "watch": {
        "emoji": "🟡",
        "level": "FLOOD WATCH",
        "severity": "Low to moderate",
        "meaning": "Conditions may develop into flood risk if rainfall continues.",
        "action": "Monitor conditions closely. Prepare emergency kits and follow official updates.",
        "community_guidance": [
            "Stay alert for weather updates.",
            "Avoid unnecessary movement near rivers and drainage channels.",
            "Prepare important documents, phone charging, medicine, and basic supplies.",
        ],
    },

    "warning": {
        "emoji": "🟠",
        "level": "FLOOD WARNING",
        "severity": "Moderate to high",
        "meaning": "Flooding is possible or likely in vulnerable locations.",
        "action": "Move valuables to higher ground. Avoid river crossings and flood-prone roads.",
        "community_guidance": [
            "Move livestock, documents, and valuables away from low-lying areas.",
            "Avoid walking or driving through flooded roads.",
            "Prepare to move if local authorities advise evacuation.",
        ],
    },

    "alert": {
        "emoji": "🔴",
        "level": "FLOOD ALERT",
        "severity": "High",
        "meaning": "Flooding is likely or already occurring in exposed areas.",
        "action": "Move away from low-lying areas immediately and follow local authority instructions.",
        "community_guidance": [
            "Leave riverbanks, drainage corridors, and floodplains.",
            "Move children, elderly people, and vulnerable persons to safer ground.",
            "Do not cross flooded roads, bridges, or seasonal rivers.",
        ],
    },

    "extreme": {
        "emoji": "🚨",
        "level": "EXTREME FLOOD DANGER",
        "severity": "Very high",
        "meaning": "Severe flooding is expected or ongoing. Immediate protective action is required.",
        "action": "Evacuate immediately if you are in a flood-prone area. Call emergency services if needed.",
        "community_guidance": [
            "Move to higher ground immediately.",
            "Do not attempt to cross moving water.",
            "Follow instructions from local authorities and emergency responders.",
            "Call 999, 112, or local emergency contacts if life is at risk.",
        ],
    },
}


# ==============================================================================
# Kenya Emergency and Response References
# ==============================================================================

KENYA_RESPONSE_CONTACTS = {
    "national_emergency_numbers": ["999", "112"],
    "recommended_local_contacts": [
        "County disaster management office",
        "Local administration",
        "Kenya Red Cross local response team",
        "Nearest police station",
        "Community emergency response volunteers",
    ],
    "note": (
        "Emergency contacts may vary by county. County-specific contacts should be "
        "added to the knowledge base or alert workflow when available."
    ),
}


# ==============================================================================
# Kenya Monitoring Priorities
# ==============================================================================

KENYA_MONITORING_PRIORITIES = {
    "primary_indicators": [
        "Daily rainfall accumulation",
        "Short-duration intense rainfall",
        "Soil moisture saturation",
        "River level or discharge anomaly",
        "Detected flood extent from Sentinel-1 SAR",
        "Population exposure in detected flood zones",
    ],
    "priority_outputs": [
        "Flood watch or warning level",
        "Affected basin or county",
        "Likely flood type",
        "Recommended datasets for confirmation",
        "Community action message",
        "Response-team summary",
    ],
    "decision_notes": (
        "Rainfall and soil moisture thresholds should be treated as screening tools. "
        "Final warnings should consider local observations, official forecasts, "
        "river gauges, terrain, drainage condition, and verified field reports."
    ),
}