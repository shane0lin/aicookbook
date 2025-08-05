Discovering MCP Servers in Python
Introduction to the Model Context Protocol
Welcome to the first lesson of our course on developing and integrating Model Context Protocol (MCP) servers in Python. In the previous course, you built a strong foundation in how AI agents work and explored the basics of the OpenAI Agents SDK. Now, we are ready to take the next step: learning how to connect these agents to the outside world using the Model Context Protocol.

The rise of MCP marks a major shift in how large language models (LLMs) interact with external tools, data, and software environments. MCP is quickly becoming the standard for connecting AI models to real-world applications, and major AI labs are adopting it to streamline their workflows.

In this lesson, you will learn how to set up and run a basic MCP server using the official Python SDK. We will focus on two main ways to run your server: using standard input/output (stdio) and using Server-Sent Events (SSE). By the end of this lesson, you will be able to launch your own MCP server and understand when to use each transport method.

Overview of the Model Context Protocol (MCP)
The Model Context Protocol (MCP) is an open standard developed by Anthropic in late 2024. Its main goal is to make it easy for LLMs to interact with external systems, tools, and data sources in a consistent and reliable way. Before MCP, developers had to create custom solutions for every integration, which were time-consuming and often fragile. MCP solves this by providing a universal framework for exchanging context and commands between AI models and software environments.

With MCP, AI models can easily connect to external tools to perform tasks like solving math problems, searching the web, querying databases, or managing files—without needing custom code for each integration. This means you can give your AI agent new abilities simply by plugging in the right MCP-compatible tool, making it much easier to extend what your AI can do in real-world applications.

MCP has quickly gained traction in the AI community. OpenAI, for example, added MCP support to its Agents SDK and ChatGPT desktop apps in early 2025. Google DeepMind and other major labs have also adopted MCP to improve how their models connect with external tools. This widespread adoption shows that MCP is not just a passing trend — it is becoming the backbone of modern AI integrations.

Understanding MCP Hosts, Clients, and Servers
Before you start building your own MCP server, it’s helpful to understand the three main roles in the MCP ecosystem: host, client, and server. These terms come up often when working with MCP, and knowing what each one does will make it much easier to design and debug your integrations.

Host:
The host is the main application that brings everything together. Think of it as the “home base” where AI models run and interact with external tools. Examples of hosts include AI-powered apps like ChatGPT Desktop, Claude Desktop, or custom agent frameworks. The host is responsible for managing connections to different tools and making sure everything works smoothly and securely.

Client:
A client acts as a bridge between the host and an external server. Each client manages a single connection to one MCP server. The client’s job is to send requests from the host to the server, and to deliver responses back. Clients help keep things organized and secure by isolating each server connection, so that tools don’t interfere with each other.

Server:
The server is the external tool or service that provides new capabilities to the host. For example, an MCP server might let the AI model access a database, call a web API, or control a smart device. Servers can run locally on your computer or remotely on another machine. When you build an MCP server in Python, you are creating one of these external tools that the host (via a client) can connect to and use.


In short:

The host is the main AI app or environment.
The client is the connector that links the host to a specific server.
The server is the service that provides external tools and resources.
Understanding these roles will help you see where your MCP server fits in the bigger picture, and how it will interact with other parts of the system.

How Agents Use Tools via MCP
In the Model Context Protocol (MCP), tools are the primary primitives that enable AI agents to perform actions and computations beyond their inherent capabilities. By integrating tools, agents can interact with external systems, execute functions, and retrieve real-time data, thereby enhancing their autonomy and functionality.

MCP utilizes JSON-RPC 2.0, a stateless, lightweight remote procedure call protocol that employs JSON for message formatting, to facilitate seamless interaction between AI agents and external tools. This standardized approach ensures consistent and reliable communication, allowing agents to dynamically discover and invoke tools as needed.

The interaction process between agents and tools via MCP involves several key steps:

Tool Discovery: The agent queries the MCP server to retrieve a list of available tools, each accompanied by a name, description, and the parameters it accepts.

Example Request:

JSON
Copy to clipboard
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list"
}
Example Response:

JSON
Copy to clipboard
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "name": "get_weather",
      "description": "Retrieves current weather information for a specified location.",
      "parameters": {
        "location": {
          "type": "string",
          "description": "City name or coordinates"
        }
      }
    }
  ]
}
Tool Invocation: When the agent determines that a specific tool is needed to fulfill a task, it sends a request to the server, specifying the tool's name and providing the necessary parameters.

