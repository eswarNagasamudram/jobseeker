from pydantic import BaseModel, Field
from typing import Optional, List

class JDModel(BaseModel):
    job_description : str = Field(description="The detailed description of the job including the role, responsibilities and the perks. If the field are not available return foo")
    company : str = Field(description="A list of names of the company which has posted the job. The company can be expressed in multiple ways like Amazon or Amazon Pvt Ltd. Add all these names to the list. Examples of company names are Amazon, Flipkart, Google, Meta.If the field are not available return foo")
    hiring_manager : str = Field(description="A list of the names of hiring manager name of the hiring manager who has posted the job. This is usually a name. If the designation is present that is also acceptable.If the field are not available return foo")
    job_role : str = Field(description="The role for the job posted.This is usually like Program manager, Product manager etc.If the field are not available return foo")
    team : str = Field(description="The team in the company which is hiring.If the field are not available return foo")

    # @classmethod
    # def merge(self,other_model) : 
    #     merged_job_description = self.job_description + other_model.job_description
    #     merged_compnay = self.company + other_model.company
    #     merged_hiring_manager = self.hiring_manager + other_model.hiring_manager
    #     merged_role = self.role + other_model.role
    #     team 