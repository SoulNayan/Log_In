from django.db import models
from django.forms import ModelForm

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_images/')

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name","surname","email","contact","password","image"]

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_image/')
    title = models.CharField(max_length=300)

class SliderForm(ModelForm):
    class Meta:
        model = Slider
        fields = ["image","title"]

class Categories(models.Model):
    image = models.ImageField(upload_to='Categories_image/')
    title = models.CharField(max_length=300)

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["image","title"]