from pydantic import BaseModel
from langchain.prompts import PromptTemplate

class JDParserPrompt(BaseModel):
    text: str = "You are a helpful AI agent who will parse a text input of a job board into structured job details.\n \
                The format instructions are as follows \n \
                {format_instructions}\n \
                Job description  : \n \
                {input} \n \
                Output : "
    # text : str = "Format the user input based on the format instructions.\n \
    #               Format instructions : \n {format_instructions}\n \
    #               user input : \n {input}"

    # text : str = "Given user input of text extracted from a HTML page of a job board as below \n \
    #             {input} \n \
    #             Respond with only the content relevant to job posting and ignore the rest"

    @classmethod
    def set_prompt(cls, new_prompt: str):
        """Set the prompt text value"""
        return cls(text=new_prompt)

    def get_prompt(self):
        """Return the PromptTemplate"""
        return PromptTemplate.from_template(self.text)