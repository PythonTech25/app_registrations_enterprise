from django.shortcuts import render, redirect
from records import forms, models

# Create your views here.
def login_view(request):
    return render(request, 'pages/login/login.html')


def logout_view(request):
    return render(request, 'pages/login/logout.html')


def register_employee(request):
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.user = request.user
            register.save()
            
            enterprise = request.POST.get('enterprise')
            if enterprise:
                enterprise_nome = models.Enterprise(name=enterprise)
                enterprise_nome.save()
                
            return redirect('register_employee')
    form = forms.EmployeeForm()
    return render(request, 'pages/employee/employee_create.html', {'form': form})
            
