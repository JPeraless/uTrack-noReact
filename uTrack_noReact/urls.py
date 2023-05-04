"""
URL configuration for uTrack_noReact project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.urls import re_path
from web_app.views import *

urlpatterns = [
    #HANDLING AUTHORIZATION AND AUTHENTICATION
	path('admin/', admin.site.urls),
	path('api/auth/login/', UserLoginView.as_view()),
	path('api/auth/register/', UserRegistrationView.as_view()),

	# HANDLING GENERAL DATA
	path('api/get_Users/', AllUsersView.as_view()),
	path('api/get_classes/', AllClassesView.as_view()),
	path('api/get_intramurals/', AllIntramuralsView.as_view()),
	path('api/get_equipment/', AllEquipmentView.as_view()),
	path('api/get_facilities/', AllFacilitiesView.as_view()),

	# 
	path('api/Checkins/', CheckInSystemView.as_view()),
	path('api/Checkout/last/<str:tracked_username>/', CheckOutView.as_view()),

	# HANDLING USER-SPECIFIC DATA
	path('api/get_user_classes/<str:username>', UserClassesView.as_view()),
	path('api/get_user_intramurals/<str:tracked_username>', UserIntramuralsView.as_view()),
	path('api/get_user_equipment/<str:username>', UserEquipmentView.as_view()),
	path('api/get_user_facilities/<str:tracked_username>', UserEquipmentView.as_view()),
	path("api/viewer/", OverseerView.as_view())
]
