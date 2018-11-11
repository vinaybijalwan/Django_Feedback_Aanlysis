from django import forms

from .models import patientinfo

DATE_CHOICES = ('2016', '2017', '2018', '2019', '2020' )
DISEASE_CHOICES = (
   ('AVATU GRANTHI VIKAR / THYROID', 'AVATU GRANTHI VIKAR / THYROID'),
    ('AVTUGRANTHI SARVA ALPTA / HYPOTHYROIDISM', 'AVTUGRANTHI SARVA ALPTA / HYPOTHYROIDISM'),
    ('AVTUGRANTHI ATIKRIYASHEELTA/ BHASMAK ROGA/ HYPERTHYROIDISM', 'AVTUGRANTHI ATIKRIYASHEELTA/ BHASMAK ROGA/ HYPERTHYROIDISM'),
)


class patientinfoForm(forms.ModelForm):
    patient_name = forms.TextInput(attrs={'size': 30, 'label': 'Your name'})
    visit_date = forms.DateField(widget=forms.SelectDateWidget(years=DATE_CHOICES))
    Ist_Visit_pyp = forms.DateField(widget=forms.SelectDateWidget(years=DATE_CHOICES))
    disease = forms.CharField(label="Choose Disease",widget=forms.Select(
        choices=DISEASE_CHOICES,
    ))




    class Meta:
        model = patientinfo
        fields = '__all__'