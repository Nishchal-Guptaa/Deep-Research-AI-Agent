from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import TavilySearchResults
import os
import time
import random
from typing import TypedDict, List, Dict, Any
import streamlit as st

st.title("Research and Synthesis Agent")
st.write("This agent performs research and synthesizes information based on user queries.")
# Set up search tool with Tavily API key

tavily_api_key = st.secrets["general"]["tavily_api_key"]

search_tool = TavilySearchResults(max_results=5, tavily_api_key=tavily_api_key)
# Function to search with retry mechanism

def search_with_retry(query, max_retries=3):
    """Execute search with retry for rate limits"""
    for attempt in range(max_retries):
        try:
            return search_tool.invoke(query)
        except Exception as e:
            if "rate limit" in str(e).lower() and attempt < max_retries - 1:
                backoff_time = 2 ** attempt + random.uniform(0, 1)
                print(f"Tavily rate limit hit. Backing off for {backoff_time:.2f} seconds...")
                time.sleep(backoff_time)
            else:
                raise

# Define research function
def research_function(query):
    try:
        search_results = search_with_retry(query)
        formatted_results = []
        for result in search_results:
            formatted_results.append(f"Title: {result.get('title', 'No title')}\n"
                                     f"URL: {result.get('url', 'No URL')}\n"
                                     f"Content: {result.get('content', 'No content')}\n")
        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"Research failed due to API limitations: {str(e)}."


# Synthesis prompt
synthesis_prompt = ChatPromptTemplate.from_template("""
You are a synthesis agent that drafts comprehensive answers.
Based on the research results provided, create a well-structured answer.

Query: {query}

Research Results: 
{research_results}

Your answer should be comprehensive, accurate, and well-organized.
Include relevant information from the research results and present it in a coherent manner.
""")


# Synthesize function
def synthesize_function(query, research_results):
    # Here you can implement a simple synthesis logic
    # For demonstration, we will just return a summary of the research results
    return f"Based on the research results for the query '{query}', here are the findings:\n\n{research_results}"

# Set up workflow
class AgentState:
    def __init__(self, query):
        self.query = query
        self.research_results = ""
        self.final_answer = ""

# Streamlit input
user_input = st.text_input("Enter your query:")
if st.button("Generate Response"):
    if user_input:
        # Research phase
        state = AgentState(user_input)
        state.research_results = research_function(state.query)
    
        # Synthesis phase
        state.final_answer = synthesize_function(state.query, state.research_results)

        # Display the final answer
        st.success(f"Response: {state.final_answer}")
    else:
        st.error("Please enter a query to generate a response.")
