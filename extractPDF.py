import os
import PyPDF2

# Specify the directory containing your PDF files
pdf_directory = 'pdfs'

# Specify the directory where you want to save the text files
output_directory = 'word'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through each PDF file in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        # Build the full file paths
        pdf_file_path = os.path.join(pdf_directory, filename)
        text_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")

        # Open the PDF file in binary mode
        with open(pdf_file_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize an empty string to store the extracted text
            text = ""

            # Iterate through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Get the page object
                page = pdf_reader.pages[page_num]

                # Extract text from the page and append it to the 'text' variable
                text += page.extract_text()

            # Write the extracted text to the corresponding text file
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            print(f"Content from {filename} extracted and saved to {text_file_path}")
