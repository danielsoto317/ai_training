🤖 LLM Data Science & Agent Toolkit
A comprehensive collection of interactive tools, applications, and Jupyter notebooks leveraging LangChain and IBM Granite/Llama models to perform advanced data analysis, agent-based tool calling, and automated visualization over structured datasets.

📁 Repository Structure
Plaintext
├── Course1/
│   ├── Hello World-v1.ipynb
│   ├── Interactive Tool-Calling Agent-v1.ipynb
│   ├── LLM-Powered Data Science-v1.ipynb
│   ├── Tool-Calling-v1.ipynb
│   ├── ai_test_1.py
│   ├── classification_dataset.csv
│   └── regression_dataset.csv
├── ai_config.example.py     # Template for your local environment keys
├── app.py                   # Main application entry point
├── requirements.txt         # Project dependencies
└── README.md                # You are here!
🚀 Getting Started
Follow these steps to set up the project locally on your machine.

1. Prerequisites
Ensure you have Python 3.10+ installed on your system. You will also need an API key from either IBM Cloud (Watsonx.ai) or OpenRouter depending on your model routing configuration.

2. Clone and Setup Environment
Open your terminal in the project directory and run the following commands to isolate your dependencies:

Bash
# Create a virtual environment
python -in venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
3. Install Dependencies
With your virtual environment activated, install all the required AI frameworks and data science libraries:

Bash
pip install -r requirements.txt
⚙️ Configuration
To protect your credentials, API keys are managed via a local configuration file that is ignored by Git.

Locate the ai_config.example.py file in the root directory.

Duplicate or rename the file to ai_config.py.

Open ai_config.py and input your respective deployment keys:

Python
# ai_config.py
OPENROUTER_API_KEY = "your_openrouter_key_here"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# Add any specific Watsonx Project IDs or local parameters here
💻 Running the Projects
Running the Python Application
To execute the main script directly from your terminal, run:

Bash
python app.py
Exploring the Interactive Notebooks
To run the interactive data science labs, start the Jupyter environment:

Bash
jupyter notebook
Navigate into the Course1/ directory to explore the step-by-step implementations for:

LLM-Powered Data Science: Running predictive analysis on data tables.

Interactive Tool-Calling Agents: Watching LangChain generate and run Python code natively to render analytical charts like Seaborn box plots.