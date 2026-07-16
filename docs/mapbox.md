Transform any AI agent into a geospatially-aware system with Mapbox APIs. Provides geocoding, POI search, routing, travel time matrices, isochrones, and static map generation.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/mapbox](https://hub.docker.com/repository/docker/mcp/mapbox)
**Author**|[mapbox](https://github.com/mapbox)
**Repository**|https://github.com/mapbox/mcp-server

## Available Tools (28)
Tools provided by this Server|Short Description
-|-
`area_tool`|Calculate Area|
`bbox_tool`|Calculate Bounding Box|
`bearing_tool`|Calculate Bearing|
`buffer_tool`|Create Buffer Zone|
`category_search_tool`|Category Search Tool|
`centroid_tool`|Calculate Centroid|
`convex_tool`|Convex Hull|
`destination_tool`|Calculate Destination|
`difference_tool`|Difference of Polygons|
`directions_tool`|Directions Tool|
`distance_tool`|Calculate Distance|
`ground_location_tool`|Ground Location Tool|
`intersect_tool`|Intersect Polygons|
`isochrone_tool`|Isochrone Tool|
`length_tool`|Measure Line Length|
`map_matching_tool`|Map Matching Tool|
`matrix_tool`|Matrix Tool|
`midpoint_tool`|Calculate Midpoint|
`nearest_point_on_line_tool`|Nearest Point on Line|
`nearest_point_tool`|Nearest Point|
`optimization_tool`|Optimize Multi-Stop Route|
`place_details_tool`|Place Details Tool|
`points_within_polygon_tool`|Points Within Polygon|
`reverse_geocode_tool`|Reverse Geocode Tool|
`search_and_geocode_tool`|Search and Geocode Tool|
`simplify_tool`|Simplify Geometry|
`static_map_image_tool`|Static Map Image Tool|
`union_tool`|Union Polygons|

---
## Tools Details

#### Tool: **`area_tool`**
Calculate the area of a polygon or multipolygon. Supports various units including square meters, kilometers, acres, and hectares. Works offline without API calls.
Parameters|Type|Description
-|-|-
`geometry`|`string`|Polygon or MultiPolygon coordinates. Polygon: array of rings (first is outer, rest are holes). MultiPolygon: array of polygons.
`units`|`string` *optional*|Unit of measurement for area

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`bbox_tool`**
Calculate the bounding box (extent) of any geometry. Returns the minimum and maximum longitude and latitude that encompass the geometry. Works offline without API calls.
Parameters|Type|Description
-|-|-
`geometry`|`string`|Geometry coordinates (Point, LineString, Polygon, or MultiPolygon)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`bearing_tool`**
Calculate the bearing (compass direction) from one point to another. Returns bearing in degrees where 0° is North, 90° is East, 180° is South, and 270° is West. Works offline without API calls.
Parameters|Type|Description
-|-|-
`from`|`object`|Starting coordinate
`to`|`object`|Ending coordinate

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`buffer_tool`**
Create a buffer zone (polygon) around a point, line, or polygon at a specified distance. Useful for proximity analysis, service areas, or creating zones of influence. Works offline without API calls.
Parameters|Type|Description
-|-|-
`distance`|`number`|Buffer distance
`geometry`|`string`|Geometry coordinates (Point, LineString, or Polygon)
`units`|`string` *optional*|Unit of measurement for distance

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`category_search_tool`**
Return all places that match a category (industry, amenity, or NAICS‑style code). Use when the user asks for a type of place, plural or generic terms like 'museums', 'coffee shops', 'electric‑vehicle chargers', or when the query includes is‑a phrases such as 'any', 'all', 'nearby'. Do not use when a unique name or brand is provided. Supports both JSON and text output formats.
Parameters|Type|Description
-|-|-
`category`|`string`|The canonical place category name to search for (e.g., "restaurant", "hotel", "cafe"). To get the full list of supported categories, use the category_list_tool.
`bbox`|`object` *optional*|Bounding box to limit results within specified bounds
`country`|`array` *optional*|Array of ISO 3166 alpha 2 country codes to limit results
`format`|`string` *optional*|Output format: "json_string" returns raw GeoJSON data as a JSON string that can be parsed; "formatted_text" returns human-readable text with place names, addresses, and coordinates. Both return as text content but json_string contains parseable JSON data while formatted_text is for display.
`language`|`string` *optional*|IETF language tag for the response (e.g., "en", "es", "fr", "de", "ja")
`limit`|`number` *optional*|Maximum number of results to return (1-25)
`poi_category_exclusions`|`array` *optional*|Array of POI categories to exclude from results
`proximity`|`object` *optional*|Location to bias results towards as {longitude, latitude}. If not provided, defaults to IP-based location.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`centroid_tool`**
Calculate the geometric center (centroid) of a polygon or multipolygon. The centroid is the arithmetic mean position of all points in the shape. Works offline without API calls.
Parameters|Type|Description
-|-|-
`geometry`|`string`|Polygon or MultiPolygon coordinates. Polygon: array of rings (first is outer, rest are holes). MultiPolygon: array of polygons.

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`convex_tool`**
Compute the convex hull of a set of points — the smallest convex polygon that contains all the points. Useful for bounding area analysis, estimating coverage area, or wrapping a set of locations. Works offline without API calls.
Parameters|Type|Description
-|-|-
`points`|`array`|Points to compute the convex hull from (minimum 3)

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`destination_tool`**
Calculate a destination point given a starting point, bearing, and distance using geodesic (great-circle) straight-line offset. Useful for "find a point 5km north of X", constructing search offsets, or computing waypoints. Bearing: 0=north, 90=east, 180/-180=south, -90=west. Note: this calculates a straight-line geographic offset, not road-network distance. Works offline without API calls.
Parameters|Type|Description
-|-|-
`bearing`|`number`|Direction of travel in degrees (0=north, 90=east, -90=west, 180=south)
`distance`|`number`|Distance to travel
`origin`|`object`|Starting point
`units`|`string` *optional*|Units for the distance

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`difference_tool`**
Subtract one polygon from another, returning the area in polygon1 that is not covered by polygon2. Useful for computing exclusion zones, finding uncovered service areas, or "what is in zone A but not zone B?". Returns null geometry if polygon2 fully covers polygon1. Works offline without API calls.
Parameters|Type|Description
-|-|-
`polygon1`|`array`|The polygon to subtract from
`polygon2`|`array`|The polygon to subtract

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`directions_tool`**
Fetches directions from Mapbox API based on provided coordinates and direction method. For route planning and distance calculations, use geometries="none" to get compact responses. Only request full geometry (geometries="geojson") when you need to visualize the route on a map or provide detailed turn-by-turn navigation instructions.
Parameters|Type|Description
-|-|-
`coordinates`|`array`|Array of coordinate objects with longitude and latitude properties to visit in order. Must include at least 2 coordinate pairs (starting and ending points). Up to 25 coordinates total are supported.
`alternatives`|`boolean` *optional*|Whether to try to return alternative routes (true) or not (false, default). Up to two alternatives may be returned.
`arrive_by`|`string` *optional*|The desired arrival time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ, YYYY-MM-DDThh:mmss±hh:mm, or YYYY-MM-DDThh:mm). This parameter is only available for the driving profile and is not supported by other profiles, not even driving-traffic. The travel time will be calculated based on historical and real-time traffic data.
`depart_at`|`string` *optional*|The departure time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ, YYYY-MM-DDThh:mmss±hh:mm, or YYYY-MM-DDThh:mm). This parameter is only available for the driving and driving-traffic profiles. The travel time will be calculated based on historical and real-time traffic data.
`exclude`|`string` *optional*|Whether to exclude certain road types and custom locations from routing. Multiple values can be specified as a comma-separated list. Available options:
- All profiles:  ferry, cash_only_tolls
- Driving/Driving-traffic profiles only: motorway, toll, unpaved, tunnel, country_border, state_border or point(<lng> <lat>)
For custom locations you can use Point exclusions (note lng and lat are space separated and at most 50 points are allowed)
Note: country_border excludes all controlled country borders; borders within the Schengen Area are not excluded.
`geometries`|`string` *optional*|The format of the returned geometry. Options: 
- none (default): no geometry object is returned at all, use this if you do not need all of the intermediate coordinates.
- geojson: as GeoJSON LineString (might be very long as there could be a lot of points)
`max_height`|`number` *optional*|The max vehicle height, in meters. The Directions API will compute a route that includes only roads with a height limit greater than or equal to the max vehicle height. Must be between 0 and 10 meters. The default value is 1.6 meters. Only available for driving and driving-traffic profiles.
`max_weight`|`number` *optional*|The max vehicle weight, in metric tons (1000 kg). The Directions API will compute a route that includes only roads with a weight limit greater than or equal to the max vehicle weight. Must be between 0 and 100 metric tons. The default value is 2.5 metric tons. Only available for driving and driving-traffic profiles.
`max_width`|`number` *optional*|The max vehicle width, in meters. The Directions API will compute a route that includes only roads with a width limit greater than or equal to the max vehicle width. Must be between 0 and 10 meters. The default value is 1.9 meters. Only available for driving and driving-traffic profiles.
`routing_profile`|`string` *optional*|Routing profile for different modes of transport. Options: 
- mapbox/driving-traffic (default): automotive with current traffic conditions
- mapbox/driving: automotive based on typical traffic
- mapbox/walking: pedestrian/hiking
- mapbox/cycling: bicycle

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`distance_tool`**
Calculate the distance between two geographic coordinates. Supports various units including kilometers, miles, meters, feet, and nautical miles. Uses the Haversine formula for accurate great-circle distance calculations. This tool works offline without requiring API calls.
Parameters|Type|Description
-|-|-
`from`|`object`|Starting coordinate with longitude and latitude
`to`|`object`|Ending coordinate with longitude and latitude
`units`|`string` *optional*|Unit of measurement for distance

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`ground_location_tool`**
Answer questions about what is near a location, what neighborhood a coordinate is in, or what places are within walking/driving distance. Use this as the FIRST and ONLY tool when given coordinates and asked about nearby places, neighborhood context, local discovery, or area summaries — do NOT also call reverse_geocode_tool or search the web for places. Pass the place category (e.g. "restaurant", "coffee", "park") as the query parameter to get nearby POIs in the same call. Returns place name, nearby POIs matching the query, and travel-time reachability — all sourced from live Mapbox data with citations.
Parameters|Type|Description
-|-|-
`latitude`|`number`|Latitude of the location to ground responses around
`longitude`|`number`|Longitude of the location to ground responses around
`contours_minutes`|`array` *optional*|Travel-time thresholds in minutes for the isochrone. Max 4 values, each between 1-60.
`language`|`string` *optional*|IETF language tag for the response (e.g., "en", "es", "fr", "de", "ja")
`limit`|`number` *optional*|Maximum number of nearby POIs to return (1-25)
`profile`|`string` *optional*|Travel profile for isochrone calculation. Use "mapbox/driving-traffic" for traffic-aware driving. Defaults to "mapbox/walking".
`query`|`string` *optional*|Optional category or type of places to search for nearby (e.g., "restaurant", "coffee", "park"). If omitted, returns general place context only.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`intersect_tool`**
Find the intersection geometry of two polygons — the area they share in common. Useful for coverage overlap analysis, finding shared service areas, or zone overlap. Returns null geometry if the polygons do not overlap. Works offline without API calls.
Parameters|Type|Description
-|-|-
`polygon1`|`array`|First polygon
`polygon2`|`array`|Second polygon

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`isochrone_tool`**
Computes areas that are reachable within a specified amount of time from a location, and returns the reachable regions as contours of Polygons or LineStrings in GeoJSON format that you can display on a map.
  Common use cases:
    - Show a user how far they can travel in X minutes from their current location
    - Determine whether a destination is within a certain travel time threshold
    - Compare travel ranges for different modes of transportation'
