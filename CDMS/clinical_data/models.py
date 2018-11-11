from django.db import models



class patientinfo(models.Model):
    HIN = models.IntegerField(default=100) #HIN- Hospital Ientiy Number
    patient_name = models.CharField(max_length=50)  # Patient name
    Ist_Visit_pyp = models.DateField(auto_now=False) #Ist Visit Visit
    visit_date = models.DateField(auto_now=False) # patient Visit date
    disease = models.CharField(max_length=200)
    disease_category = models.CharField(max_length=200, default='NA')
    problem_since = models.CharField(max_length=100, default='NA')
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=70, blank=False)
    other_treatment = models.CharField(max_length=50, default='NA')
    doctor_name = models.CharField(max_length=100, default='NA')

    class Meta:
        verbose_name_plural = "patientinfos"

    def __str__(self):
        return str(self.HIN)