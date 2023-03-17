from App_1.models import Person

from App_1.models import *

# exec(open(r'D:\ankit_python\class_files\project_Django\First_project\App_1\db_shell.py').read())

# objs  = Person.objects.all()
# print(objs)

# for person in objs:
#     # print(person)
#     print(person.__dict__)

# obj = Person.objects.first()   # return the all the object from person table 
# print(obj)


"""get the data of passed id"""

# obj = Person.objects.all() .get(id= 4) # return the data of passed id
# print(obj)  # Return data for passed id, as Harshal--Kawalkar  nitin-- kawalkar
# "other way"
# obj = Person.objects.get(Age= 24, Name__startswith = "A")
# print(obj)  # return --> Ajinkya--Burande, for pased condition
# print(obj.__dict__)   #{'_state': <django.db.models.base.ModelState object at 0x000001EBB3DF77C0>, 'id': 3, 'Name': 'Ajinkya', 'LastName': 'Burande', 'Age': 24, 'MobileNumber': 7865456798, 'Address': 'Nagpur'}



"""get the multiple data by passing filename"""

# objs = Person.objects.filter(Age__gte= 23)  # __gte :- grater than or equak to
# print(objs)

"""modify existing data"""

# obj = Person.objects.get(id = 3)
# print(obj.__dict__)    # get  the dictionary of privious data 
# obj.Name = "Ajinkyaaa"  # Updating name of persion 
# print(obj.__dict__)  # printing dictionary to verify
# obj.save()  # if we did not save here then the changes wont be reflect in database



"""delete any existing persion"""

# p1 = Person.objects.get(id = 1)
# print(p1.__dict__)

# p1.delete()  # here we have delete this data from the database, no need to save after delete

"""bulk create"""

# p1 = Person(Name= "A1", LastName = "l1", Age= 56, MobileNumber= 1233478654, Address = "Channei")
# p2 = Person(Name = "A2", LastName= "L2", Age= 34, MobileNumber= 5674234567, Address= "Wkad")
# p3 = Person(Name = "A3", LastName = "L3", Age= 45, MobileNumber= 3456788789, Address= "Viman nagar")

# list_person = [p1, p2, p3]
# Person.objects.bulk_create(list_person)

# print(Person.objects.count())  



"""to delete all record"""

# Person.objects.all().delete()


"""to delete multiple record"""

# Person.objects.filter(Age = 56).delete()  # here we have succesfully delete data from database

# Person.objects.get(id = 2).show_details()


# print(Person.objects.filter(Name__startswith = "A"))
# print(Person.objects.filter(LastName__endswith = "A"))

# print(Person.objects.filter(Name= "Ajinkyaaa").exists())

# for person in Person.objects.all():
#     person.show_details()              # get the details of all the person


# print(Person.get_avg_age())   







"""one to one """
# clg = College.objects.all() # willl return in the from of query set
# print(clg)   # <QuerySet [<College: D Y Patil>, <College: YCC Nagpur>]> 


# for clg_name in clg:
#     print(clg_name)  # return the name of college from query set of collge
#                         # D Y Patil
#                         # YCC Nagpur





# print(clg[0].principal)  # Arun, get the name of principal
# print(clg[1].principal) # Nirmala, get the name of principal 

# for i in range(len(clg)):
#     print(clg[i].principal)    # rerturn the name of principal
#                             # Arun
#                             # Nirmala



"""one to many """

# clgs = College.objects.all()
# clg = clgs[0]

# print(dir(clg))

# depts = clg.department_set.all()
# # print(depts)  #<QuerySet [<Department: Mechanical>, <Department: EE>, <Department: Civil>]>

# for dept in depts:
#     print(dept)   # return the name of department
#                     # Mechanical
#                     # EE
#                     # Civil



# dept = Department.objects.first()
# print(dept)  # return  the first department of college , mechanical
# print(dept.college)  # return the name of college, D Y Patil



# dept = Department.objects.first()
# print(dept.student_set.all())

# stu = Student.objects.all()
# for stud in stu:
#     print(f"name of student :- {stud} -- name of deparatment {stud.dept.name}")

#                 # name of student :- Gulshan -- name of deparatment EE
#                 # name of student :- Apurva -- name of deparatment EE
#                 # name of student :- Pralay -- name of deparatment Civil
#                 # name of student :- Sachin -- name of deparatment Civil
#                 # name of student :- Sanjay -- name of deparatment Mechanical
#                 # name of student :- Sunil -- name of deparatment Mechanical