Example Request:

JSON
Copy to clipboard
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "Paris"
    }
  }
}
Receiving Results: The server processes the request, executes the tool, and returns the results to the agent, which can then incorporate this information into its response or further processing.

Example Response:

JSON
Copy to clipboard
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "temperature": 18,
    "unit": "Celsius",
    "condition": "Cloudy"
  }
}
By adhering to the JSON-RPC 2.0 standard, MCP ensures consistent and reliable communication between AI agents and external tools. This standardized communication allows AI agents to seamlessly integrate external functionalities, such as querying databases, sending emails, or performing calculations, thereby extending their utility beyond their built-in capabilities.

Why MCP Is Compared to the USB-C Port
You might hear people say that MCP is like the “USB-C port for AI.” This comparison helps highlight what makes MCP so powerful and important.

Before USB-C, connecting devices to your computer was messy—different gadgets needed different cables and ports, and not everything worked together. USB-C changed that by providing a single, universal connector that works for charging, data transfer, displays, and more. Now, you can plug almost anything into a USB-C port and expect it to just work.

MCP does something similar for AI agents and external tools. In the past, every time you wanted your AI model to use a new tool or data source, you had to build a custom integration—often with lots of tricky, one-off code. With MCP, there’s now a universal “port” or protocol that any tool or service can use to connect to any AI agent that supports MCP. This means:

Plug-and-play: You can add new tools to your AI agent as easily as plugging in a USB-C device—no custom wiring required.
Interoperability: Tools and agents from different companies can work together, as long as they speak MCP.
Future-proofing: As new tools and capabilities are developed, they can be added to your AI environment without major rewrites.
In short, MCP is to AI integrations what USB-C is to hardware: a single, flexible, and reliable way to connect everything together.

The Official MCP Python SDK and CLI
To make it easy for developers to build and integrate MCP-compatible servers in Python, Anthropic—through the ModelContextProtocol GitHub organization—provides an official MCP Python SDK. This SDK abstracts away the details of the MCP specification and transport mechanisms like stdio and server-sent events (SSE), so you can focus on your server’s core functionality instead of protocol implementation. The SDK is open source and available on GitHub.

Alongside the SDK, the package also includes a command-line interface (CLI) tool. The CLI provides useful commands for developing, running, and managing MCP servers. For example, you can use the CLI to run your server in development mode with mcp dev, or to interact with and inspect MCP servers during development.

In your own projects, you would typically install the SDK and CLI together with:

Bash
Copy to clipboard
pip install "mcp[cli]"
Or, if you use uv for dependency management:

Bash
Copy to clipboard
uv add "mcp[cli]"
However, for this course, you will be working in the CodeSignal coding environment, where all the necessary installation steps have already been taken care of. You can start using both the MCP SDK and CLI right away without any setup.

With the SDK and CLI ready to use in your environment, you’re all set to start building your own MCP server and connecting it to the outside world.

Understanding stdio and SSE Transport Mechanisms
When you run an MCP server, you need to decide how it will communicate with clients (other programs or applications that want to use your server). There are two main ways to do this: stdio and SSE.

stdio (Standard Input/Output):
This is the most basic and traditional way for programs on the same computer to talk to each other. With stdio, one program sends messages by writing text to its output, and the other program reads those messages as input. This is how many command-line tools work together.

Common uses: Local development, testing, or when your server is being run as a background process by another program.
Recommended when: Both the client and server are on the same machine, or you are building tools that will be used from the command line.
SSE (Server-Sent Events):
SSE is a web technology that allows your server to send real-time updates to clients over the internet using HTTP. With SSE, your server can "push" messages to web browsers or other networked programs as soon as something happens, without the client having to keep asking for updates.

Common uses: Web applications, dashboards, or any situation where you want to send live updates to users or other systems over a network.
Recommended when: You need your server to communicate with web apps, or when clients and servers are on different machines or need to talk over the internet.
In summary:

Use stdio for simple, local, or command-line-based integrations.
Use SSE for real-time, web-based, or networked scenarios where you want to push updates to clients as they happen.
It's worth noting that the Model Context Protocol has introduced a new transport mechanism called Streamable HTTP, which aims to simplify communication by using a single HTTP endpoint for bidirectional messaging, and may eventually replace the previous HTTP with Server-Sent Events (SSE) transport for some purposes. However, for the purposes of this lesson, we will focus on the stdio and SSE transports, as they are foundational and widely used in MCP implementations.

