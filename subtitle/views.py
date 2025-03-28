from django.shortcuts import get_object_or_404, render
from .models import SubTitle
import PyPDF2

def subtitle(request, subtitle_id):
    sub_title = get_object_or_404(SubTitle, id=subtitle_id)
    pdf_content = ""
    try:
        reader = PyPDF2.PdfReader(sub_title.description)
        for page in reader.pages:
            pdf_content += page.extract_text()
    except Exception as e:
        pdf_content = f"erreur du PDF: {str(e)}"
    
    
    paragraphs = []
    if pdf_content:
        paragraphs = pdf_content.split('#')    
    
    structured_content = []
    split_paragraphs=[]
    for paragraph in paragraphs:
        sub_paragraphs = paragraph.split('*')  
        split_paragraphs.append(sub_paragraphs)
        
    context = {
        'sub_title': sub_title,
        'paragraphs': split_paragraphs,  
    }
    return render(request, 'subtitle/subtitle.html', context)