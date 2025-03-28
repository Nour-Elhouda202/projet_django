

from django.shortcuts import render, get_object_or_404
from .models import MainTitle
import PyPDF2

def title(request, main_title_id):
    # الحصول على العنوان الرئيسي باستخدام الـ slug
   main_title = get_object_or_404(MainTitle, id=main_title_id)
   pdf_content = ""
   try:
        reader = PyPDF2.PdfReader(main_title.description)
        for page in reader.pages:
            pdf_content += page.extract_text()
   except Exception as e:
        pdf_content = f"حدث خطأ أثناء قراءة ملف PDF: {str(e)}"
    
    # تقسيم النص إلى فقرات
   paragraphs = []
   if pdf_content:
        # تقسيم النص بناءً على الأسطر الفارغة
        paragraphs = pdf_content.split('#')  # يفترض أن الأسطر الفارغة تفصل بين الفقرات
    
    # إعداد البيانات لتمريرها إلى النموذج
   context = {
        'main_title': main_title,
        'paragraphs': paragraphs,  # تمرير الفقرات بدلاً من النص الكامل
    }
    
    # عرض البيانات في النموذج
   return render(request, 'title/title.html', context)