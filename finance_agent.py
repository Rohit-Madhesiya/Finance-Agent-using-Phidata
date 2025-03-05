import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

st.set_page_config(page_title="Finance Agent using Phidata")
st.title("Finance Agent using Phidata")
groq_api_key=st.sidebar.text_input("GROQ API KEY")


web_agent=Agent(
  name="Web Search Agent",
  role="Search the web for information",
  model=Groq(id="deepseek-r1-distill-llama-70b",api_key=groq_api_key),
  tools=[DuckDuckGo()],
  instructions=["Always include sources"],
  show_tool_calls=True,
  markdown=True
)

finance_agent=Agent(
  name="Finance Agent",
  role="Get Financial Data",
  model=Groq(id="deepseek-r1-distill-llama-70b",api_key=groq_api_key),
  tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,company_info=True)],
  instructions=["Use tables to display data"],
  show_tool_calls=True,
  markdown=True
)

agent_team=Agent(
  model=Groq(id="deepseek-r1-distill-llama-70b",api_key=groq_api_key),
  team=[web_agent,finance_agent],
  instructions=["Always include sources","Use tables to display data"],
  show_tool_calls=True,
  markdown=True,
)


question=st.text_input("Ask any Finance or Web Search related Questions")

if st.button("Answer") and groq_api_key:
  response:RunResponse=agent_team.run(question)
  st.write(response.content)
