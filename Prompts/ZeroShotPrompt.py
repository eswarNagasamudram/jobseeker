from pydantic import BaseModel
from langchain.prompts import PromptTemplate

class ZeroShotPrompt(BaseModel):
    text: str = "You are a helpful AI agent who will write personalised cover letters for job applicants. \n \
                Resume of the applicant : \n \
                {resume}\n \
                Job description : \n \
                {job_description} \n \
                Instructions : \n \
                1. Generate a personalised cover letter addressing the team being hired for. For example if the team is marketing address it as  \n \
                Dear marketing team, \n \
                2. Incorporate the job description details to highlight how the experiences of the applicant match with the job requirements \n \
                3. Tailor the letter to showcase that you are ideal candidate for the job \n \
                5. Ensure the letter maintains a professional note and includes a closing expression of gratitude \n \
                6. Use the name of the applicant in the closing expression. \n \
                Cover letter :"
    @classmethod
    def set_prompt(cls, new_prompt: str):
        """Set the prompt text value"""
        return cls(text=new_prompt)

    def get_prompt(self):
        """Return the PromptTemplate"""
        return PromptTemplate.from_template(self.text)