"""fetcing value with the related name"""

# clg = College.objects.all()
# print(clg[0].principal)
# print(clg[0].depts.all())


# print(clg[0].depts.all()[1].stud.all())






"""adding data"""

# College.objects.create(name= "MIT", add= "Pune")
c1 = College.objects.get(id= 3)
# print(c1)
# Principal.objects.create(name= "abc", exp="23", qual="phd", college = c1)

# p1 = Principal(name= "abc", exp= "34", qual= "phd", college= College.objects.get(id= 3))
# p1.save()

# p2 = Principal(name= "xyz", exp= "45", qual= "phd", college_id= 3)
# p2.save()


# s1 = Student.objects.create(name= "a",mark= 76, age = 56)
# s2 = Student.objects.create(name= "b", mark= 90, age= 34)

# c1 = College.objects.get(id=1)
# d1 = Department.objects.create(name= "Production", dept_stringth= 67, college= c1)



# stud = Student.objects.filter(id__gte= 7, id__lte= 17)
# print(stud)


# lst = []
# for student in stud:
    # lst.append(student.id)
# print(lst)

# for student in stud:
#     dept = Department.objects.get(id = 7)
#     dept.stud.add(student)



# ------------------------------------------------------------------------------------------------

# select_related

# studs = Student.objects.select_related("dept")
# for stud in studs:
#     print(f"Name of Student :- {stud.name}  department :- {stud.dept.name}")



# dept = Department.objects.select_related("college")

# for dep in dept:
#     print(f"name of depatrment :- {dep}  name of college :- {dep.college.name}")



# for dep in dept:
#     print(f"name of College {dep.college.name} name of proncipal :- {dep.college.principal.name}\
#         qualification of principal :- {dep.college.principal.qual}")

#             # name of College D Y Patil name of proncipal :- Arun
#             # name of College D Y Patil name of proncipal :- Arun
#             # name of College D Y Patil name of proncipal :- Arun        qualification of principal :- PHD
#             # name of College D Y Patil name of proncipal :- Arun        qualification of principal :- PHD
#             # name of College D Y Patil name of proncipal :- Arun        qualification of principal :- PHD
#             # name of College D Y Patil name of proncipal :- Arun        qualification of principal :- PHD
#             # name of College D Y Patil name of proncipal :- Arun        qualification of principal :- PHD
#             # name of College D Y Patil name of proncipal :- Arun        qualification of principal :- PHD
#             # name of College YCC Nagpur name of proncipal :- Nirmala        qualification of principal :- PHD
#             # name of College YCC Nagpur name of proncipal :- Nirmala        qualification of principal :- PHD
#             # name of College YCC Nagpur name of proncipal :- Nirmala        qualification of principal :- PHD






# --------------------------------------------------------------------------------------------------------

"creating car models"

# dzire = CarModel.objects.create(name= "Dzire")
# fortuner = CarModel.objects.create(name= "Fortuner")
# i20 = CarModel.objects.create(name="I20")
# eon = CarModel.objects.create(name= "Eon")

"adding fuel type"

# gas = FuelType.objects.create(name= "Gas")
# diesel = FuelType.objects.create(name= "Diesel")
# hybrid = FuelType.objects.create(name= "Hybrid")
# petrol = FuelType.objects.create(name= "Petrol")

"""now we will associate the car model with fuel type"""

# car = CarModel.objects.get(name = "Eon")
# ftype = FuelType.objects.get(name= "Gas")
# car.fueltype.add(ftype)


# car = CarModel.objects.get(name= "Dzire")
# ftype = FuelType.objects.get(name= "Petrol")
# car.fueltype.add(ftype)


"ectract the fuel type to add in car models"

fgas = FuelType.objects.get(name= "Gas")
fdiesel = FuelType.objects.get(name = "Diesel")
fhybrid = FuelType.objects.get(name= "Hybrid")
fpetrol = FuelType.objects.get(name= "Petrol")


"extract car models to add fuel type in it"
car_1 = CarModel.objects.get(name= "dzire")
car_2 = CarModel.objects.get(name= "Fortuner")
car_3 = CarModel.objects.get(name= "I20")
car_4 = CarModel.objects.get(name= "Eon")

"here i have add multiple fuel type for car in single step"
# car_1.fueltype.add(fgas, fpetrol)
# car_2.fueltype.add(fhybrid, fpetrol, fdiesel)
# car_3.fueltype.add(fpetrol, fhybrid)
# car_4.fueltype.add(fgas, fpetrol)


