# PDF Merger

## Introduction
This Python script utilizes the PyPDF2 library to merge multiple PDF files into a single PDF document. The script takes a list of PDF file names, opens each file, appends its content to a PDF merger object, and finally creates a new PDF file containing the combined content of the input files.

## Features
- **PDF Merger:** Combines multiple PDF files into a single PDF document.
- **Configurable Input:** Specify the names of the input PDF files in the `filess` list.
- **Output File:** The merged PDF content is saved in a file named 'newpdf.pdf'.

## Usage
- **Install PyPDF2:** Ensure that the PyPDF2 library is installed before running the script.
- **Update Input Files:** Modify the `filess` list to include the names of the PDF files you want to merge.
- **Run the Script:** Execute the script in a Python environment.
- **Output:** The merged PDF file, named 'newpdf.pdf', will be created in the same directory as the script.

## Customization
- **Input Files:** Add or remove file names in the `filess` list to customize the set of PDFs to be merged.
- **Output File Name:** Modify the output file name in the `merger.write('newpdf.pdf')` line to suit your preferences.

## Notes
- The script assumes that the input PDF files are in the same directory as the script.
- The PyPDF2 library is used for PDF manipulation, so make sure it is installed before running the script.
