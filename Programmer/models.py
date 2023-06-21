from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name
    
    
class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    grade =  models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WeekPlan(models.Model):  
    Student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    week_number = models.DecimalField(   decimal_places=0 , max_digits=3,default=1)
    task1 = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='weekplan_task1')
    task2 = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='weekplan_task2')
    task3 = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='weekplan_task3')
    task4 = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='weekplan_task4')
    def __str__(self):
        return f"Weekly Plan for {self.Student.first_name} {self.Student.last_name}"
    
class DailyProgram(models.Model):
    relatedweek = models.ForeignKey(WeekPlan, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    task1 = models.CharField(max_length=100)
    task2 = models.CharField(max_length=100)
    task3 = models.CharField(max_length=100)
    task4 = models.CharField(max_length=100)
    classday = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day} - {self.relatedweek.Student}"    
    
    

        