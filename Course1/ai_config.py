# 1. LangChain Core Components (Everything your manual chain actually uses)
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# 2. Standard Data Science & Utility Packages
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # Standard plotting convention
import seaborn as sns            # Standard styling convention
import sklearn
import openai

import glob
import os
from typing import List, Optional, Dict, Any

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# API KEYS
OPENROUTER_API_KEY = ""
OPENROUTER_BASE_URL = ""

os.environ["OPENAI_API_BASE"] = OPENROUTER_BASE_URL
os.environ["OPENAI_API_KEY"] = OPENROUTER_API_KEY

DATAFRAME_CACHE = {}


openai_llm = ChatOpenAI(
    model="gpt-4.1-nano", 
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base=OPENROUTER_BASE_URL,
    timeout=10.0
)

watsonx_llm = ChatOpenAI(
    model="ibm-granite/granite-4.1-8b",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base=OPENROUTER_BASE_URL,
    timeout=10.0
)
