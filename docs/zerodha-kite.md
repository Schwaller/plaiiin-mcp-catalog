MCP server for Zerodha Kite Connect API - India's leading stock broker trading platform. Execute trades, manage portfolios, and access real-time market data for NSE, BSE, and other Indian exchanges.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/zerodha-kite](https://hub.docker.com/repository/docker/mcp/zerodha-kite)
**Author**|[anshuljain90](https://github.com/anshuljain90)
**Repository**|https://github.com/anshuljain90/zerodha-kite-mcp

## Available Tools (15)
Tools provided by this Server|Short Description
-|-
`place_order`|Place a new order in the market|
`modify_order`|Modify an existing pending order|
`cancel_order`|Cancel a pending order|
`get_positions`|Get all open positions (intraday and overnight)|
`get_holdings`|Get long-term holdings in demat account|
`get_margins`|Get account margins and available funds|
`get_quote`|Get real-time market quotes for a symbol|
`get_historical_data`|Get historical candlestick data|
`get_instruments`|Get list of all tradeable instruments|
`get_orders`|Get list of all orders for the day|
`get_trades`|Get list of all executed trades|
`get_order_history`|Get complete history of an order including modifications|
`get_profile`|Get user profile information|
`get_ltp`|Get last traded price for multiple instruments|
`get_market_status`|Check if markets are open or closed|

---
## Tools Details

#### Tool: **`place_order`**
Place a new order in the market
Parameters|Type|Description
-|-|-
`exchange`|`string`|Trading exchange (NSE, BSE, NFO, CDS, MCX)
`tradingsymbol`|`string`|Trading symbol (e.g., RELIANCE, INFY)
`transaction_type`|`string`|BUY or SELL
`quantity`|`number`|Number of shares/lots
`order_type`|`string`|Order type (MARKET, LIMIT, SL, SL-M)
`product`|`string`|Product type (CNC for delivery, MIS for intraday, NRML for F&O)
`price`|`number`|Price for LIMIT orders (optional)
`trigger_price`|`number`|Trigger price for SL orders (optional)

---
#### Tool: **`modify_order`**
Modify an existing pending order
Parameters|Type|Description
-|-|-
`order_id`|`string`|Unique order ID
`quantity`|`number`|New quantity (optional)
`price`|`number`|New price (optional)
`order_type`|`string`|New order type (optional)
`trigger_price`|`number`|New trigger price (optional)

---
#### Tool: **`cancel_order`**
Cancel a pending order
Parameters|Type|Description
-|-|-
`order_id`|`string`|Unique order ID to cancel

---
#### Tool: **`get_positions`**
Get all open positions (intraday and overnight)
#### Tool: **`get_holdings`**
Get long-term holdings in demat account
#### Tool: **`get_margins`**
Get account margins and available funds
#### Tool: **`get_quote`**
Get real-time market quotes for a symbol
Parameters|Type|Description
-|-|-
`exchange`|`string`|Exchange (NSE, BSE, etc.)
`tradingsymbol`|`string`|Trading symbol

---
#### Tool: **`get_historical_data`**
Get historical candlestick data
Parameters|Type|Description
-|-|-
`instrument_token`|`string`|Unique instrument identifier
`from_date`|`string`|Start date (YYYY-MM-DD)
`to_date`|`string`|End date (YYYY-MM-DD)
`interval`|`string`|Time interval (minute, 3minute, 5minute, 10minute, 15minute, 30minute, 60minute, day)

---
#### Tool: **`get_instruments`**
Get list of all tradeable instruments
Parameters|Type|Description
-|-|-
`exchange`|`string`|Exchange to fetch instruments for

---
#### Tool: **`get_orders`**
Get list of all orders for the day
#### Tool: **`get_trades`**
Get list of all executed trades
#### Tool: **`get_order_history`**
Get complete history of an order including modifications
Parameters|Type|Description
-|-|-
`order_id`|`string`|Unique order ID

---
#### Tool: **`get_profile`**
Get user profile information
#### Tool: **`get_ltp`**
Get last traded price for multiple instruments
Parameters|Type|Description
-|-|-
`instruments`|`array`|Array of exchange:tradingsymbol pairs

---
#### Tool: **`get_market_status`**
Check if markets are open or closed
