from pydantic import BaseModel
from AppConfig import AppConfig
from langchain.document_loaders import PyPDFLoader


class ResumeLoader(BaseModel):
    app_config : AppConfig = None
    pdf_path : str = None
    
    class config:
        arbitrary_types_allowed = True
    
    def load_resume_from_pdf(self,path):
        docs = PyPDFLoader(path).load()
        return docs[0].page_content