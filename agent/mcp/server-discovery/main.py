import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Define server parameters for stdio connection
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )

    # Establish stdio client connection
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection (perform handshake)
            await session.initialize()

            # List all tools the server provides
            tools_response = await session.list_tools()
            print("Available tools:")
            for tool in tools_response.tools:
                print(f" - {tool.name}: {tool.description}")

            # TODO: List all resources the server provides
            resources_response = await session.list_resources()
            # TODO: Print each resource's URI and description
            for res in resources_response.resources:
                print(f" - {res.uri}: {res.description}")

if __name__ == "__main__":
    asyncio.run(main())