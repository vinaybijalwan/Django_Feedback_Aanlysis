from django.test import TestCase

# Create your tests here.


{{ patient_record.previous }}
        {{ patient_record.number }}
        {{ patient_record.paginator.count }}
        {{ patient_record.paginator.num_page }}
        {{ patient_record.paginator.page_range }}
        {{ patient_record.has_next }}