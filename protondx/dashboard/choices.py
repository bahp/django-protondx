# Gender choices
FEMALE = 'F'
MALE = 'M'
OTHER = 'O'
PREFER_NOT_SAY = 'X'

GENDER = [
    (FEMALE, 'Female'),
    (MALE, 'Male'),
    (OTHER, 'Other'),
    (PREFER_NOT_SAY, 'Prefer not to say'),
]


# Centre type choices
HOSPITAL = 'Hospital'
CLINIC = 'GP clinic'
DRIVE_THROUGH = 'Drive through centre'
HOME_TEST_SITE = 'Home'
OTHER_TEST_SITE = 'Other'

CENTRE_TYPE = [
    (HOSPITAL, 'Hospital'),
    (CLINIC, 'GP clinic'),
    (DRIVE_THROUGH, 'Drive through centre'),
    (HOME_TEST_SITE, 'Home'),
    (OTHER_TEST_SITE, 'Other'),
]


# Test result choices
POS = True
NEG = False

DIAGNOSIS = [
    (POS, 'Positive'),
    (NEG, 'Negative'),
]