from django.db import models

# Create your models here.
class From1(models.Model):
    name = models.CharField(max_length=25,blank=True)
    number = models.CharField(max_length=10)
    #last = models.CharField(max_length=25,blank=True)
    #father_name = models.CharField(max_length=25,blank=True)
    #mother_name = models.CharField(max_length=25,blank=True)
    email=models.EmailField(max_length=40,blank=True)
    #address = models.CharField(max_length=55,blank=True)
    #city= models.CharField(max_length=20,blank=True)
    #number = models.CharField(max_length=10)
    carmodel = models.CharField(max_length=12)
    
   
    #Aadhrnumber=models.IntegerField()
   
    def __str__(self):
        return self.name



class From2(models.Model):
    name = models.CharField(max_length=25,blank=True)
    number = models.CharField(max_length=10)
    #last = models.CharField(max_length=25,blank=True)
    #father_name = models.CharField(max_length=25,blank=True)
    #mother_name = models.CharField(max_length=25,blank=True)
    email=models.EmailField(max_length=40,blank=True)
    address = models.CharField(max_length=55,blank=True)
    city= models.CharField(max_length=20,blank=True)
    #number = models.CharField(max_length=10)
    #number1 = models.CharField(max_length=12)
    about = models.CharField(max_length=25,blank=True)
    comment = models.CharField(max_length=100,blank=True)
    
   
    #Aadhrnumber=models.IntegerField()
   
    def __str__(self):
        return self.name        