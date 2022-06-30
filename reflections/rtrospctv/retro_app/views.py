from django.shortcuts import render
from django.http import HttpResponse
import csv
import os
import random
from re import I

# Create your views here.
def index(request):
    # return HttpResponse("hello world, we've started\nblah",)
    data = {'data':'this is the data'}
    return render(request, 'retro_app/index.html', data)

def magic(request):
    pass

def contestant(request):
    #hard coding num here bc we dont have an input:
    num = 100

    former_reflectors = ['Alisha Burgfeld','Daniel Reither']

    random_number=random.randint(1,num)
    print(random_number)

    students = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "students.csv")

    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'] != former_reflectors[0] and row['Name'] != former_reflectors[1]:
                students.append(row)

    print(students)    
    rolls=[]
    for student in students:
        roll=random.randint(1,num)
        if roll not in rolls:
            rolls.append(roll)
            student["Number"]= roll

    # print(students)
    # print(rolls)
    
    closest=num
    closest_student={} 

    for student in students:
        if abs(random_number-int(student["Number"])) < closest:
            closest= abs(random_number-int(student["Number"]))
            # print(f"closest: {closest}")
            closest_student=student
    #appending the names of the person chosen to the list.
    former_reflectors.append(closest_student['Name'])
    print(closest_student)
    print(former_reflectors)
    data = closest_student
    
    return render(request, 'retro_app/contestant.html',data)

