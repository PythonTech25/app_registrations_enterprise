from django.shortcuts import render, redirect
from records import forms, models
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('register_employee')
    
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
    context = {'form': form}
    return render(request, 'pages/employee/employee_create.html', context=context)

def register_key(request):
    if request.method == 'POST':
        form = forms.KeyForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.user = request.user
            register.save()
            
        return redirect('register_key')
    
    form = forms.KeyForm()
    context = {'form': form}
    return render(request, 'pages/key/key_create.html', context=context)


def register_epi(request):
    if request.method == 'POST':
        form = forms.EPIForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.user = request.user
            register.save()
            messages.success(request, 'Epi cadastrado com sucesso!')
            
        return redirect('register_epi')
    
    form = forms.EPIForm()
    context = {'form': form}
    return render(request, 'pages/epi/epi_create.html', context=context)


def success_page(request):
    return render(request, 'pages/alert/success.html')
            
