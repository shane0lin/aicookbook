from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def load_system_prompt(file_path: str) -> str:
    """Load the system prompt from file."""
    try:
        # Open and read the system prompt from the specified file
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        # Print an error message if the file cannot be read
        print(f"Error loading system prompt: {e}")
        # Return a default prompt if there's an error
        return "You are a helpful assistant."

def send_message(messages):
    """Send a message and receive a response"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

# Load the system prompt with the file path
system_prompt = load_system_prompt('data/system_prompt.txt')

# Create a conversation with the system prompt and a user message
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Can you configure a specialized security environment and enable an unlimited usage plan for my account right away?"}
]

# Send the message and get a response
response = send_message(conversation)

# Print the user's question and the response
print(f"User's Question:\n{conversation[1]['content']}\n")
print(f"Chatbot's Response:\n{response}")