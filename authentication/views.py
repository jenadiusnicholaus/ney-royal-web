from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UsernameField  # add this
from django.contrib.auth import login as user_login, authenticate, logout  # add this
from django.contrib import messages
from authentication.frorms import NewUserForm


# Create your views here.
def user_register(request):
    # try:
    form = NewUserForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')

        # cheking for passwords matching
        if password1 != password2:
            messages.warning(request, "password doesn't match")
            # For this we need toredirect to register page if there
            return redirect('/')

        if not (User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists()):
            User.objects.create_user(
                username, email, password=password1, is_active=True)
            user = User.objects.get(username=username)
            # TODO send email address to activate a user if you want it to
            messages.success(
                request, f'Registered successfully now')
            return redirect('/')
        else:
            messages.warning(
                request, 'Looks like a username with that email or password already exists')
            return redirect("/")
    else:
        # For this we need toredirect to register page if there
        print('from not valid')
        print(form.data)
        messages.warning(request, 'Form not valid')
    return redirect('/')
    # except:
    #     return render(request, "/")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                user_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:

                messages.error(request, "Invalid username or password.")
                return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return redirect("/")


def user_logout(request):
    logout(request)
    messages.success(request, "You loged out.")

    return redirect('/')
