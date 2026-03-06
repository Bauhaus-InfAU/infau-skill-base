#!/usr/bin/env python3
"""
Convert PDF to Markdown using Docling

This script converts a PDF file to Markdown format using the Docling library.
Based on examples from https://docling-project.github.io/docling/examples/
"""

import os
import warnings
from pathlib import Path

# Disable HuggingFace hub symlink warnings on Windows
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
warnings.filterwarnings('ignore')

def convert_pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert a PDF file to Markdown using Docling
    
    Args:
        pdf_path (str): Path to the input PDF file
        output_path (str, optional): Path for the output Markdown file. 
                                   If None, uses the same name as PDF with .md extension
    """
    try:
        from docling.document_converter import DocumentConverter
        
        # Initialize the converter
        converter = DocumentConverter()
        
        # Convert the document
        print(f"Converting {pdf_path} to Markdown...")
        result = converter.convert(pdf_path)
        
        # Get the document content as Markdown
        markdown_content = result.document.export_to_markdown()
        
        # Determine output path
        if output_path is None:
            # Save to ThüLeNa Framework directory with appropriate name
            output_path = Path("C:/Work/JOB/InfAU/Teaching/ThüLeNa/00_Context/ThüLeNa_Framework/Kurserstellende_Handreichung.md")
        
        # Write the Markdown content to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Successfully converted PDF to Markdown: {output_path}")
        print(f"Document has {len(result.document.pages)} pages")
        
        return str(output_path)
        
    except ImportError as e:
        print(f"Error: Docling is not installed. Please run: pip install docling")
        print(f"Import error: {e}")
        return None
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None

if __name__ == "__main__":
    # Directory containing equipment PDFs
    equipment_dir = r"C:\Work\JOB\InfAU\Teaching\ThüLeNa\.documents\Admin\Equipment"
    
    # Output directory for markdown files
    output_dir = Path(r"C:\Work\JOB\InfAU\Teaching\ThüLeNa\.documents\Admin\Equipment\markdown_outputs")
    output_dir.mkdir(exist_ok=True)
    
    # Find all PDF files in the equipment directory
    pdf_files = list(Path(equipment_dir).glob("*.pdf"))
    
    if not pdf_files:
        print(f"Error: No PDF files found in {equipment_dir}")
        exit(1)
    
    print(f"Found {len(pdf_files)} PDF files to convert:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file.name}")
    
    # Convert each PDF
    successful_conversions = []
    failed_conversions = []
    
    for pdf_file in pdf_files:
        # Create output path with same name as PDF but .md extension
        output_path = output_dir / f"{pdf_file.stem}.md"
        
        print(f"\n--- Converting {pdf_file.name} ---")
        result = convert_pdf_to_markdown(str(pdf_file), str(output_path))
        
        if result:
            successful_conversions.append(pdf_file.name)
        else:
            failed_conversions.append(pdf_file.name)
    
    # Summary
    print(f"\n{'='*50}")
    print(f"CONVERSION SUMMARY")
    print(f"{'='*50}")
    print(f"Successfully converted: {len(successful_conversions)}")
    for file in successful_conversions:
        print(f"  ✓ {file}")
    
    if failed_conversions:
        print(f"\nFailed conversions: {len(failed_conversions)}")
        for file in failed_conversions:
            print(f"  ✗ {file}")
    
    print(f"\nMarkdown files saved to: {output_dir}")