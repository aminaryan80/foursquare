from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from account.models import Account


def get_register_template(request, error_str):
    return render(request, 'register.html', context={'error': error_str})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            return get_register_template(request, 'password and confirm password are different!')

        if User.objects.filter(username=username).exists():
            return get_register_template(request, 'username taken')
        else:
            user = User.objects.create_user(username=username, password=password)

            account = Account.objects.create(user=user)
            account.save()

            return redirect('login')
    else:
        return render(request, 'register.html', context={'error': "None"})


def index(request):
    context = {
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username,
    }

    return render(request, 'index.html', context=context)
