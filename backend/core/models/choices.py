from django.db import models


class ClassRoomStreamChoices(models.TextChoices):
    A = "A"
    B = "B"
    C = "C"
    D = "D"

class ClassRoomTitleChoices(models.TextChoices):
    CLASS1 = "JUNIOR SECONDARY 1"
    CLASS2 = "JUNIOR SECONDARY 2"
    CLASS3 = "JUNIOR SECONDARY 3"
    CLASS4 = "SENIOR SECONDARY SCHOOL 1"
    CLASS5 = "SENIOR SECONDARY SCHOOL 2"
    CLASS6 = "SENIOR SECONDARY SCHOOL 3"

class ClassRoomCodeChoices(models.TextChoices):
    CLASS_CODE1 = "JSS 1"
    CLASS_CODE2 = "JSS 2"
    CLASS_CODE3 = "JSS 3"
    CLASS_CODE4 = "SSS 1"
    CLASS_CODE5 = "SSS 2"
    CLASS_CODE6 = "SSS 3"