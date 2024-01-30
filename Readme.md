# PDF Merger

## Introduction
This Python script utilizes the PyPDF2 library to merge multiple PDF files into a single PDF document. The script takes a list of PDF file names, opens each file, appends its content to a PDF merger object, and finally creates a new PDF file containing the combined content of the input files.

## Features
<ul>
<li><b>PDF Merger: </b>Combines multiple PDF files into a single PDF document.</li>
<li><b>Configurable </b>Input: Specify the names of the input PDF files in the filess list.</li>
<li><b>Output File: </b>The merged PDF content is saved in a file named 'newpdf.pdf'.</li>
</ul>

## Usage
<li><b>Install PyPDF2: </b>Ensure that the PyPDF2 library is installed before running the script.</li>
<li><b>Update Input Files: </b>Modify the filess list to include the names of the PDF files you want to merge.</li>
<li><b>Run the Script: </b>Execute the script in a Python environment.</li>
<li><b>Output:</b> The merged PDF file, named 'newpdf.pdf', will be created in the same directory as the script.</li>

## Customization
<li>Input Files: Add or remove file names in the filess list to customize the set of PDFs to be merged.</li>
<li>Output File Name: Modify the output file name in the merger.write('newpdf.pdf') line to suit your preferences.</li>

## Notes
<li>The script assumes that the input PDF files are in the same directory as the script.</li>
<li>The PyPDF2 library is used for PDF manipulation, so make sure it is installed before running the script.</li>
