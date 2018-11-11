# Generated by Django 2.1.3 on 2018-11-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patientinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HIN', models.IntegerField(default=100)),
                ('patient_name', models.CharField(max_length=50)),
                ('Ist_Visit_pyp', models.DateField()),
                ('visit_date', models.DateField()),
                ('disease', models.CharField(max_length=200)),
                ('disease_category', models.CharField(default='NA', max_length=200)),
                ('problem_since', models.CharField(default='NA', max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('other_treatment', models.CharField(default='NA', max_length=50)),
                ('doctor_name', models.CharField(default='NA', max_length=100)),
            ],
        ),
    ]
