from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
# Chat History
chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

print("=" * 50)
print("🤖 Gemini Chatbot")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # Add user message
    chat_history.append(HumanMessage(content=user_input))

    # Generate AI response
    result = model.invoke(chat_history)

    # Save AI response
    chat_history.append(AIMessage(content=result.content))

    print("AI:", result.content)
    print()

# Print  Chat History
print("\n========== Chat History ==========\n")

for message in chat_history:
    print(f"{message.type.upper()}:")
    print(message.content)
    print("-" * 50)
