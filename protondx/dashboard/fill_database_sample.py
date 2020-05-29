from dashboard.models import *
from django.contrib.gis.geos import Point
import datetime
import random


def new_patient(first_name, last_name, gender, dob_day, dob_month, dob_year, postcode):
    date = datetime.date(dob_year, dob_month, dob_day)
    entry = Patient(first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    postcode=postcode,
                    dob=date)
    entry.save()


def new_centre(centre_type, postcode, lat, long):
    point = Point(long, lat)
    entry = TestingCentre(centre_type=centre_type,
                          postcode=postcode,
                          coordinates=point)
    entry.save()


def new_diagnostic(test_date, test_result, centre_ID, patient_ID):
    # example date time "2020-0 15:26"
    date = datetime.datetime.strptime(test_date, "%Y-%m-%d %H:%M")
    entry = DiagnosticTest(date_test=date,
                           test_result=test_result,
                           testing_centre=centre_ID,
                           patient=patient_ID)
    entry.save()


def create_entries(num):
    new_patient("John", "Doe", "M", 1, 1, 1990, "W8 5JJ")
    new_patient("John", "Smith", "M", 1, 1, 1990, "SW7 1AW")
    new_patient("Jane", "Doe", "F", 1, 1, 1990, "W8 5JJ")
    new_patient("Elizabeth", "Windsor", "F", 21, 4, 1926, "SW1A 1AA")

    new_centre("Home", "W8 5JJ", 51.49579622093249, -0.1896153101237956)
    new_centre("Home", "SW1A 1AA", 51.501089612989176, -0.14222818642555113)
    new_centre("Hospital", "SW5 0TU", 51.49415610172322, -0.19134750351409544)
    new_centre("Drive through centre", "WD4 8LZ", 51.707485, -0.440311)
    new_centre("Other", "HP20 1PQ", 51.816230, -0.800203)
    new_centre("Hospital", "EH3 9HQ", 55.944739, -3.197911)
    new_centre("Other", "EH1 2NG", 55.948478, -3.199903)
    new_centre("GP clinic", "EH30 9RB", 55.990914, -3.398235)
    new_centre("Drive through centre", "M2 3JL", 53.479033, -2.241551)
    new_centre("GP clinic", "M15 6BH", 53.470539, -2.239421)
    new_centre("Hospital", "G3 8SJ", 55.867440, -4.297762)
    new_centre("Drive through centre", "G51 4TF", 55.863467, -4.340535)

    # Create Diagnostic test entries

    centre_ids = list(TestingCentre.objects.values_list('id', flat=True))
    patient_ids = list(Patient.objects.values_list('id', flat=True))

    start_dt = datetime.date.today().replace(day=1, month=1).toordinal()
    end_dt = datetime.date.today().toordinal()

    for i in range(num):
        random_day = datetime.date.fromordinal(random.randint(start_dt, end_dt))
        random_time = str(random_day) + " 00:00"

        random_result = False if random.random() < 0.8 else True

        random_centre = random.choice(centre_ids)
        random_patient = random.choice(patient_ids)

        new_diagnostic(random_time, random_result, TestingCentre(random_centre), Patient(random_patient))
