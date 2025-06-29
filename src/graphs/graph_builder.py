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

    def build_langauge_graph(self):
        """
        Build a graph for blog generation with inputs topic anfd language
        """

        self.blog_node_obj=BlogNode(self.llm)

        ##Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_creation", self.blog_node_obj.content_genration)
        self.graph.add_node("hindi_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "hindi"}))
        self.graph.add_node("french_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "french"}))
        self.graph.add_node("route",self.blog_node_obj.route)

        ## Edges and conditional edges

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", "route")

        ## Conditional edges
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            {
                "hindi": "hindi_translation",
                "french": "french_translation"
            }
        )

        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)

        return self.graph
    

    def setup_graph(self, usecase):
        if usecase=="topic":
            self.build_topic_graph()
        if usecase=="language":
            self.build_langauge_graph()

        return self.graph.compile()

## Below code is for the langsmith langgrapg studio
llm= AzureLLM().get_llm()

## get the graph
graph_builder = GraphBuilder(llm)
graph=graph_builder.build_langauge_graph()
