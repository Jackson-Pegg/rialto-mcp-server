from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Rialto Loan Database")

# Schema design: each loan record is flat (no nested objects) to keep MCP tool responses
# token-efficient and easy for LLMs to reason over. Fields chosen reflect the minimum
# viable data an asset manager needs to triage a position: identity (id, property),
# geography (market), exposure (balance), risk bucket (status), and collateral type (type).
# In production these records would be hydrated from a loan-level database; status would
# be computed nightly from covenant tests and payment history rather than stored directly.
LOANS = [
    {"id": "L001", "property": "Brickell Office Tower", "market": "Miami", "balance": 15000000, "status": "current", "type": "office"},
    {"id": "L002", "property": "Wynwood Retail Center", "market": "Miami", "balance": 8500000, "status": "watchlist", "type": "retail"},
    {"id": "L003", "property": "Manhattan Mixed-Use", "market": "NYC", "balance": 42000000, "status": "current", "type": "mixed-use"},
    {"id": "L004", "property": "Brooklyn Multifamily", "market": "NYC", "balance": 21000000, "status": "default", "type": "multifamily"},
    {"id": "L005", "property": "Coral Gables Office Park", "market": "Miami", "balance": 11000000, "status": "current", "type": "office"},
    {"id": "L006", "property": "Austin Tech Campus", "market": "Austin", "balance": 33000000, "status": "watchlist", "type": "office"},
]

@mcp.tool()
def get_loan_by_id(loan_id: str) -> dict:
    """Get a specific loan record by its ID"""
    for loan in LOANS:
        if loan["id"] == loan_id:
            return loan
    return {"error": f"Loan {loan_id} not found"}

@mcp.tool()
def list_loans_by_market(market: str) -> list:
    """List all loans in a specific market"""
    results = [loan for loan in LOANS if loan["market"].lower() == market.lower()]
    if not results:
        return [{"error": f"No loans found in {market}"}]
    return results

@mcp.tool()
def get_portfolio_summary() -> dict:
    """Get high-level summary statistics for the entire loan portfolio"""
    total_balance = sum(loan["balance"] for loan in LOANS)
    status_counts = {}
    for loan in LOANS:
        status_counts[loan["status"]] = status_counts.get(loan["status"], 0) + 1
    return {
        "total_loans": len(LOANS),
        "total_balance": total_balance,
        "status_breakdown": status_counts
    }

@mcp.tool()
def get_loans_by_status(status: str) -> list:
    """Filter loans by risk status. Valid values: current, watchlist, default."""
    valid_statuses = {"current", "watchlist", "default"}
    normalized = status.lower()
    if normalized not in valid_statuses:
        return [{"error": f"Invalid status '{status}'. Must be one of: {', '.join(sorted(valid_statuses))}"}]
    results = [loan for loan in LOANS if loan["status"] == normalized]
    if not results:
        return [{"error": f"No loans found with status '{normalized}'"}]
    return results

if __name__ == "__main__":
    mcp.run()