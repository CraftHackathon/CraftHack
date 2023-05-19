"""vigil_ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import scam_detection_view
from django.urls import path
from .views import email_addresses, post_email, report , getPrediction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getPrediction/', getPrediction),
    path('report/', report),
    path('getPrediction/', scam_detection_view),    
    path('email-addresses/', email_addresses),
    path('email-populate/', post_email),
]
