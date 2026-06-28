<div align="center">

# 🔗 Langchain_Prompt

### A hands-on exploration of LangChain's prompt engineering & conversational AI building blocks

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Gemini-2.5--Flash-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](#)
[![Made with ❤](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=for-the-badge)](#)

<br/>

*A modular collection of LangChain scripts exploring prompt templates, chat history, message types, and LLM-powered apps — built with Gemini & OpenAI.*

[🔗 Live Repo](https://github.com/nitishchauhan002/Langchain_Prompt) •
[Modules](#-modules) •
[Tech Stack](#-tech-stack) •
[Architecture](#%EF%B8%8F-architecture) •
[Quick Start](#-quick-start) •
[Roadmap](#%EF%B8%8F-roadmap)

</div>

---

## 📖 Overview

**Langchain_Prompt** is a structured set of standalone Python scripts that progressively explore the core building blocks of **LangChain** — from basic LLM invocation to reusable prompt templates, structured chat messages, conversation memory, and a fully interactive Streamlit-based research-paper summarizer app.

Each script is intentionally self-contained, making this repo a practical **reference/learning kit** for anyone exploring how to build LLM-powered applications with prompt templates, message-based chat history, and multi-provider model integration (Google Gemini + OpenAI).

| | |
|---|---|
| 👤 **Author** | Nitish Kumar Singh ([@nitishchauhan002](https://github.com/nitishchauhan002)) |
| 🧪 **Category** | Generative AI / LLM Application Development |
| 🏗️ **Framework** | LangChain (LCEL — LangChain Expression Language) |
| 🤖 **Models Used** | Google Gemini 2.5 Flash, OpenAI GPT-4 |
| 🖥️ **UI Layer** | Streamlit |

---

## 🧩 Modules

| File | What it Demonstrates |
|---|---|
| `test.py` | Minimal LangChain setup — invoking Gemini with a single prompt |
| `temperature.py` | Controlling LLM creativity/randomness via the `temperature` parameter (OpenAI GPT-4) |
| `prompt_generator.py` | Building a reusable `PromptTemplate` with input variables and saving it as `template.json` |
| `template.json` | Serialized prompt template — paper summarizer with style & length controls |
| `prompt_template.py` | Loading & invoking a `PromptTemplate` dynamically with runtime variables |
| `prompt_ui.py` | Full **Streamlit web app** — research paper summarizer using a loaded prompt template + Gemini |
| `messages.py` | Structured conversation using `SystemMessage`, `HumanMessage`, and `AIMessage` |
| `message_placeholder.py` | Injecting dynamic chat history into a `ChatPromptTemplate` via `MessagesPlaceholder` |
| `chat_prompt_template.py` | Multi-variable `ChatPromptTemplate` with system + human roles |
| `chatbot.py` | A fully interactive **CLI chatbot** with persistent in-memory chat history |
| `chat_history.txt` | Sample stored conversation used to simulate prior chat context |

---

## 🧰 Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **LLM Framework** | ![LangChain](https://img.shields.io/badge/-LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) (Prompts, Messages, Chains — LCEL) |
| **LLM Providers** | ![Gemini](https://img.shields.io/badge/-Google%20Gemini-4285F4?style=flat-square&logo=googlegemini&logoColor=white) ![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white) |
| **Web UI** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) |
| **Config Management** | `python-dotenv` (`.env` based API key management) |
| **Data Format** | JSON (serialized prompt templates) |
| **Version Control** | ![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white) |

</div>

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[User Input] --> B[PromptTemplate /<br/>ChatPromptTemplate]
    B --> C{LCEL Chain<br/>prompt | model}
    C --> D[LLM Provider]
    D -->|Gemini 2.5 Flash| E[Google Generative AI]
    D -->|GPT-4| F[OpenAI API]
    C --> G[AI Response]
    G --> H[Chat History<br/>SystemMessage / HumanMessage / AIMessage]
    H -->|MessagesPlaceholder| B
    G --> I[Streamlit UI / CLI Output]
```

**Conceptual flow covered across scripts:**
1. **Direct invocation** → send a raw string to the model (`test.py`)
2. **Prompt templating** → parameterize prompts with `PromptTemplate` (`prompt_template.py`, `prompt_generator.py`)
3. **Serialization** → save/load reusable prompts as JSON (`template.json`)
4. **Structured messages** → model roles via `SystemMessage` / `HumanMessage` / `AIMessage` (`messages.py`)
5. **Conversational memory** → maintain and replay chat history (`chatbot.py`, `message_placeholder.py`)
6. **Productionizing** → wrap it all in a Streamlit UI (`prompt_ui.py`)

---

## 📁 Project Structure

```
Langchain_Prompt/
├── 🧪 test.py                     # Basic Gemini invocation
├── 🌡️ temperature.py              # Temperature/creativity control demo (OpenAI)
├── 📝 prompt_generator.py         # Create & save a PromptTemplate
├── 📄 template.json               # Saved prompt template (paper summarizer)
├── 🧩 prompt_template.py          # Load & invoke a PromptTemplate
├── 🖥️ prompt_ui.py                # Streamlit app — Research Paper Summarizer
├── 💬 messages.py                 # System/Human/AI message structuring
├── 🗂️ message_placeholder.py      # Dynamic chat history injection
├── 🤖 chatbot.py                  # Interactive CLI chatbot with memory
├── 💭 chat_prompt_template.py     # Multi-role ChatPromptTemplate demo
├── 📜 chat_history.txt            # Sample stored conversation
└── 📘 README.md
```

---

## 🚀 Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/nitishchauhan002/Langchain_Prompt.git
cd Langchain_Prompt
```

### 2️⃣ Set up environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install langchain langchain-google-genai langchain-openai python-dotenv streamlit
```

### 3️⃣ Configure API keys

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 4️⃣ Run individual scripts

```bash
python test.py                     # Basic Gemini call
python temperature.py              # GPT-4 with temperature control
python prompt_generator.py         # Generate template.json
python prompt_template.py         # Dynamic prompt invocation
python messages.py                 # Structured chat messages
python chat_prompt_template.py    # Multi-role chat template
python message_placeholder.py     # Chat history placeholder demo
python chatbot.py                  # Interactive CLI chatbot
```

### 5️⃣ Launch the Streamlit app

```bash
streamlit run prompt_ui.py
```

Then open `http://localhost:8501` to use the **Research Paper Summarizer** — pick a paper, an explanation style, and a length, and get an AI-generated summary instantly.

---

## 🖥️ Featured App: Research Paper Summarizer

A polished Streamlit interface (`prompt_ui.py`) that lets users:
- 📑 Choose from popular ML research papers (Attention Is All You Need, BERT, GPT-3, Diffusion Models)
- 🎯 Select an explanation style (Beginner-Friendly, Technical, Code-Oriented, Mathematical)
- 📏 Pick a summary length
- ⚡ Generate a tailored summary via a reusable, JSON-serialized prompt template + Gemini

---

## 🗺️ Roadmap

- [ ] 🔗 Add LangChain output parsers (Pydantic/structured output)
- [ ] 🧠 Integrate vector store + retrieval (RAG) for grounded paper summarization
- [ ] 💾 Replace `chat_history.txt` with persistent storage (SQLite/Redis)
- [ ] 🌐 Deploy the Streamlit app (Streamlit Community Cloud / HuggingFace Spaces)
- [ ] 🔁 Add LangGraph-based agent workflows
- [ ] 🧪 Add unit tests for prompt template validation

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

<div align="center">

**Nitish Kumar Singh**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nitishchauhan002)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nitish-kumar-singh-4802792bb/)

⭐ If this project helped you, consider giving it a star on [GitHub](https://github.com/nitishchauhan002/Langchain_Prompt)!

</div>
