from pydantic import BaseModel
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class SimplePDFWriter(BaseModel):

    def write_to_pdf(self, file_name, content):
        # Split the cover letter text into paragraphs
        paragraphs = content.split('\n\n')

        # Define styles
        styles = getSampleStyleSheet()

        # Create a PDF document
        pdf_doc = SimpleDocTemplate(file_name, pagesize=letter)
        pdf_elements = []

        # Add applicant name
        name = f"\nEswar Prasanth"
        name_paragraph = Paragraph(name, styles['Heading2'])
        pdf_elements.append(name_paragraph)
        
        email = f"\nprasanthsamudram@gmail.com"
        email_paragraph = Paragraph(email, styles['Italic'])
        pdf_elements.append(email_paragraph)

        pdf_elements.append(Spacer(1, 12))  # Add space after name and email

        # Add each paragraph to the PDF
        for paragraph in paragraphs:
            if paragraph.strip():  # Skip empty paragraphs
                pdf_elements.append(Paragraph(paragraph, styles['BodyText']))
                pdf_elements.append(Spacer(1, 12))  # Add space after each paragraph


        # Build the PDF document
        pdf_doc.build(pdf_elements)

        print(f'Cover letter created and saved as {file_name}.')
