
"""
core > models.py
"""
def registration_number(self):
    registration_number = self.created.strftime("%m%d-%Y-%H%M%S") + str(self.id)
    return registration_number[::-1]
"""
The attribute/method above generate student registration number
self.created was used along with the self.id to generate a unique number for a new registered student


suggested student fields
grade = models.CharField(max_length=10, blank=True, null=True)
attendance = as foreignKey


"""
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


"""
models
"""
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    """
        Many-to-many relationship with subject object
        This assumes that a teacher can be associated with multiple subjects, 
        and each subject can have multiple teachers.
    """
    assigned_subjects = models.ManyToManyField(Subject, related_name='teachers')

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    """
        Many-to-many relationship with subject object
        This assumes that each student can be enrolled in multiple subjects, 
        and each subject can have multiple enrolled students.
    """
    enrolled_subjects = models.ManyToManyField(Subject, related_name='enrolled_students')
    
    @property
    def registration_number(self):
        registration_number = self.created.strftime("%m%d-%Y-%H%M%S") + str(self.id)
        return registration_number[::-1]

class Subject(models.Model):
    title = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    max_marks = models.PositiveIntegerField(default=100)
    min_mark = models.PositiveIntegerField(default=40)
    mark_obtained = models.PositiveIntegerField(default=0, null=True)
    grade = models.CharField(max_length=10, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def grading_system(self):
        """
        Calculate and set the grade based on the value of mark_obtained.
        """
        if not self.mark_obtained:
            return

        if self.mark_obtained >= 90:
            self.grade = 'A+'
        elif 70 <= self.mark_obtained < 90:
            self.grade = 'A'
        elif 60 <= self.mark_obtained < 70:
            # self.mark_obtained is between 60-69
            self.grade = 'B'
        elif 50 <= self.mark_obtained < 60:
            # self.mark_obtained is between 50-59
            self.grade = 'C'
        elif 40 <= self.mark_obtained < 50:
            # self.mark_obtained is between 40-59
            self.grade = 'D'
        else:
            # self.mark_obtained is less than 40
            self.grade = 'FAILED'

    def save(self, *args, **kwargs):
        self.grading_system()
        super().save(*args, **kwargs)
