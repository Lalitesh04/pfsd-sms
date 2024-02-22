from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Admin, Student, Course, Faculty


# Create your views here.

def adminhome(request):
    return render(request, "AdminHome.html")


def logout(request):
    return render(request, "Login.html")


def checkadminlogin(request):
    admin_name = request.POST["uname"]
    admin_password = request.POST["pwd"]
    admin = Admin.objects.filter(Q(username=admin_name) & Q(password=admin_password))

    if admin:
        return render(request, "AdminHome.html")
    else:
        return HttpResponse("Login Failed")


def viewstudents(request):
    students = Student.objects.all()
    count = Student.objects.count()
    return render(request, "viewstudents.html", {"studentdata": students, "count": count})


def viewfaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "viewfaculty.html", {"facultydata": faculty, "count": count})


def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "viewcourses.html", {"coursesdata": courses, "count": count})


def adminstudent(request):
    return render(request, "adminstudent.html")


def adminfaculty(request):
    return render(request, "adminfaculty.html")


def admincourse(request):
    return render(request, "admincourse.html")


def addcourses(request):
    return render(request, "addcourse.html")


def addstudent(request):
    return render(request, "addstudent.html")


def addfaculty(request):
    return render(request, "addfaculty.html")


def insertcourse(request):
    if request.method == "POST":
        dept = request.POST["dept"]
        ay = request.POST["ay"]
        sem = request.POST["sem"]
        year = request.POST["year"]
        ccode = request.POST["ccode"]
        ctitle = request.POST["ctitle"]
        course = Course(department=dept, academicyear=ay, semester=sem, year=year, coursecode=ccode, coursetitle=ctitle)
        Course.save(course)
        message = "Course Added SuccessFully!"
        return render(request, "addcourse.html", {"message": message})

    return HttpResponse("Not Added")


def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "deletecourse.html", {"courses": courses, "count": count})


def insertfaculty(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
        gender = request.POST["gender"]
        dept = request.POST["dept"]
        qualification = request.POST["qualification"]
        designation = request.POST["designation"]
        email = request.POST["email"]
        contact = request.POST["contact"]

        faculty = Faculty(facultyid=id, fullname=name, gender=gender, department=dept, qualification=qualification,
                          designation=designation, email=email, contact=contact)
        Faculty.save(faculty)
        message = "Faculty Added SuccessFully"
        return render(request, "addfaculty.html", {"message": message})


def coursedeletion(request, cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")