Running an MCP Server with stdio
To create your own MCP server, you’ll use the FastMCP class from the official MCP Python SDK. When you set up your server, it’s important to give it a clear name and description. The name helps clients identify your server, and the description explains what your server can do. This information is especially useful when your server is listed or discovered by other tools.

Here’s a minimal example of how to define and run an MCP server using the stdio transport:

Python
Copy to clipboard
from mcp.server.fastmcp import FastMCP

# Create an MCP server with a name and description
mcp = FastMCP(
    name="My Server",
    description="Provides functionalities to do things"
)

if __name__ == "__main__":
    # Run the server using stdio transport
    mcp.run(transport="stdio")
In this code:

You import the FastMCP class and create a server instance, specifying its name and description.
The if __name__ == "__main__": block ensures the server only starts when you run this script directly.
When you use stdio as the transport, your server is designed to be run as a background process by another program, such as an AI agent or a command-line tool. The server will wait for requests from the client and respond through standard input and output streams. To see your server in action and inspect its behavior, you can use the MCP CLI’s development command, which also launches the MCP Inspector—a web-based tool for interactively testing and debugging your MCP server. The MCP Inspector lets you send requests, try out your server’s tools, and view responses in real time.

When you run:

Bash
Copy to clipboard
mcp dev your_file_name.py
The CLI will start your server using the stdio transport and automatically launch the MCP Inspector in your browser. You’ll see output similar to:

Plain text
Copy to clipboard
Starting MCP inspector...
⚙️ Proxy server listening on port 6277
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
The MCP CLI automatically selects available ports for the proxy server and the Inspector web interface (in this example, ports 6277 and 6274). You don’t need to specify these ports yourself; the CLI handles port selection to avoid conflicts with other services on your machine. You can open the Inspector URL in your browser to interactively send requests, test your server’s endpoints, and debug its behavior while it runs with the stdio transport.

Choosing the Inspector Ports When Running with mcp dev
By default, when you run your MCP server with the mcp dev command, the CLI automatically selects available ports for the MCP Inspector web interface and the proxy server. However, you may want to specify which ports to use—especially if you have other services running or need to avoid port conflicts.

You can control the ports by setting the CLIENT_PORT and SERVER_PORT environment variables before running the command:

CLIENT_PORT sets the port for the Inspector's web interface.
SERVER_PORT sets the port for the MCP proxy server.
For example, to run the Inspector on port 3000 and the proxy server on port 9000, use:

Bash
Copy to clipboard
CLIENT_PORT=3000 SERVER_PORT=9000 mcp dev your_file_path.py 
You will see output similar to:

Plain text
Copy to clipboard
Starting MCP inspector...
⚙️ Proxy server listening on port 9000
🔍 MCP Inspector is up and running at http://127.0.0.1:3000 🚀
This allows you to control exactly where the Inspector and proxy server are accessible, making it easier to integrate with your development workflow or avoid conflicts with other applications.

Running an MCP Server with SSE
Now, let’s see how to run the same MCP server using the SSE transport. This is useful when you want your server to be accessible over the network, such as from a web application or another remote client.

Here is the updated code:

Python
Copy to clipboard
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(
    name="My Server",
    description="Provides functionalities to do things",
    port=8080  # Optional: specify the port to run the server on
)

if __name__ == "__main__":
    # Run the server with sse transport
    mcp.run(transport="sse")
When running with SSE, the MCP Python SDK uses the uvicorn ASGI server internally to serve your MCP server over HTTP. By default, if you do not specify a port, the server will listen on port 8000. You can override this default by providing the port argument when creating the FastMCP instance, as shown above.

To run this server, you can use the standard Python command:

Bash
Copy to clipboard
python your_file_name.py
You will see output similar to:

Plain text
Copy to clipboard
INFO:     Started server process [351]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
Once started, your server will be accessible at http://localhost:<port>, where <port> is the port you specified or the default 8000. Clients can connect to this endpoint and receive real-time updates via Server-Sent Events. This makes SSE ideal for web-based integrations, dashboards, or any scenario where you want to push live updates to clients over the network.

