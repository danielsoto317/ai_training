from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, START, END  # 💡 Added START constant
from langgraph.types import Command                 # 💡 Modern way to handle routing + state updates
import os
import sys

# 🚀 Tell Python to look one folder up (the root folder) for imports
sys.path.append(os.path.abspath(".."))

# 1. State Definition (Stays clean)
class SalesReportState(TypedDict):
    request: str
    raw_data: Optional[dict]
    processed_data: Optional[dict]
    chart_config: Optional[dict]
    report: Optional[str]
    errors: List[str]

# 2. Modernized Node Handlers (Autonomous Multi-Agent Routing)
def data_collector_agent(state: SalesReportState):
    # If things go wrong, you can route dynamically to the error_handler:
    if not state["request"]:
        return Command(
            update={"errors": ["Empty request received"]}, 
            goto="error_handler"
        )
    
    # Otherwise, update state and pass execution smoothly to the next agent
    return Command(
        update={"raw_data": {"sales": 150000}}, 
        goto="data_processor"
    )

def data_processor_agent(state: SalesReportState):
    # Process the raw data, then hand off control directly to the chart generator
    return Command(
        update={"processed_data": {"clean_sales": 150000}}, 
        goto="chart_generator"
    )

def chart_generator_agent(state: SalesReportState):
    return Command(
        update={"chart_config": {"type": "bar_chart"}}, 
        goto="report_generator"
    )

def report_generator_agent(state: SalesReportState):
    return Command(
        update={"report": "Q1-Q2 2024 Sales look phenomenal!"}, 
        goto=END  # 🏁 Complete the workflow natively
    )

def error_handler_agent(state: SalesReportState):
    # Wrap up and terminate the graph lifecycle safely
    return Command(
        update={"report": "Report generation failed due to structural data errors."}, 
        goto=END
    )

# 3. Constructing the Streamlined Graph Workflow
def create_sales_report_workflow():
    workflow = StateGraph(SalesReportState)

    # Register the nodes normally
    workflow.add_node("data_collector", data_collector_agent)
    workflow.add_node("data_processor", data_processor_agent)
    workflow.add_node("chart_generator", chart_generator_agent)
    workflow.add_node("report_generator", report_generator_agent)
    workflow.add_node("error_handler", error_handler_agent)

    # 🔗 Set the Entry Point using the correct modern edge constant
    workflow.add_edge(START, "data_collector")

    # NOTE: Look how clean this is! You do NOT need any `add_conditional_edges` here.
    # The Command objects returned inside the agent functions handle it natively.

    return workflow.compile()

def run_sales_report_workflow():
    app = create_sales_report_workflow()
    
    # Invoke the compiled graph normally
    final_state = app.invoke({
        "request": "Q1-Q2 2024 Sales Analysis",
        "raw_data": None,
        "processed_data": None,
        "chart_config": None,
        "report": None,
        "errors": []
    })
    
    print("\nFinal Report:\n", final_state.get("report"))
    return final_state

if __name__ == "__main__":
    run_sales_report_workflow()