from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Conversation Messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain.")
]

# Invoke Model
result = model.invoke(messages)

# Save AI Response
messages.append(AIMessage(content=result.content))

# Print Conversation
for message in messages:
    print(f"{message.type.upper()}:")
    print(message.content)
    print("-" * 50)