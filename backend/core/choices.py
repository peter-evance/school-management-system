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
    SSS_4 = "SSS 1"
    SSS_5 = "SSS 2"
    SSS_6 = "SSS 3"