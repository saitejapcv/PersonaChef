# PersonaChef

PersonaChef is a LangChain agent that acts as a five-star Indian chef. Give it the ingredients you have available and it can suggest a recipe, optionally searching the web for supporting information. Its answers follow a structured recipe format: name, description, ingredients, steps, and servings.

The agent is exposed to LangGraph Studio through `main.py` and `langgraph.json`.

## What it uses

- **LangChain** to create the agent
- **Google Gemini** (`gemini-3.1-flash-lite`) as the language model
- **Tavily** for web search
- **Pydantic** to enforce the recipe response schema
- **LangGraph Studio** to inspect and interact with the agent visually

## Project layout

```text
.
├── main.py         # Defines the Recipe schema, web-search tool, and chef_agent
├── langgraph.json  # Registers chef_agent for LangGraph Studio
├── pyproject.toml  # Project and dependency configuration
└── project.ipynb   # Notebook exploration/development
```

## Prerequisites

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) (recommended for dependency management)
- A Google AI API key
- A Tavily API key

## Setup

1. Clone the repository and enter the project directory.

2. Install the dependencies:

   ```bash
   uv sync
   ```

3. Create a `.env` file in the project root:

   ```env
   GOOGLE_API_KEY=your_google_ai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   LANGSMITH_PROJECT=personal_chef
   
   ```

   Keep this file private—do not commit API keys to version control.

## Run the agent locally

The example in `main.py` asks the chef what to make from leftover chicken and rice.

```bash
uv run python main.py
```

The response is printed after the agent completes its run.

## Open in LangGraph Studio

`langgraph.json` registers the agent under the name `agent` and points Studio to `main.py:chef_agent`.

Start the local LangGraph development server:

```bash
uv run langgraph dev
```

Then open the local Studio URL shown in the terminal. Select the `agent` graph and send it a message such as:

```text
I have paneer, tomatoes, onions, rice, and common Indian spices. What can I cook?
```

## Agent response format

PersonaChef is configured with this recipe schema:

```json
{
  "name": "Recipe name",
  "description": "A short description",
  "ingredients": ["ingredient 1", "ingredient 2"],
  "steps": ["step 1", "step 2"],
  "servings": 2
}
```

## Configuration notes

- The system prompt instructs the agent to specialize in Indian food and use only the ingredients provided by the user.
- The `web_search` tool uses Tavily and is available to the agent when it needs outside information.
- Update the model identifier in `main.py` if you want to use a different Google Gemini model.

