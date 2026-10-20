import dotenv
from langchain.agents import create_agent
from typing import Dict, Any
from tavily import TavilyClient
from langchain.tools import tool
from pydantic import BaseModel
from langchain.messages import HumanMessage

dotenv.load_dotenv()

tavily_client = TavilyClient()

class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    steps: list[str]
    description: str
    servings: int

@tool
def web_search(query : str) -> Dict[str, Any]:
    """Search the web for information"""

    return tavily_client.search(query)

system_prompt = ("""You are a chef in 5 star restaurant. You excell in making Indian food. The user will give you a list of ingredients they have in their house."
                 
                 Using the websearch tool, search the web for recipies that can be made with the Ingredients present.
                 
                 You can use only the ingredients given to you(which i have).""")

chef_agent = create_agent(
    model='google_genai:gemini-3.1-flash-lite',
    system_prompt = system_prompt,
    tools = [web_search],
    response_format=Recipe
)

question = HumanMessage(content="I have some left over Chicken and rice.")

config = {"configurable" : {"thread_id": 1}}

response = chef_agent.invoke(
    {'messages': [question],},
    config,
)

print(response["messages"][-1].content)