"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from system import views

urlpatterns = [
    path('patients/',
         views.UserViewAllPatients.as_view(),
         name='all-patients'),
    path('visits/',
         views.UserViewAllVisits.as_view(),
         name='all-visits'),
    path('locations/',
         views.UserViewAllLocations.as_view(),
         name='all-locations'),
    # path('create_patient/',
    #      views.UserCreateOnePatient.as_view(),
    #      name='create-patient'),
    path('create_patient/',
         views.UserCreateOnePatient.as_view(),
         name='create-patient'),
    path('create_location/',
         views.UserCreateOneLocation.as_view(),
         name='create-location'),
    path('create_visit/',
         views.UserCreateOneVisit.as_view(),
         name='create-visit'),
    path('view/<int:caseID>',
         views.UserViewOnePatient.as_view(),
         name='selected-patient'),
]
