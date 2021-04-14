from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect

from accounts.models import User


def user_sign_in(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'accounts/user-login.html', d)


def sign_out(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('home')


def user_register(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        email_address = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        try:
            if password == confirm_password:
                user = User.objects.create_user(username=username, email=email_address, first_name=first_name,
                                                last_name=last_name, password=password)
                user.save()
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    p = {'error': error}
    return render(request, 'accounts/user-signup.html', p)
