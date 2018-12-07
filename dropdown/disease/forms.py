from django import forms
from .models import Diagnosis, patientinfo

class patientinfoForm(forms.ModelForm):

    class Meta:
        model = patientinfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Diagnosis'].queryset = Diagnosis.objects.none()