Parameters|Type|Description
-|-|-
`coordinates`|`object`|A coordinate object with longitude and latitude properties around which to center the isochrone lines. Longitude: -180 to 180, Latitude: -85.0511 to 85.0511
`generalize`|`number`|Positive number in meters that is used to simplify geometries.
        - Walking: use 0-500. Prefer 50-200 for short contours (minutes < 10 or meters < 5000), 300-500 as they grow.
        - Driving: use 1000-5000. Start at 2000, use 3000 if minutes > 10 or meters > 20000. Use 4000-5000 if near 60 minutes or 100000 meters.
`contours_colors`|`array` *optional*|Contour colors as hex strings without starting # (for example ff0000 for red. must match contours_minutes or contours_meters length if provided).
`contours_meters`|`array` *optional*|Distances in meters. Distances must be in increasing order. Must be specified either contours_minutes or contours_meters.
`contours_minutes`|`array` *optional*|Contour times in minutes. Times must be in increasing order. Must be specified either contours_minutes or contours_meters.
`denoise`|`number` *optional*|A floating point value that can be used to remove smaller contours. A value of 1.0 will only return the largest contour for a given value.
`depart_at`|`string` *optional*|An ISO 8601 date-time string representing the time to depart (format string: YYYY-MM-DDThh:mmss±hh:mm).
`exclude`|`array` *optional*|Exclude certain road types and custom locations from routing.
`polygons`|`boolean` *optional*|Whether to return Polygons (true) or LineStrings (false).
`profile`|`string` *optional*|Mode of travel.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`length_tool`**
Measure the total length of a line defined by a series of coordinates. Useful for measuring a drawn route, path, or boundary without a routing API call. Supports kilometers, miles, meters, and feet. Works offline without API calls.
Parameters|Type|Description
-|-|-
`coordinates`|`array`|LineString coordinates as [longitude, latitude] pairs
`units`|`string` *optional*|Units for the length measurement

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`map_matching_tool`**
Snap GPS traces to roads using Mapbox Map Matching API. Takes noisy/inaccurate coordinate sequences (2-100 points) and returns clean routes aligned with actual roads, bike paths, or walkways. Useful for analyzing recorded trips, cleaning fleet tracking data, or processing fitness activity traces. Returns confidence scores, matched geometry, and optional traffic/speed annotations.
Parameters|Type|Description
-|-|-
`coordinates`|`array`|Array of coordinate objects with longitude and latitude properties representing a GPS trace. Must include at least 2 and up to 100 coordinate pairs. Coordinates should be in the order they were recorded.
`annotations`|`array` *optional*|Additional data to include in the response. Options: 
- speed: Speed limit per segment (km/h)
- distance: Distance per segment (meters)
- duration: Duration per segment (seconds)
- congestion: Traffic level per segment (low, moderate, heavy, severe)
`geometries`|`string` *optional*|Format of the returned geometry. Options: 
- geojson: GeoJSON LineString (recommended)
- polyline: Polyline with precision 5
- polyline6: Polyline with precision 6
`overview`|`string` *optional*|Format of the returned geometry. Options: 
- full: Returns full geometry with all points
- simplified: Returns simplified geometry
- false: No geometry returned
`profile`|`string` *optional*|Routing profile for different modes of transport. Options: 
- driving: automotive based on road network
- driving-traffic: automotive with current traffic conditions
- walking: pedestrian/hiking
- cycling: bicycle
`radiuses`|`array` *optional*|Array of maximum distances (in meters) each coordinate can snap to the road network. If provided, must have the same length as coordinates array. Default is unlimited. Use smaller values (5-25m) for high-quality GPS, larger values (50-100m) for noisy GPS traces.
`timestamps`|`array` *optional*|Array of Unix timestamps (in seconds) corresponding to each coordinate. If provided, must have the same length as coordinates array. Used to improve matching accuracy based on speed.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`matrix_tool`**
Calculates travel times and distances between multiple points using Mapbox Matrix API.
Parameters|Type|Description
-|-|-
`coordinates`|`array`|Array of coordinate objects with longitude and latitude properties. Must include at least 2 coordinate pairs. Up to 25 coordinates total are supported for most profiles (10 for driving-traffic).
`profile`|`string`|Routing profile for different modes of transport. Options: 
- mapbox/driving-traffic (default): automotive with current traffic conditions (limited to 10 coordinates)
- mapbox/driving: automotive based on typical traffic
- mapbox/walking: pedestrian/hiking
- mapbox/cycling: bicycle
`annotations`|`string` *optional*|Specifies the resulting matrices. Possible values are: duration (default), distance, or both values separated by a comma.
`approaches`|`string` *optional*|A semicolon-separated list indicating the side of the road from which to approach waypoints. Accepts "unrestricted" (default, route can arrive at the waypoint from either side of the road) or "curb" (route will arrive at the waypoint on the driving_side of the region). If provided, the number of approaches must be the same as the number of waypoints. You can skip a coordinate and show its position with the ; separator.
`bearings`|`string` *optional*|A semicolon-separated list of headings and allowed deviation indicating the direction of movement. Input as two comma-separated values per location: a heading course measured clockwise from true north between 0 and 360, and the range of degrees by which the angle can deviate (recommended value is 45° or 90°), formatted as {angle,degrees}. If provided, the number of bearings must equal the number of coordinates. You can skip a coordinate and show its position in the list with the ; separator.
`destinations`|`string` *optional*|Use the coordinates at given indices as destinations. Possible values are: a semicolon-separated list of 0-based indices, or "all" (default). The option "all" allows using all coordinates as destinations.
`sources`|`string` *optional*|Use the coordinates at given indices as sources. Possible values are: a semicolon-separated list of 0-based indices, or "all" (default). The option "all" allows using all coordinates as sources.

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`midpoint_tool`**
Calculate the geographic midpoint between two coordinates. Returns the point that is halfway between the two input points along the great circle path. Works offline without API calls.
Parameters|Type|Description
-|-|-
`from`|`object`|Starting coordinate
`to`|`object`|Ending coordinate

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`nearest_point_on_line_tool`**
Snap a point to the nearest position on a line or route. Returns the closest point on the line and the distance to it. Useful for "which point on this route is closest to my location?" or map-matching without the API. Works offline without API calls.
Parameters|Type|Description
-|-|-
`line`|`array`|LineString coordinates as [longitude, latitude] pairs
`point`|`object`|The point to snap to the line
`units`|`string` *optional*|Units for the distance result

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`nearest_point_tool`**
Find the nearest point in a collection to a given target point. More efficient than calling distance_tool for each candidate and sorting. Useful for finding the closest store, stop, or landmark to a location. Works offline without API calls.
Parameters|Type|Description
-|-|-
`points`|`array`|Candidate points to search
`target`|`object`|The reference point to measure from
`units`|`string` *optional*|Distance units for the result

