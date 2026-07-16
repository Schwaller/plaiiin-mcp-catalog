Place search, geocoding, and route optimization.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/aws-location-mcp-server](https://hub.docker.com/repository/docker/mcp/aws-location-mcp-server)
**Author**|[awslabs](https://github.com/awslabs)
**Repository**|https://github.com/awslabs/mcp

## Available Tools (8)
Tools provided by this Server|Short Description
-|-
`calculate_route`|Calculate a route and return summary info and turn-by-turn directions.|
`geocode`|Get coordinates for a location name or address using Amazon Location Service geo-places geocode API.|
`get_place`|Get details for a place using Amazon Location Service geo-places get_place API.|
`optimize_waypoints`|Optimize the order of waypoints using Amazon Location Service geo-routes optimize_waypoints API (V2).|
`reverse_geocode`|Reverse geocode coordinates to an address using Amazon Location Service geo-places reverse_geocode API.|
`search_nearby`|Search for places near a location using Amazon Location Service geo-places search_nearby API.|
`search_places`|Search for places using Amazon Location Service geo-places search_text API.|
`search_places_open_now`|Search for places that are open now using Amazon Location Service geo-places search_text API and filter by opening hours.|

---
## Tools Details

#### Tool: **`calculate_route`**
Calculate a route and return summary info and turn-by-turn directions.

Parameters:
    departure_position: [lon, lat]
    destination_position: [lon, lat]
    travel_mode: 'Car', 'Truck', 'Walking', or 'Bicycle' (default: 'Car')
    optimize_for: 'FastestRoute' or 'ShortestRoute' (default: 'FastestRoute')

Returns:
    dict with distance, duration, and turn_by_turn directions (list of step summaries).
Parameters|Type|Description
-|-|-
`departure_position`|`array`|Departure position as [longitude, latitude]
`destination_position`|`array`|Destination position as [longitude, latitude]
`optimize_for`|`string` *optional*|Optimize route for 'FastestRoute' or 'ShortestRoute' (default: 'FastestRoute')
`travel_mode`|`string` *optional*|Travel mode: 'Car', 'Truck', 'Walking', or 'Bicycle' (default: 'Car')

---
#### Tool: **`geocode`**
Get coordinates for a location name or address using Amazon Location Service geo-places geocode API.
Parameters|Type|Description
-|-|-
`location`|`string`|Location name or address to geocode

---
#### Tool: **`get_place`**
Get details for a place using Amazon Location Service geo-places get_place API. Output is standardized and includes all fields, even if empty or not available.
Parameters|Type|Description
-|-|-
`place_id`|`string`|The unique PlaceId for the place
`mode`|`string` *optional*|Output mode: 'summary' (default) or 'raw' for all AWS fields

---
#### Tool: **`optimize_waypoints`**
Optimize the order of waypoints using Amazon Location Service geo-routes optimize_waypoints API (V2).

Returns summary (optimized order, total distance, duration, etc.) or full response if mode='raw'.
Parameters|Type|Description
-|-|-
`destination_position`|`array`|Destination position as [longitude, latitude]
`origin_position`|`array`|Origin position as [longitude, latitude]
`waypoints`|`array`|List of intermediate waypoints, each as a dict with at least Position [longitude, latitude], optionally Id
`mode`|`string` *optional*|Output mode: 'summary' (default) or 'raw' for all AWS fields
`travel_mode`|`string` *optional*|Travel mode: 'Car', 'Truck', 'Walking', or 'Bicycle' (default: 'Car')

---
#### Tool: **`reverse_geocode`**
Reverse geocode coordinates to an address using Amazon Location Service geo-places reverse_geocode API.
Parameters|Type|Description
-|-|-
`latitude`|`number`|Latitude of the location
`longitude`|`number`|Longitude of the location

---
#### Tool: **`search_nearby`**
Search for places near a location using Amazon Location Service geo-places search_nearby API. If no results, expand the radius up to max_radius. Output is standardized and includes all fields, even if empty or not available.
Parameters|Type|Description
-|-|-
`latitude`|`number`|Latitude of the center point
`longitude`|`number`|Longitude of the center point
`max_results`|`integer` *optional*|Maximum number of results to return
`query`|`string` *optional*|Optional search query
`radius`|`integer` *optional*|Search radius in meters

---
#### Tool: **`search_places`**
Search for places using Amazon Location Service geo-places search_text API. Geocode the query using the geocode API to get BiasPosition. If no results, try a bounding box filter. Includes contact info and opening hours if present. Output is standardized and includes all fields, even if empty or not available.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query (address, place name, etc.)
`max_results`|`integer` *optional*|Maximum number of results to return
`mode`|`string` *optional*|Output mode: 'summary' (default) or 'raw' for all AWS fields

---
#### Tool: **`search_places_open_now`**
Search for places that are open now using Amazon Location Service geo-places search_text API and filter by opening hours. If no open places, expand the search radius up to max_radius. Uses BiasPosition from geocode.
Parameters|Type|Description
-|-|-
`query`|`string`|Search query (address, place name, etc.)
`initial_radius`|`integer` *optional*|Initial search radius in meters for expansion

---

## Screenshots

![Amazon Location Service screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-location-1.png)

![Amazon Location Service screenshot 2](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-location-2.png)

![Amazon Location Service screenshot 3](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/assets/img/aws-location-3.png)