"get the fuel type of for the car"
# print(car_1.fueltype.all())
# print(car_2.fueltype.all())
# print(car_3.fueltype.all())
# print(car_4.fueltype.all())

#                 # <QuerySet [<FuelType: Gas>, <FuelType: Petrol>]>
#                 # <QuerySet [<FuelType: Diesel>, <FuelType: Hybrid>, <FuelType: Petrol>]>
#                 # <QuerySet [<FuelType: Hybrid>, <FuelType: Petrol>]>
#                 # <QuerySet [<FuelType: Gas>, <FuelType: Petrol>]>


"""create and add fuel type in car model in single step"""

# car_2.fueltype.create(name= "Bio Diesel")
# print(car_2.fueltype.all())



"""get the car models associate with the fuel type 
using many 2 many relationship in backword direction"""

# print(fgas.carmodels.all())
# print(fdiesel.carmodels.all())
# print(fpetrol.carmodels.all())
# print(fhybrid.carmodels.all())

#             # <QuerySet [<CarModel: Eon>, <CarModel: Dzire>]>
#             # <QuerySet [<CarModel: Fortuner>]>
#             # <QuerySet [<CarModel: Dzire>, <CarModel: Fortuner>, <CarModel: I20>, <CarModel: Eon>]>
#             # <QuerySet [<CarModel: Fortuner>, <CarModel: I20>]>



"""Filtering records using m2m relationship"""


# cmodel = CarModel.objects.filter(fueltype__name= "Gas")
# for model in cmodel:
#     print(model)

# cmodel = CarModel.objects.filter(fueltype__name__startswith = "G")
# # print(cmodel)
# for model in cmodel:
#     print(f"fuel type name startswith :- G  -- car model :- {model}")


# ftype = FuelType.objects.filter(carmodels__name = "Dzire")
# print(ftype)



# ftype = FuelType.objects.filter(carmodels__name__startswith = "F")
# print(ftype)  #<QuerySet [<FuelType: Diesel>, <FuelType: Hybrid>, <FuelType: Petrol>, <FuelType: Bio Diesel>, <FuelType: Bio Diesel>]>





# stu_subj = Subject.objects.filter(student__name = "Gulshan")
# print(stu_subj)  # <QuerySet [<Subject: PSE>]>

# print(Subject.objects.filter(student__name__startswith = "S"))  #<QuerySet [<Subject: DOM>, <Subject: DOM>, <Subject: SOM>]>




# ______________________________________________________________________________________________________________


"""Row SQL query"""

# First way   :- 


# from django.db import connection
# cursor = connection.cursor()
# cursor.execute("select * from student")
# data = cursor.fetchall()
# print(data)


# second way :-  

# data = Student.objects.raw("SELECT * FROM student;")
# print(data)  # return query set,  <RawQuerySet: seleect * from student>

# for i in data:
#     print(i)   # return all the data inside of query set



"""multiple dataabase"""
DATA_BASE = "second_db"
data = Student.objects.using(DATA_BASE).all()
print(data) # <QuerySet []> , return empty becouse we don't have anything inside this database

"""creating a data for second database"""

# c1 = College.objects.using(DATA_BASE).create(name= "COEP", add= "Pune") 
# d1 = Department.objects.using(DATA_BASE).create(name= "Chemical",dept_stringth= 60, college= c1)
# s1= Student.objects.using(DATA_BASE).create(name = "ABC", mark= 78, age= 23, dept = d1)
# s2 = Student.objects.using(DATA_BASE).create(name= "XYZ", mark= 89, age= 24, dept = d1)
# subj_1 = Subject.objects.using(DATA_BASE).create(name= "Engineering Chemistry", is_practical= True, dept= d1)


# subj_2 = Subject.objects.using(DATA_BASE).create(name = "Eniginnering Physics", is_practical= True, dept= Department.objects.get(id = 1))


# subj_2 = Subject.objects.using(DATA_BASE).get(id=2).delete()


studs = Student.objects.using(DATA_BASE).filter(id__gte= 0)
subj_1 = Subject.objects.using(DATA_BASE).get(id= 1)
print(subj_1)
subj_2 = Student.objects.using(DATA_BASE).get(id= 3)

# for stud in studs:
#     stud.subjs.add(subj_1)
#     stud.subjs.add(subj_2)
studs[0].subjs.add(subj_2)
