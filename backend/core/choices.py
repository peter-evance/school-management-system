from django.db import models


class ClassRoomStreamChoices(models.TextChoices):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class ClassRoomTitleChoices(models.TextChoices):
    JUNIOR_SECONDARY_SCHOOL_1 = "JUNIOR SECONDARY SCHOOL 1"
    JUNIOR_SECONDARY_SCHOOL_2 = "JUNIOR SECONDARY SCHOOL 2"
    JUNIOR_SECONDARY_SCHOOL_3 = "JUNIOR SECONDARY SCHOOL 3"
    SENIOR_SECONDARY_SCHOOL_1 = "SENIOR SECONDARY SCHOOL 1"
    SENIOR_SECONDARY_SCHOOL_2 = "SENIOR SECONDARY SCHOOL 2"
    SENIOR_SECONDARY_SCHOOL_3 = "SENIOR SECONDARY SCHOOL 3"


class ClassRoomCodeChoices(models.TextChoices):
    JSS_1 = "JSS 1"
    JSS_2 = "JSS 2"
    JSS_3 = "JSS 3"
    SSS_1 = "SSS 1"
    SSS_2 = "SSS 2"
    SSS_3 = "SSS 3"


class SubjectTitleChoices(models.TextChoices):
    ENGLISH_LANGUAGE = "ENGLISH LANGUAGE"
    MATHEMATICS = "MATHEMATICS"
    AGRICULTURAL_SCIENCE = "AGRICULTURAL SCIENCE"
    BIOLOGY = "BIOLOGY"
    ECONOMICS = "ECONOMICS"
    CIVIC_EDUCATION = "CIVIC EDUCATION"
    FRENCH = "FRENCH LANGUAGE"
    FURTHER_MATHEMATICS = "FURTHER MATHEMATICS"
    CHEMISTRY = "CHEMISTRY"
    PHYSICS = "PHYSICS"
    GEOGRAPHY = "GEOGRAPHY"
    COMPUTER_SCIENCE = "COMPUTER SCIENCE"
    SOCIAL_STUDIES = "SOCIAL STUDIES"
    MUSIC = "MUSIC"
    GOVERNMENT = "GOVERNMENT"
    COMMERCE = "COMMERCE"


class SubjectCodeChoices(models.TextChoices):
    ENG = "ENG"
    MTH = "MTH"
    AGS = "AGS"
    BIO = "BIO"
    ECONS = "ECONS"
    CVE = "CVE"
    FRN = "FRN"
    FMTH = "FMTH"
    CHM = "CHM"
    PHY = "PHY"
    GEO = "GEO"
    CPS = "CPS"
    SOS = "SOS"
    MUSIC = "MUSIC"
    GOV = "GOV"
    COMMERCE = "COMMERCE"


class ExamType(models.TextChoices):
    MIDTERM = "Mid Term"
    FINAL = "Final Exam"
    QUIZ = "Quiz"
