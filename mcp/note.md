# Limitations of standalone LLMs
As our scheduling assistant example illustrated, here are the primary limitations we encounter with standalone LLMs:

## Fixed knowledge cutoffs: 
Standalone LLMs are trained on vast datasets collected up to a specific point in time, known as their knowledge cutoff. This means their understanding of the world is frozen at that date. If we ask an LLM trained until early 2023 about events from late 2024, it simply won’t know.

## Lack of real-world interaction: 
While LLMs in advanced setups can use tools to interact with the web or other systems, a standalone LLM doesn’t autonomously initiate these actions. Without external tools or an agentic framework, it cannot independently browse, operate software, or control devices.

## No inherent action capabilities: 
LLMs are designed to generate text, not to plan or execute multi-step tasks. While they can provide detailed instructions or elaborate plans, they cannot self-initiate external actions, verify outcomes, or correct themselves based on real-world feedback. They don’t possess an “action module.”

## Challenges in scalability and maintainability for complex applications: 
Relying solely on a single, monolithic LLM for all functionalities in a large application can lead to significant engineering challenges. As systems grow, managing context windows for long conversations, ensuring consistent behavior, and updating underlying models become computationally intensive and complex. A single change might require re-training or careful prompt engineering across the entire system.

# The four pillars of agentic systems
These four foundational components empower an AI agent to operate intelligently and autonomously within its designated environment.

Consider an AI agent optimizing package deliveries:

## Perception: 
It refers to the agent’s ability to understand its environment and gather relevant information. This step monitors live traffic, new delivery requests, package statuses, and vehicle locations.

## Reasoning: 
Once an agent perceives information, it processes data to plan and make decisions. This step analyzes data to determine efficient routes and prioritize deliveries.

## Action: 
This is the agent’s ability to execute reasoned decisions and interact with its environment, often via external tools. The agent updates driver routes, sends customer notifications, and logs deliveries in this step.

## Memory: 
Agents need memory to store and recall past experiences, learned knowledge, and the ongoing state. This step stores historical data to refine operations and learn optimal patterns.
