from pydantic import BaseModel
from AppConfig import AppConfig
from langchain.llms.vertexai import VertexAI
from Prompts.ZeroShotPrompt import ZeroShotPrompt
from langchain.schema.output_parser import StrOutputParser
from datetime import datetime
from Loaders.JDLoader import JDLoader
from langchain.llms.vertexai import VertexAI
from Loaders.ResumeLoader import ResumeLoader
from Prompts.ZeroShotPrompt import ZeroShotPrompt
from langchain.schema.output_parser import StrOutputParser
from Writers.SimplePDFWriter import SimplePDFWriter

class ZeroShotAgent(BaseModel):
    app_config : AppConfig = None
    run_name : str = "run-"+ datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    class config:
        arbitrary_types_allowed = True

    def generate_coverletter(self, resume_path:str, jd_path:str):
        
        # Load resume
        resume_loader = ResumeLoader(app_config= self.app_config)
        resume = resume_loader.load_resume_from_pdf(resume_path)
        
        #Load JD
        jd_loader = JDLoader(app_config=self.app_config)
        job_description = jd_loader.load_jd_from_pdf(jd_path)

        zero_shot_prompt = ZeroShotPrompt().get_prompt()
        llm = VertexAI(model_name= "text-bison", max_output_tokens=1024)
        chain = (
            {"resume" : lambda x : x["resume"],
             "job_description" : lambda x : x["job_description"]
             }
             | zero_shot_prompt
             | llm
             | StrOutputParser()
            )
        cover_letter_content = chain.invoke({ "resume": resume,
                                        "job_description" : job_description})
        writer = SimplePDFWriter()
        writer.write_to_pdf(f'{self.run_name}_output.pdf',cover_letter_content)        
    
