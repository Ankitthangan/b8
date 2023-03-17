from django.shortcuts import render, HttpResponse

# Create your views here.

#Automic Transaction 

# two types of  view 

        # -- function based 
        # -- class based

# def welcome(request):     # request is reserved key word
#     return HttpResponse("welcome django home page..!!")



from .models import Student

# def welcome(request):
#     Stu = Student.objects.get(id=1)
#     return HttpResponse(f"welcome to Django Application {Stu.name}")

# def welcome(request):
#     stud = Student.objects.values("name")
#     lst_stu = list(map(lambda x : x["name"], stud))
#     # print(lst_stu)
#     return HttpResponse(f"welcome to the Django Application {lst_stu}")

# def welcome(request):
#         # print(request.method)   # return get in the terminal
#         # print(request.user)  # return the name of user 
#         Stud = Student.objects.get(id= 1)
#         return HttpResponse(Stud.name)


def welcome(request):
        return render(request, "home.html")