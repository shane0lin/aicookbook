import uuid
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Store all active chat sessions
chat_sessions = {}

# Define a common system prompt for all conversations
system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

# Create a new chat session with a unique identifier
def create_chat():
    chat_id = str(uuid.uuid4())  # Create unique session identifier
    chat_sessions[chat_id] = []  # Initialize empty conversation history
    chat_sessions[chat_id].append(system_prompt)  # Add system prompt to conversation history
    return chat_id

# Send a message in a specific chat session and get a response
def send_message(chat_id, user_message):
    # Ensure we're adding to a valid conversation
    if chat_id not in chat_sessions:
        raise ValueError("Chat session not found!")
    
    # Add the new message to conversation history
    chat_sessions[chat_id].append({"role": "user", "content": user_message})
    
    # Get AI's response while maintaining conversation context
    response = client.chat.completions.create(
        model="gpt-4",
        messages=chat_sessions[chat_id]  # Full history for context
    )
    
    # Process response and maintain conversation history
    answer = response.choices[0].message.content.strip()
    chat_sessions[chat_id].append({"role": "assistant", "content": answer})
    return answer

# TODO: Create the first chat session and store its id
chat_id_1 = create_chat()
# TODO: Send a first message in Chat 1 and print the response
response1_1 = send_message(chat_id_1, "What is Python?")
print("assistant1: ", response1_1)
# TODO: Send a follow-up message in Chat 1 and print the response
response1_2 = send_message(chat_id_1, "Give me 3 most popular refence to start learning Python")
print("assistant1: ", response1_2)
# TODO: Create the second chat session and store its id
chat_id_2 = create_chat()
# TODO: Send a first message in Chat 2 and print the response
response2_1 = send_message(chat_id_2, "What is Java?")
print("assistant2: ", response2_1)
# TODO: Send a follow-up message in Chat 2  and print the response
response2_2 = send_message(chat_id_2, "Give me 3 most popular refence to start learning Java")
print("assistant2: ", response2_2)

# TODO: Print both conversation histories to confirm they are separate