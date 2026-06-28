from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt

# Load Environment Variables
load_dotenv()

# Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Streamlit UI
st.set_page_config(page_title="Research Tool", page_icon="📄")

st.title("📄 Research Paper Summarizer")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed Explanation)"
    ]
)

# Load Prompt Template
template = load_prompt("template.json")

if st.button("Summarize"):

    chain = template | model

    with st.spinner("Generating Summary..."):

        try:
            result = chain.invoke(
                {
                    "paper_input": paper_input,
                    "style_input": style_input,
                    "length_input": length_input
                }
            )

            st.success("Summary Generated Successfully!")

            st.markdown(result.content)

        except Exception as e:
            st.error(f"Error: {e}")