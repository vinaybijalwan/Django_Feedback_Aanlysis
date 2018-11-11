from django.urls import path

from . import views


urlpatterns = [
    path('', views.homePageView, name='home'),
    path('PatientListView', views.PatientListView, name='PatientListView'),
    path('pat/new', views.pat_new, name='pat_new'),
    path('patient_edit', views.patient_edit, name='patient_edit'),
    #path('thyroid', views.thyroid, name='thyroid'),



]