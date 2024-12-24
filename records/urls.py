from django.urls import path
from records import views

urlpatterns = [
    # login/logout
    path("login/", views.login_view, name='login_view'),
    path("logout/", views.logout_view, name='logout_view'),
    
    # employeers
    path("funcionario/", views.register_employee, name='register_employee'),
    
    # key
    path('chave/', views.register_key, name='register_key'),
    
    # EPI
    path('epi/', views.register_epi, name='register_epi'),
    
    # alert
    path('success/', views.success_page, name='success_page'),
]
