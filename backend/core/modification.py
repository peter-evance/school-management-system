
"""
core > models.py
"""
def generate_registration_number(self):
    registration_number = self.created.strftime("%m%d-%Y-%H%M%S") + str(self.id)
    return registration_number[::-1]
"""
The attribute/method above generate student registration number
self.created was used along with the self.id to generate a unique number for a new registered student


suggested student fields
grade = models.CharField(max_length=10, blank=True, null=True)
attendance = as foreignKey


"""
"""
"""
