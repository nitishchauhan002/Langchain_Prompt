from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Prompt Template
template = PromptTemplate(
    template="Greet this person in 5 languages. The name of the person is {name}",
    input_variables=["name"]
)

# Fill Placeholder
prompt = template.invoke({"name": "Nitish"})

# Invoke Model
result = model.invoke(prompt)

print(result.content)
