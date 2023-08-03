from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseServerError
from django.contrib import messages
from .models import Blog, List_Blog

# Create your views here.



def home(request):
    return render(request, 'index.html')

def form_page(request):
    return render(request,'register_form.html')


def blog(request):
    blog = Blog.objects.all()
    list_blog = List_Blog.objects.all()
    return render(request,'blog.html', {"blog":blog, "list_blog":list_blog})



def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not (name and email and subject and message):
            return HttpResponseServerError("All fields are required.")
        
        try:
            # Change the recipient email to the desired address
            recipient_email = "admin@csed.org.ng"
            
            # Change the email sender to a valid email address on your server
            from_email = email
            
            # Email content
            email_body = f"You have received a new message from your website contact form.\n\nHere are the details:\n\nName: {name}\n\nEmail: {email}\n\nSubject: {subject}\n\nMessage: {message}"
            
            # Send the email
            send_mail(subject, email_body, from_email, [recipient_email])
            # ert_script = "<script>alert('your message send successful');</script>" 
            messages.success(request, 'Your message has been sent successfully!')
            # Optionally, you can display a success message or redirect to a thank-you page
            return redirect('contactUs')
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")
    else:
        # Handle GET request or display the contact form
        return render(request, 'index.html')  
    
    
    
     
    
def form(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        subject = request.POST.get('program')
        commite = request.POST.get('commite')
        source = request.POST.get('source')
        employ = request.POST.get('employ')
        current_employ = request.POST.get('current')
        tech = request.POST.get('tech')
        state = request.POST.get('state')
        nationality = request.POST.get('nationality')
        option = request.POST.get('option')
        expectation = request.POST.get('expectation')
        hear = request.POST.get('hear')
        industry = request.POST.get('industry')

        if not (name and email and phone and gender and subject and commite and source and employ and current_employ and tech and state and nationality and option and expectation and hear and industry):
            return HttpResponseServerError("All fields are required.")
        
        try:
            # Change the recipient email to the desired address
            recipient_email = "admin@csed.org.ng"
            
            # Change the email sender to a valid email address on your server
            from_email = email
            
            # Email content
            email_body = f"You have received a application message from your Website!\n\nHere are the details:\n\nName: {name}\n\nEmail: {email}\n\nWhatsAPP_Phone: {phone}\n\nGender: {gender}\n\nProgram_Select: {subject}\n\nTime_Commite: {commite}\n\nGood_Internet_Source: {source}\n\nCurrently_employee:{employ}\n\nIndustry_employ:{current_employ}\n\ntech_business:{tech}\n\nState:{state}\n\nNationality:{nationality}\n\nOption_About_you:{option}\n\nExpectations:{expectation}\n\nHear_about_program:{hear}\n\nIndustry:{industry}"
            
            # Send the email
            send_mail(subject, email_body, from_email, [recipient_email])
            # ert_script = "<script>alert('your message send successful');</script>" 
            messages.success(request, 'Thank you for Applying!')
            
            # Optionally, you can display a success message or redirect to a thank-you page
            return redirect('form')
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")
    else:
        # Handle GET request or display the contact form
        return render(request, 'register_form.html')      