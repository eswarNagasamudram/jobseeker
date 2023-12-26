from AppConfig import AppConfig
from Agents.ZeroShotAgent import ZeroShotAgent
from Loaders.JDLoader import JDLoader

def load_config():
    app_config = AppConfig() 
    return app_config



if __name__ == '__main__':
    
    
    # load config file into an object
    app_config = load_config()
    
    resume_path = "/Users/eswar/coverletter-generator/app/EswarNagasamudram_product.pdf"
    jd_path = "/Users/eswar/coverletter-generator/app/JobDescription.pdf"
    # loader = JDLoader(app_config=app_config)
    # response = loader.parse_job_board(jd_path)
    # print(response)


    #Give each run a name so that the output is saved based on the experiment and output can be compared
    run_name = "zeroshot_first_propmt"

    #Create the agent and generate the cover letter
    zero_shot_agent = ZeroShotAgent(app_config=app_config, run_name=run_name)
    try:
        zero_shot_agent.generate_coverletter(resume_path=resume_path,jd_path=jd_path)
    except Exception as e:
        print(f'Some error occured in generating the coverletter for the run - {run_name}.  \n The exception is as follows : \n {e}')


