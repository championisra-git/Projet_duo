"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WEmanager import views  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('releve/', views.enregistrement_relevé, name='relevé'),
    path('abonne/', views.enregistrement_abonne, name="abonné"),
    path('facture/', views.enregistrement_facture, name="facture"), 
    path('paiement/', views.enregistrement_paiement, name="paiement"),
    path('login/', views.login_view, name='login'),         
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),  

]
