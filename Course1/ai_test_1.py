from ai_config import openai_llm, get_dataset_summaries, list_csv_files, evaluate_classification_dataset, evaluate_regression_dataset
from langchain_core.tools import tool
from langchain.agents import create_agent

my_agent = create_agent(
    model=openai_llm, 
    tools=[get_dataset_summaries, list_csv_files, evaluate_classification_dataset, evaluate_regression_dataset],
    system_prompt="You are a data science assistant. Use the available tools to analyze CSV files. Your job is to determine whether each dataset is for classification or regression, based on its structure."
)

print("📊 Ask questions about your dataset (type 'exit' to quit):")
config = {"configurable": {"thread_id": "data_science_chat_1"}}

while True:
    user_input=input(" You: ")
    if user_input.strip().lower() in ['exit','quit']:
        print("see ya later")
        break
        
    result = my_agent.invoke(
        {"messages": [("user", user_input)]},
        config=config
    )
    final_answer = result["messages"][-1].content
    print(f"My Agent: {final_answer}\n")