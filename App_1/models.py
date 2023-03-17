from django.db import models

# Create your models here.


class Person(models.Model):
    Name = models.CharField(max_length= 100)
    LastName = models.CharField(max_length= 100)
    Age =  models.IntegerField()
    MobileNumber = models.IntegerField()
    Address = models.CharField(max_length= 100)

    class Meta:
        db_table = "Person"   # to rename the table 


    def __str__(self):   # get the name in database  
        return f"{self.Name}--{self.LastName}  "

    def show_details(self):
        print(f"""___________________________________________
Name :- {self.Name}
Last Name  :- {self.LastName}
age :- {self.Age}
molbile number :- {self.MobileNumber}
Addresss :- {self.Address}
""")

    @classmethod
    def get_all_data_above_age(cls):
        return cls.objects.filter(Age__gte = 25)

    @classmethod
    def get_avg_age(cls):
        data = cls.objects.all().values("id", "Name", "Age")
        list_age = list(map(lambda x : x["Age"], list(data)))
        return sum(list_age)//len(list_age)



class CommonClass(models.Model): # def commom class for name
    name = models.CharField(max_length=100)   # define name for all objects

    def __str__(self):
        return self.name

    class Meta:
        abstract = True 

class College(CommonClass):
    add = models.CharField(max_length=100)  # def addres for the college
    est_data = models.DateField(auto_now= True)  # def established date of college 

    class Meta:
        db_table = "College"

class Principal(CommonClass):
    exp = models.IntegerField()
    qual = models.CharField(max_length=100)
    college = models.OneToOneField(College, on_delete= models.CASCADE, related_name= "principal")  # here we have set one to one relationship and on_delete if college delete then automatically principle will delete

    class Meta:
        db_table = "Principal"


class Department(CommonClass):
    dept_stringth = models.IntegerField()
    college = models.ForeignKey(College, on_delete= models.CASCADE, related_name="depts")

    class Meta:
        db_table = "Department"



class Student(CommonClass):
    mark = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete= models.CASCADE, related_name="stud", null= True)

    class Meta:
        db_table = "Student"

class Subject(CommonClass):
    is_practical = models.BooleanField(default= False)
    student = models.ManyToManyField(Student, related_name="subjs")
    dept = models.ForeignKey(Department, on_delete= models.CASCADE, related_name= "subjs", null= True)

    class Meta:
        db_table = "Subject"
 

class SubjectStudent(models.Model):
    id = models.BigAutoField(primary_key= True)
    Subject = models.ForeignKey(Subject, models.DO_NOTHING)
    Student = models.ForeignKey(Student, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "subject_student"
        unique_together = (('Subject', 'Student'))



# ____________________________________________________________________________________________


class FuelType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "fueltype"
    
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType, related_name='carmodels')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "carmodel"