MCP Server for searching Airbnb and get listing details.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/openbnb-airbnb](https://hub.docker.com/repository/docker/mcp/openbnb-airbnb)
**Author**|[openbnb-org](https://github.com/openbnb-org)
**Repository**|https://github.com/openbnb-org/mcp-server-airbnb

## Available Tools (2)
Tools provided by this Server|Short Description
-|-
`airbnb_listing_details`|Get detailed information about a specific Airbnb listing.|
`airbnb_search`|Search for Airbnb listings with various filters and pagination.|

---
## Tools Details

#### Tool: **`airbnb_listing_details`**
Get detailed information about a specific Airbnb listing. Provide direct links to the user
Parameters|Type|Description
-|-|-
`id`|`string`|The Airbnb listing ID
`adults`|`number` *optional*|Number of adults
`checkin`|`string` *optional*|Check-in date (YYYY-MM-DD)
`checkout`|`string` *optional*|Check-out date (YYYY-MM-DD)
`children`|`number` *optional*|Number of children
`ignoreRobotsText`|`boolean` *optional*|Ignore robots.txt rules for this request
`infants`|`number` *optional*|Number of infants
`pets`|`number` *optional*|Number of pets

---
#### Tool: **`airbnb_search`**
Search for Airbnb listings with various filters and pagination. Provide direct links to the user
Parameters|Type|Description
-|-|-
`location`|`string`|Location to search for (city, state, etc.)
`adults`|`number` *optional*|Number of adults
`checkin`|`string` *optional*|Check-in date (YYYY-MM-DD)
`checkout`|`string` *optional*|Check-out date (YYYY-MM-DD)
`children`|`number` *optional*|Number of children
`cursor`|`string` *optional*|Base64-encoded string used for Pagination
`ignoreRobotsText`|`boolean` *optional*|Ignore robots.txt rules for this request
`infants`|`number` *optional*|Number of infants
`maxPrice`|`number` *optional*|Maximum price for the stay
`minPrice`|`number` *optional*|Minimum price for the stay
`pets`|`number` *optional*|Number of pets
`placeId`|`string` *optional*|Google Maps Place ID (overrides the location parameter)
`propertyType`|`string` *optional*|Filter by property type: 'entire_home' (entire homes/apartments), 'private_room' (private rooms in shared homes), 'shared_room' (shared/dorm-style rooms), 'hotel_room' (hotel rooms)

---
