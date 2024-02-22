from django.db import models


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department_choice = (("Cse(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=20, blank=False, choices=department_choice)
    academic_choice = (("2022-23", "2022-23"), ("2023-24", "2023-24"), ("2024-25", "2024-25"))
    academicyear = models.CharField(max_length=20, blank=False, choices=academic_choice)
    semester_choice = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False, choices=semester_choice)
    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False, unique=True)
    coursetitle = models.CharField(max_length=25, blank=False)

    class Meta:
        db_table = "course_table"

    def __str__(self):
        return self.coursetitle


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=25, blank=False)
    gender_choice = (("MALE", "MALE"), ("FEMALE", "FEMALE "))
    gender = models.CharField(max_length=10, blank=False, choices=gender_choice)

    department_choice = (("Cse(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=50, blank=False, choices=department_choice)

    program_choice = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False, choices=program_choice)

    semester_choice = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False, choices=semester_choice)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=10, blank=False, default="klu123")
    email = models.CharField(max_length=50, blank=False, unique=True)
    contact = models.CharField(max_length=10, blank=False, unique=True)

    class Meta:
        db_table = "student_table"

    def __str__(self):
        return str(self.studentid)


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid = models.CharField(max_length=10, blank=False, unique=True)
    fullname = models.CharField(max_length=25, blank=False)

    gender_choice = (("MALE", "MALE"), ("FEMALE", "FEMALE "))
    gender = models.CharField(max_length=10, blank=False, choices=gender_choice)
    department_choice = (("Cse(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=50, blank=False, choices=department_choice)
    qualification_choice = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"), ("ph.D", "ph.D"))
    qualification = models.CharField(max_length=50, blank=False, choices=qualification_choice)
    designation_choice = (("Prof.", "professor"),
                          ("Assoc . prof.", "Associate Professor"),
                          ("Asst . prof.", "Assistant professor"))

    designation = models.CharField(max_length=50, blank=False, choices=designation_choice)
    password = models.CharField(max_length=10, blank=False, default="klu123")
    email = models.CharField(max_length=50, blank=False, unique=True)
    contact = models.CharField(max_length=11, blank=False, unique=True)

    class Meta:
        db_table = "faculty_table"

    def __str__(self):
        return self.facultyid
