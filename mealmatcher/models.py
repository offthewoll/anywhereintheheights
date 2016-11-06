from django.db import models
from django.contrib.auth.models import User
    
class MealTime(models.Model):
    MealType = models.CharField(max_length = 14)
    
    def __str__(self):
        return self.MealType

class Gender(models.Model):
    GenderType = models.CharField(max_length = 13)
    
    def __str__(self):
        return self.GenderType

class CoedSettings(models.Model):
    CoedType = models.CharField(max_length = 40)
    
    class Meta:
        verbose_name_plural = 'Coed Settings'
    
    def __str__(self):
        return self.CoedType
    
class FoodRestriction(models.Model):
    RestrictionType = models.CharField(max_length = 13)
    
    def __str__(self):
        return self.RestrictionType

class UserSettings(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    CoedSetting = models.ForeignKey(CoedSettings, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'User Settings'

class Host(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=10)

class Guest(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    RestrictionID = models.ForeignKey(FoodRestriction, on_delete=models.CASCADE)
    Notes = models.TextField()

class Meal(models.Model):
    HostID = models.ForeignKey(User, on_delete=models.CASCADE)
    MealDate = models.DateField()
    MealTimeID = models.ForeignKey(MealTime, on_delete=models.CASCADE)
    CoedSetting = models.ForeignKey(CoedSettings, on_delete=models.CASCADE)

class GuestRequest(models.Model):
    HostID = models.ForeignKey(User, on_delete=models.CASCADE)
    MealTimeID = models.ForeignKey(MealTime, on_delete=models.CASCADE)
    MealDate = models.DateField()
