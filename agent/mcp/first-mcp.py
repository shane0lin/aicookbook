from mcp.server.fastmcp import FastMCP

# Create a basic MCP server with a name and description
mcp = FastMCP(
    name="Basic MCP Server",
    description="A simple MCP server that demonstrates initial setup and stdio transport."
)

if __name__ == "__main__":
    mcp.run(transport="stdio")


# mcp dev first-mcp.py
# CLIENT_PORT=3000 SERVER_PORT=8000 mcp dev first-mcp.py