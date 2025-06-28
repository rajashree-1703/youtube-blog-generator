from src.states.blogstate import BlogState


class BlogNode:
    """
    A class to represent the blog node 
    """

    def __init__(self, llm):
        self.llm = llm
    
    def title_creation(self, state: BlogState):
        """
        Create the title of the blog
        """
        
        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert blong content writeer. Use markdown formatiing, Generate 
                   a blog title for the {topic}. This title should be creattive and SEO friendly.

                   """
            
            system_message=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog": {"title": response.content}}
        
    
    def content_genration(self, state: BlogState):
        """
        Generate the content of the blog
        """

        if "topic" in state and state["topic"]:
            system_promt="""
                   You are an expert blong content writeer. Use markdown formatiing, Generate 
                   detailed blog content with detailed breakdown for the {topic}. This content should be creattive and SEO friendly.

                   """
            
            system_message=system_promt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog": {"title": state["blog"]["title"], "content": response.content}}