---
title: Finance Agent Using Phidata
emoji: 📉
colorFrom: indigo
colorTo: green
sdk: streamlit
sdk_version: 1.43.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: An intelligent agent capable of providing financial insights
---

# Finance Agent using Phidata 💹🤖

Welcome to the Finance Agent using Phidata repository! This project leverages the [Phidata](https://github.com/agno-agi/phidata) framework to create an intelligent agent capable of providing real-time financial insights by integrating various data sources and tools. As an **Agentic AI** project, it exemplifies the autonomy and adaptability characteristic of such systems.

## What is Agentic AI? 🧠

Agentic AI refers to artificial intelligence systems capable of independently pursuing goals and managing complex workflows with minimal human oversight. These AI agents are highly adaptive, understanding user needs based on context, formulating plans, and taking specific actions to accomplish objectives.

Unlike deterministic systems that follow fixed rules, Agentic AI operates probabilistically, relying on patterns and likelihoods to make decisions and adapt to changing environments.

## Overview 📝

The Finance Agent utilizes Phidata's capabilities to build a multi-modal agent equipped with memory, knowledge, tools, and reasoning. By integrating financial data retrieval tools and leveraging models like **deepseek-r1-distill-llama-70b**, the agent can analyze market trends, fetch stock data, and provide structured financial analyses.

## Features ✨

- **Market Trend Analysis**: The agent can perform web searches to gather the latest market trends and news.
- **Stock Data Retrieval**: Utilizes tools like YFinance to fetch real-time stock data, including prices, volumes, and historical data.
- **Analyst Recommendations**: Aggregates analyst recommendations to provide insights into stock performance.
- **News Summarization**: Summarizes relevant financial news to keep users informed.

## Getting Started 🚀

To set up and run the Finance Agent locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Rohit-Madhesiya/Finance-Agent-using-Phidata.git
   cd Finance-Agent-using-Phidata

2. **Create a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use 'env\Scripts\activate'
    ```
    
3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Finance Agent:**

    ```bash
    streamlit run finance_agent.py

    
**Usage 🛠️**

Once the agent is running, you can interact with it through the console or integrate it into other applications. The agent accepts natural language queries related to financial data, such as:

* "What are the latest trends in the technology sector?"
* "Provide the current stock price and analyst recommendations for Apple Inc."
* "Summarize the recent news about the automotive industry."

The agent will process these queries and provide detailed, structured responses.
