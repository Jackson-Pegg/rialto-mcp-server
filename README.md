# Rialto MCP Server

A Python MCP (Model Context Protocol) server that exposes a real estate loan database to AI assistants like Claude.

Built as a prototype of the MCP infrastructure Rialto Capital uses to give investment professionals natural language access to live business data.

## Tools

- `get_loan_by_id` — retrieve a specific loan record by ID
- `list_loans_by_market` — filter loans by market (Miami, NYC, Austin)
- `get_portfolio_summary` — return high-level portfolio stats including total balance and status breakdown

## Example

> "What loans do we have in Miami?"

Claude queries the MCP server and returns all Miami loans with balances, property types, and watchlist flags.

## Stack

- Python
- FastMCP (MCP SDK)
- Claude Desktop
