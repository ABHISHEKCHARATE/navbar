
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from .form import SignupForm, LoginForm  # Ensure you import forms correctly
from loginsystem.ml_text_summary import extract_text_from_pdf, generate_summary

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)  # Log the user in after successful signup
                return redirect('dashboards')  # Redirect to dashboards
            except Exception as e:
                return HttpResponse(f"Error saving user: {str(e)}")
        else:
            # Display detailed form errors
            errors = form.errors.as_json()
            return HttpResponse(f"Form is not valid. Please ensure all fields are correctly filled. Errors: {errors}")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff or user.is_superuser:
                    return HttpResponse("Admin users cannot log in from here.")
                login(request, user)
                return redirect('dashboards')  # Redirect to dashboards
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def dashboards(request):
    return render(request, 'dashboards.html')


def text_summary(request):
    if request.method == "POST":
        input_type = request.POST.get('inputType')
        if input_type == "pdf":
            pdf_file = request.FILES.get('pdfFile')
            if not pdf_file:
                return render(request, 'text_summary.html', {'error': 'Please select a PDF file.'})
            pdf_text = extract_text_from_pdf(pdf_file)
            string_data = pdf_text
        else:
            text_input = request.POST.get('textInput')
            if text_input is None or not text_input.strip():
                return render(request, 'text_summary.html', {'error': 'Please enter text.'})
            string_data = text_input
        summary = generate_summary(string_data)  # Moved the summary generation inside the else block

        # Render summary.html with string_data and summary
        return render(request, 'summary.html', {'string_data': string_data, 'summary': summary})
    else:
        return render(request, 'text_summary.html')



def summary(request):
    if request.method == "POST":
        string_data = request.POST.get('string_data')
        if string_data:
            summary = generate_summary(string_data)
            return render(request, 'summary.html', {'string_data': string_data, 'summary': summary})
        else:
            return render(request, 'summary.html', {'error': 'No string data provided.'})
    else:
        return render(request, 'summary.html', {'error': 'No POST data received.'})