*This tool is read-only. It does not modify its environment.*

---
#### Tool: **`optimization_tool`**
Find the optimal (shortest by travel time) route through a set of 2-12 coordinates. Solves the Traveling Salesman Problem to determine the best visiting order. Supports options for starting point, ending point, and whether to return to start.
Parameters|Type|Description
-|-|-
`coordinates`|`array`|Array of {longitude, latitude} coordinate pairs to optimize a route through. The V1 API supports 2-12 coordinates and returns the optimal visiting order.
`annotations`|`array` *optional*|Additional metadata to include for each route segment
`destination`|`string` *optional*|Location to end the trip. "any" allows any coordinate, "last" forces the last coordinate as end.
`geometries`|`string` *optional*|Format for route geometry
`language`|`string` *optional*|Language for instructions (if steps=true). ISO 639-1 code (e.g., "en", "es").
`overview`|`string` *optional*|Detail level of route geometry
`profile`|`string` *optional*|Routing profile to use for optimization
`roundtrip`|`boolean` *optional*|Whether to return to the starting point. Set to false for one-way trips.
`source`|`string` *optional*|Location to start the trip. "any" allows any coordinate, "first" forces the first coordinate as start.
`steps`|`boolean` *optional*|Whether to include turn-by-turn instructions

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`place_details_tool`**
Retrieve detailed information about a specific place using its Mapbox ID. Use after search_and_geocode_tool, category_search_tool, or reverse_geocode_tool to get additional details such as photos, opening hours, ratings, phone numbers, and website URLs. Requires the mapbox_id field from a previous search result.
Parameters|Type|Description
-|-|-
`mapbox_id`|`string`|The Mapbox ID of the place to retrieve details for. Obtained from search results returned by search_and_geocode_tool, category_search_tool, or reverse_geocode_t

[...]

## Screenshots

![Mapbox screenshot 1](https://raw.githubusercontent.com/Schwaller/plaiiin-mcp-catalog/main/docs/img/mapbox-1.gif)
