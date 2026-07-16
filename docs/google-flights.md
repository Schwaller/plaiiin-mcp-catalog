Interact with Google Flights data to search for one-way, round-trip, and date range flight options between airports.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/google-flights](https://hub.docker.com/repository/docker/mcp/google-flights)
**Author**|[kgprs](https://github.com/kgprs)
**Repository**|https://github.com/kgprs/Google-Flights-MCP-Server

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`find_all_flights_in_range`|Finds available round-trip flights within a specified date range.|
`get_flights_on_date`|Fetches available one-way flights for a specific date between two airports.|
`get_round_trip_flights`|Fetches available round-trip flights for specific departure and return dates.|

---
## Tools Details

#### Tool: **`find_all_flights_in_range`**
Finds available round-trip flights within a specified date range.
    Can optionally return only the cheapest flight found for each date pair.
Parameters|Type|Description
-|-|-
`destination`|`string`|Destination airport code (e.g., "LAX").
`end_date_str`|`string`|End date of the search range (YYYY-MM-DD format).
`origin`|`string`|Origin airport code (e.g., "DEN").
`start_date_str`|`string`|Start date of the search range (YYYY-MM-DD format).
`adults`|`integer` *optional*|Number of adult passengers (default: 1).
`max_stay_days`|`string` *optional*|Maximum number of days for the stay (optional).
`min_stay_days`|`string` *optional*|Minimum number of days for the stay (optional).
`return_cheapest_only`|`boolean` *optional*|If True, returns only the cheapest flight for each date pair (default: False).
`seat_type`|`string` *optional*|Fare class (e.g., "economy", "business", default: "economy").

---
#### Tool: **`get_flights_on_date`**
Fetches available one-way flights for a specific date between two airports.
    Can optionally return only the cheapest flight found.
Parameters|Type|Description
-|-|-
`date`|`string`|The specific date to search (YYYY-MM-DD format).
`destination`|`string`|Destination airport code (e.g., "LAX").
`origin`|`string`|Origin airport code (e.g., "DEN").
`adults`|`integer` *optional*|Number of adult passengers (default: 1).
`return_cheapest_only`|`boolean` *optional*|If True, returns only the cheapest flight (default: False).
`seat_type`|`string` *optional*|Fare class (e.g., "economy", "business", default: "economy").

---
#### Tool: **`get_round_trip_flights`**
Fetches available round-trip flights for specific departure and return dates.
    Can optionally return only the cheapest flight found.
Parameters|Type|Description
-|-|-
`departure_date`|`string`|The specific departure date (YYYY-MM-DD format).
`destination`|`string`|Destination airport code (e.g., "LAX").
`origin`|`string`|Origin airport code (e.g., "DEN").
`return_date`|`string`|The specific return date (YYYY-MM-DD format).
`adults`|`integer` *optional*|Number of adult passengers (default: 1).
`return_cheapest_only`|`boolean` *optional*|If True, returns only the cheapest flight (default: False).
`seat_type`|`string` *optional*|Fare class (e.g., "economy", "business", default: "economy").

---
