from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    UserID = models.ForeignKey('User', on_delete=models.CASCADE)
    Gender = models.ForeignKey('Gender', on_delete=models.CASCADE)
    Coed = models.ForeignKey('Coed', on_delete=models.CASCADE)

class Host(models.Model):
    UserID = models.ForeignKey('User', on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=10)

class Guest(models.Model):
    UserID = models.ForeignKey('User', on_delete=models.CASCADE)
    RestrictionID = models.ForeignKey('FoodRestriction', on_delete=models.CASCADE)
    Notes = models.TextField()

class Meal(models.Model):
    HostID = models.ForeignKey('User', on_delete=models.CASCADE)
    MealDate = models.DateField()
    MealTimeID = models.ForeignKey('MealTime', on_delete=models.CASCADE)
    Coed = models.ForeignKey('Coed', on_delete=models.CASCADE)

class GuestRequest(models.Model):
    HostID = models.ForeignKey('User', on_delete=models.CASCADE)
    MealTimeID = models.ForeignKey('MealTime', on_delete=models.CASCADE)
    MealDate = models.DateField()
    
class MealTime(models.Model):
    MealType = models.CharField(max_length = 14)

class Gender(models.Model):
    GenderType = models.CharField(max_length = 13)

class Coed(models.Model):
    CoedType = models.CharField(max_length = 40)
    
class FoodRestriction(models.Model):
    RestrictionType = models.CharField(max_length = 13)
