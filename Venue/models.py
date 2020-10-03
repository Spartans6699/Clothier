from django.db import models

# # Create your models here.

class Slide_Picture(models.Model):
    Picture_1=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_2=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_3=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_4=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_5=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_6=models.ImageField(default='default.jpg',upload_to='Picture')
    
    def __str__(self):
        return 'SLide Pictures'

class Picture(models.Model):
    Base_Picture=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_1=models.ForeignKey(Slide_Picture,on_delete=models.CASCADE)
    Picture_2=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_3=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_4=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_5=models.ImageField(default='default.jpg',upload_to='Picture')
    Picture_6=models.ImageField(default='default.jpg',upload_to='Picture')
    
    
    def __str__(self):
        return 'Pictures'


class Description(models.Model):
    Base_Picture_Heading_1=models.CharField(max_length=100)
    Base_Picture_Heading_2=models.CharField(max_length=100)
    Heading_1=models.CharField(max_length=100)
    Description_1=models.CharField(max_length=1000)
    Heading_2=models.CharField(max_length=100)
    Description_2=models.CharField(max_length=1000)
    Heading_3=models.CharField(max_length=100)
    Description_3=models.CharField(max_length=1000)
    Heading_4=models.CharField(max_length=100)
    Description_4=models.CharField(max_length=1000)
    Heading_5=models.CharField(max_length=100)
    Description_5=models.CharField(max_length=1000)
    Heading_6=models.CharField(max_length=100)
    Description_6=models.CharField(max_length=1000)

    def __str__(self):
        return 'Headings and Descriptions'
    
