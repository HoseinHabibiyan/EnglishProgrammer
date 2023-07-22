from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils.crypto import get_random_string

class RefrenceSeri(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/', default='empty')
    description = HTMLField(null=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    def save(self, *args, **kwargs):
         if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            suffix = 1
            while Refrence.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{get_random_string(length=4)}"
                suffix += 1
            self.slug = unique_slug
         super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Language(models.Model):
     name = models.CharField(max_length=100)   
     cover = models.ImageField(upload_to='images/', default='empty')
     def __str__(self):
        return self.name
class Skill_level(models.Model):
     name = models.CharField(max_length=100)   
     cover = models.ImageField(upload_to='images/', default='empty')
     def __str__(self):
        return self.name    
class Category(models.Model):
     name = models.CharField(max_length=100)  
     cover = models.ImageField(upload_to='images/', default='empty')
     description = HTMLField()
     def __str__(self):
        return self.name      
class Keyword(models.Model):
     name = models.CharField(max_length=100)  
     def __str__(self):
        return self.name       
    
class Refrence(models.Model):
    seri =  models.ForeignKey(RefrenceSeri, on_delete=models.CASCADE,blank=True)   
    language =  models.ForeignKey(Language, on_delete=models.CASCADE,blank=True,null=True)   
    skill_level =  models.ForeignKey(Skill_level, on_delete=models.CASCADE,blank=True,null=True)   
    category =  models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)   
    related_references = models.ManyToManyField('self', blank=True)
    keywords = models.ManyToManyField(Keyword, blank=True,null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    author = models.CharField(max_length=100,null=True)
    publisher =  models.CharField(max_length=100,null=True)
    description = HTMLField()
    link = models.URLField(default='empty')
    cover = models.ImageField(upload_to='images/', default='empty')
    document = models.FileField(upload_to='docs/', default='empty')

    def save(self, *args, **kwargs):
         if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            suffix = 1
            while Refrence.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{get_random_string(length=4)}"
                suffix += 1
            self.slug = unique_slug
         super().save(*args, **kwargs)
    class Meta:
        db_table = 'Refrence'  # New table name
    def __str__(self):
        return self.name

class Track(models.Model):
    refrence = models.ForeignKey(Refrence, on_delete=models.CASCADE,default=1)   
    name = models.CharField(max_length=100)
    document = models.FileField(upload_to='tracks/', default='empty')

    
class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)   
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
    task1 = models.ForeignKey(Refrence, on_delete=models.CASCADE, related_name='weekplan_task1')
    task2 = models.ForeignKey(Refrence, on_delete=models.CASCADE, related_name='weekplan_task2',null=True)
    task3 = models.ForeignKey(Refrence, on_delete=models.CASCADE, related_name='weekplan_task3',null=True)
    task4 = models.ForeignKey(Refrence, on_delete=models.CASCADE, related_name='weekplan_task4',null=True)
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
    
    

        