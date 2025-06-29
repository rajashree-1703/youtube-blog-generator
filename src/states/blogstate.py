from typing import TypedDict, NotRequired
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str=Field(description="the title of the blog post")
    content:str=Field(description="The main content of the blog post")

class BlogState(TypedDict):
    topic: str
    blog: NotRequired[Blog]
    current_language:str