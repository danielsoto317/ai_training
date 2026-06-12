# 🤖 LLM Data Science & Agent Toolkit

A comprehensive collection of interactive tools, applications, and Jupyter notebooks leveraging LangChain and IBM Granite/Llama models to perform advanced data analysis, agent-based tool calling, and automated visualization over structured datasets.

---

## 📁 Repository Structure

```text
├── Course1/
│   ├── Hello World-v1.ipynb
│   ├── Interactive Tool-Calling Agent-v1.ipynb
│   ├── LLM-Powered Data Science-v1.ipynb
│   ├── Tool-Calling-v1.ipynb
│   ├── ai_test_1.py
│   ├── classification_dataset.csv
│   └── regression_dataset.csv
├── .env                     # Your local private keys (Hidden/Ignored by Git)
├── .gitignore               # Prevents tracking of confidential credentials
├── ai_config.py             # Global application configuration file
├── app.py                   # Main application entry point
└── requirements.txt         # Project dependencies
```

---

## 🚀 Getting Started

Follow these steps to set up the project locally on your machine.

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system. You will also need an API key from either IBM Cloud (Watsonx.ai) or OpenRouter depending on your model routing configuration.

### 2. Setup Virtual Environment
Open your terminal in the project directory and run the following commands to isolate your dependencies:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
With your virtual environment activated, install all the required AI frameworks and data science libraries:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

To protect your credentials, API keys are managed via a local `.env` environment file that is entirely ignored by Git tracker profiles.

1. Create a file named exactly `.env` in the root directory.
2. Open the file and input your deployment credentials:

```ini
OPENROUTER_API_KEY=your_openrouter_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

---

## 💻 Running the Projects

### Running the Python Application
To execute the main script directly from your active terminal, run:

```bash
python app.py
```

### Exploring the Interactive Notebooks
To run the interactive data science labs, start your local Jupyter environment:

```bash
jupyter notebook
```

Once open, navigate into the `Course1/` directory to explore the step-by-step implementations:
* **LLM-Powered Data Science**: Running predictive analysis over data tables.
* **Interactive Tool-Calling Agents**: Watching LangChain generate and execute Python code natively to render analytical charts like Seaborn box plots.