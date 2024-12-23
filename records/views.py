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
        sector = request.POST.get('sector_name')
        phone = request.POST.get('sector_phone')
        enterprise = request.POST.get('enterprise')
        
        if form.is_valid():
            register = form.save(commit=False)
            register.user = request.user
            register.save()
            
        elif enterprise:
            enterprise_nome = models.Enterprise(name=enterprise)
            enterprise_nome.save()
                
        elif sector and phone:
            sector_data = models.Sector(name=sector, phone=phone)
            sector_data.save()
                
        return redirect('register_employee')
    form = forms.EmployeeForm()
    return render(request, 'pages/employee/employee_create.html', {'form': form})
            
