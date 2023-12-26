# from reportlab.pdfgen import canvas

# def hello(c):
#     c.drawString(100,100,"Hello World")
# c = canvas.Canvas("hello.pdf")
# hello(c)
# c.showPage()
# c.save()
"""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_cover_letter(output_pdf, applicant_name, applicant_email, cover_letter_text):
    # Split the cover letter text into paragraphs
    paragraphs = cover_letter_text.split('\n\n')

    # Define styles
    styles = getSampleStyleSheet()

    # Create a PDF document
    pdf_doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    pdf_elements = []

    # Add applicant name and email
    name_and_email = f"{applicant_name}\n{applicant_email}"
    name_and_email_paragraph = Paragraph(name_and_email, styles['Heading1'])
    pdf_elements.append(name_and_email_paragraph)
    pdf_elements.append(Spacer(1, 12))  # Add space after name and email

    # Add each paragraph to the PDF
    for paragraph in paragraphs:
        if paragraph.strip():  # Skip empty paragraphs
            pdf_elements.append(Paragraph(paragraph, styles['BodyText']))
            pdf_elements.append(Spacer(1, 12))  # Add space after each paragraph

    # Add closing salutation with applicant's name on the next line
    closing_salutation_paragraph = Paragraph(f"Sincerely,<br/>{applicant_name}", styles['Heading2'])
    pdf_elements.append(closing_salutation_paragraph)

    # Build the PDF document
    pdf_doc.build(pdf_elements)

    print(f"Cover letter created and saved as '{output_pdf}'.")

# Example usage
applicant_name = "John Doe"
applicant_email = "john.doe@example.com"
cover_letter_text = 
"""


"""
Dear Hiring Team,

I am writing to express my interest in the Sr. Program Manager position within the Regulatory Intelligence, Safety, and Compliance team at Amazon. With my background in process improvement and strategic analysis, I believe I am an ideal candidate for this role.

Throughout my career, I have consistently demonstrated my ability to identify areas for improvement and develop innovative solutions to optimize processes. In my previous role as a Product Head at Rupeek, I led the design and development of a dynamic pricing model for gold loans based on customer risk and behavioral analysis. This resulted in a 22% improvement in revenue, driven by a 15% improvement in yield and a 6% improvement in loan tenor.

In addition to my technical skills, I have a proven track record of effectively managing cross-functional teams and driving strategic initiatives. At McKinsey & Company, I was part of several successful projects, including a digital transformation for a leading public sector bank and an advanced analytics implementation for a global bank. In these roles, I collaborated with diverse teams to gather requirements, prioritize features, and deliver impactful solutions within tight deadlines.

Furthermore, my experience as an Equities Trading Strategist at Goldman Sachs has equipped me with a deep understanding of financial markets and risk management. I led the development of a robust trading engine for irregular settlement of equities, which generated an annual revenue of $15 million. This project required close collaboration with compliance, risk, legal, and information security teams to ensure a smooth implementation.

I am confident that my strong analytical skills, strategic mindset, and collaborative nature make me an excellent fit for this role. I am excited about the opportunity to contribute to Amazon's mission of protecting customers and empowering business partners. I am eager to further discuss how my experiences align with your team's goals and objectives.

Thank you for considering my application. I look forward to the opportunity to discuss my qualifications in more detail.
"""
"""
output_pdf = "cover_letter_output.pdf"
create_cover_letter(output_pdf, applicant_name, applicant_email, cover_letter_text)

# Instructions to draw the PDF using ReportLab

You will write a python code for a class which will generate a cover letter PDF. The class should have a function which takes in the following values as arguments and generate the PDF.
Arguments
1. Name of the applicant
2. Role applying to
3. hiring manager 
4. Company name
5. Email of the applicant
6. Cover letter text
Follow the below instructions in formatting the PDF
1. Leave a decent margin to the left
2. First line is Name of the applicant aligned to the left
"""
from typing import List
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field, validator
from langchain.llms.vertexai import VertexAI

class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

    # You can add custom validation logic easily with Pydantic.
    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question!")
        return field
# And a query intented to prompt a language model to populate the data structure.
joke_query = "Tell me a joke."

# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

_input = prompt.format_prompt(query=joke_query)

model = VertexAI(model_name="text-bison", max_output_tokens=1024)
output = model(_input.to_string())
print(f"input : \n {_input.to_string()}")
print(f"output : \n {output}")
print(f"Output is of type - {type(parser.parse(output))}")






