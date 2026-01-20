from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import ContactMessage

def home(request):
    return render(request, "portfolio/home.html")

def about(request):
    return render(request, "portfolio/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        title = request.POST.get("title")
        message = request.POST.get("message")
        
        if not all([name, email, title, message]):
            messages.error(request, "All fields are required.")
            return redirect("contact")
        
        subject = f"[Portfolio] {title}"
        full_message = (
        "You have received a new message from your portfolio website.\n\n"
        
        f"Name   : {name}\n"
        f"Email   : {email}\n"
        f"Title     : {title}\n"
        "\n\n"
        f"{message}\n\n"
        "\n"
        "This message was sent via your portfolio contact form."
        )
        
        ContactMessage.objects.create (
            name=name,
            email=email,
            title=title,
            message=message,
        )
        
        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently = False,
        )
        
        messages.success(
            request,
            "Thank you for reaching out! Your message has been sent successfully."
        )
        
        return redirect("contact")
        
    return render(request, "portfolio/contact.html")

def projects(request):
    return render(request, "portfolio/projects.html")
