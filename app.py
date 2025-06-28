import uvicorn
from fastapi import FastAPI, Request

from src.graphs.graph_builder import GraphBuilder
from src.llms.azurellm import AzureLLM

import os
from dotenv import load_dotenv
load_dotenv()

app=FastAPI()

# os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

## API's

@app.post("/blogs")
async def create_blogs(request: Request):
    data=await request.json()
    topic=data.get("topic", "")

    ## get the llm object
    azurellm=AzureLLM()
    llm=azurellm.get_llm()

    ## get the graph
    graph_builder=GraphBuilder(llm)
    
    if topic:
        graph=graph_builder.setup_graph(usecase="topic")
        state=graph.invoke({"topic": topic})

    return {"date": state}

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")