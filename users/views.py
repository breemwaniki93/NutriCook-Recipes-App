from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms

# User Registration View
def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        
        if form.is_valid():
            # Retrieve cleaned data from the form
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            # Create a new user in the database
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Display a success message
            messages.success(request, f"Account created for {username}! You can now log in.")
            
            # Redirect to the login page after successful registration
            return redirect('user-login')
        else:
            # If the form is invalid, show an error message
            messages.error(request, "There was an error in the form. Please try again.")
    else:
        # Handle GET request: show the empty registration form
        form = forms.UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

# User Profile View (Authenticated Users Only)
@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'users/profile.html', {'user': user})

# View for Privacy Policy page
def privacy_policy(request):
    return render(request, 'users/privacy_policy.html')

# View for Terms of Service page
def terms_of_service(request):
    return render(request, 'users/terms_of_service.html')

# View for FAQ page
def faqs(request):
    return render(request, 'users/faqs.html')
