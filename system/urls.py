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
    # view records
    path('view_patients/',
         views.UserViewAllPatients.as_view(),
         name='view-patients'),
    path('view_visits/',
         views.UserViewAllVisits.as_view(),
         name='view-visits'),
    path('view_locations/',
         views.UserViewAllLocations.as_view(),
         name='view-locations'),
    path('view_details/<int:pk>',
         views.UserViewOnePatient.as_view(),
         name='selected-patient'),
    # create records
    path('create_patient/',
         views.UserCreateOnePatient.as_view(),
         name='create-patient'),
    path('create_location/',
         views.UserCreateOneLocation.as_view(),
         name='create-location'),
    path('create_visit/',
         views.UserCreateOneVisit.as_view(),
         name='create-visit'),
    # update records
    path('update_patient/<int:pk>',
         views.UserUpdateOnePatient.as_view(),
         name='update-patient'),
    path('update_location/<int:pk>',
         views.UserUpdateOneLocation.as_view(),
         name='update-location'),
    path('update_visit/<int:pk>',
         views.UserUpdateOneVisit.as_view(),
         name='update-visit'),
    # delete records
    path('delete_patient/<int:pk>',
         views.UserDeleteOnePatient.as_view(),
         name='delete-patient'),
    path('delete_location/<int:pk>',
         views.UserDeleteOneLocation.as_view(),
         name='delete-location'),
    path('delete_visit/<int:pk>',
         views.UserDeleteOneVisit.as_view(),
         name='delete-visit'),
    # search connections
    path('search_connections/',
         views.UserSearchConnections.as_view(),
         name='search-connections'),
    #path('identify_connection/<int:pk>',
    #     views.ConnectionIdentify.as_view(),
    #     name='identify-connection'),
]
