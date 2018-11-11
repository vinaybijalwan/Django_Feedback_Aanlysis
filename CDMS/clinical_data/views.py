from django.shortcuts import render, redirect
from .models import patientinfo
from .forms import patientinfoForm
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.

def homePageView(request):
    #patient_record = patientinfo.objects.all()
    return render(request, 'clinical_data/index.html')



def PatientListView(request):
    patient_record = patientinfo.objects.all()
    #paginator = Paginator(patientinfo, 8)
    #page = request.GET.get('page')

    #patient_record = paginator.get_page(page)

    return render(request, 'clinical_data/table.html', {'patient_record': patient_record})




def pat_new(request):

    if request.method == "POST":
        form = patientinfoForm(request.POST)
        if form.is_valid():

            patientinfo = form.save(commit=False)
            patientinfo.save()
            return redirect('home')
    else:
        form = patientinfoForm()

    return render(request, 'clinical_data/pat_new.html', {'form': form})



def patient_edit(request, pk):
    patient = get_object_or_404(patientinfo, pk=pk)
    if request.method == "POST":
        form = patientinfoForm(request.POST, isinstance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('home')
    else:
        form = patientinfoForm(instance=patient)
    return render(request, 'clinical_data/table.html', {'form': form})