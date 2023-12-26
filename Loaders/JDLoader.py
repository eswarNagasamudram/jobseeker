from AppConfig import AppConfig
from pydantic import BaseModel
from langchain.document_loaders import AsyncHtmlLoader, PyPDFLoader
from langchain.document_transformers import Html2TextTransformer
from Models.JDModel import JDModel
from langchain.output_parsers import PydanticOutputParser
from Prompts.JDParserPrompt import JDParserPrompt
from langchain.llms.vertexai import VertexAI


class JDLoader(BaseModel):
    app_config:AppConfig = None
    loader_type:str = None
    chunk_len:int = None
    num_chunks:int = None
    chunk_overlap:int = None


    class config:
        arbitrary_types_allowed = True
    
    def load_jd_from_pdf(self, path):
        jd_doc = PyPDFLoader(path).load()
        return jd_doc[0].page_content
    
    def load_jd_from_url(self, url) :
        # Get documents from the url
        urls = [url]
        loader = AsyncHtmlLoader(urls, verify_ssl=False)
        docs = loader.load()

        # Tramsform the HTML docs to text using HTML2Text
        html2text = Html2TextTransformer()
        docs_transformed = html2text.transform_documents(docs)
        response = self.parse_job_board(docs_transformed)
        print(response)
        return response
    
    def parse_job_board(self, path):
        jd_doc = PyPDFLoader(path).load()
        parser = PydanticOutputParser(pydantic_object=JDModel)
        prompt = JDParserPrompt().get_prompt()
        # model = OpenAI(openai_api_key=self.app_config.openai_api_key,temperature=0,model="gpt-3.5-turbo-instruct")
        model = VertexAI(model_name= "text-bison", max_output_tokens=1024)
        format_instructions = parser.get_format_instructions()
        # text_splitter = RecursiveCharacterTextSplitter(
        #     chunk_size = 4000,
        #     chunk_overlap = 200,
        #     length_function = len,
        #     is_separator_regex=False
        # )
        # content = docs[0].page_content
        # docs = text_splitter.create_documents([content])
        
        chain = ( 
                    {"format_instructions" : lambda x : x["format_instructions"], 
                     "input" : lambda x : x["input"]} 
                    | prompt
                    | model 
                    
                        )
        responses = chain.invoke({"input": jd_doc[0].page_content, "format_instructions":format_instructions })
        responses = parser.parse(responses)
        # responses = ""
        # for doc in docs :
        #     response = chain.invoke({"format_instructions": format_instructions, "input" : doc.page_content})
        #     response = parser.parse(response)
        #     responses.extend(response)
        
        # chain  = (
        #             {"input" : RunnablePassthrough()}
        #             | prompt
        #             | model
        #             | StrOutputParser()
        # )
        # for doc in docs:
        #     response = chain.invoke(doc.page_content)
        #     responses += "\n"
        #     responses += response
        return responses
        

