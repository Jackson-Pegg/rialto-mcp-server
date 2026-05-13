# Rialto MCP Server

A Python MCP server that exposes a real estate loan database to MCP client Claude

Built as a prototype of the MCP infrastructure Rialto Capital uses to give the team natural language access to live business data

## Tools

- `get_loan_by_id` — retrieve a specific loan record by ID
- `list_loans_by_market` — filter loans by market (Miami, NYC, Austin)
- `get_loans_by_status` — filter loans by status (current, watchlist, default)
- `get_portfolio_summary` — return high-level portfolio stats including total balance and status breakdown

## Schema Design

Each loan record exposes the fields an asset manager needs to make decisions:
- `id` — unique loan identifier
- `property` — asset name
- `market` — geographic market
- `balance` — outstanding loan balance
- `status` — current, watchlist, or default
- `type` — asset class (office, retail, multifamily, mixed-use)

## Example

> "What loans do we have in Miami?"

Claude queries the MCP server and returns all Miami loans with balances, property types, and watchlist flags.

## Production Notes

In production, the in-memory dataset would be replaced with a live database connection. Credentials would be stored securely in environment variables