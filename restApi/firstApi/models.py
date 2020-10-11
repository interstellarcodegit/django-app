from django.db import models

# Create your models here.
class Users(models.Model):
    
  name=models.CharField(max_length=50,unique=True)
  email=models.EmailField(max_length=50, unique=True)
  password= models.CharField(max_length=50)

  date_joined= models.DateTimeField(auto_now_add=True)
    
    

    
