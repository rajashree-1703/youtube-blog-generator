from langgraph.graph import StateGraph, START, END
from src.llms.azurellm import AzureLLM
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Builds a grpah to geenrate a blog topic.
        """

        self.blog_node_obj=BlogNode(self.llm)


        ## Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_creation", self.blog_node_obj.content_genration)

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", END)

        return self.graph
    
    def setup_graph(self, usecase):
        if usecase=="topic":
            self.build_topic_graph()

        return self.graph.compile()