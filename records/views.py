from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'pages/login/login.html')


def logout_view(request):
    return render(request, 'pages/login/logout.html')
