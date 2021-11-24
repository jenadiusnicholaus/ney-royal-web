from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth import login as user_login, authenticate, logout  # add this
from django.contrib import messages


# Create your views here.
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
