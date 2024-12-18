from django.urls import path
from records import views

urlpatterns = [
    # login/logout
    path("login/", views.login_view, name='login_view'),
    path("logout/", views.logout_view, name='logout_view'),
    
    # employeers
    path("funcionario/", views.register_employee, name='register_employee'),
]
