from django.db import models
from django.contrib.auth.models import User

class AdminApps(models.Model):
    CATEGORY_CHOICES = [
        ('category1', 'Educational apps'),
        ('category2', 'Lifestyle apps'),
        ('category3', 'Social media apps'),
        ('category4', 'Productivity apps'),
        ('category5', 'Entertainment apps'),
        ('category6', 'Game apps'),
    ]

    SUBCATEGORY_CHOICES = [
        ('subcategory1', 'Subcategory 1'),
        ('subcategory2', 'Subcategory 2'),
        # Add more subcategories as needed
    ]

    app_name = models.CharField(max_length=200)
    app_link = models.URLField()
    app_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    app_subcategory = models.CharField(max_length=20, choices=SUBCATEGORY_CHOICES)
    app_points = models.IntegerField(default=100)
    
    def __str__(self):
        return self.app_name

class UserApps(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    app_name = models.CharField(max_length=200)
    app_link= models.URLField()
    app_screenshot = models.ImageField(upload_to="app_screenshots")
    admin_app = models.ForeignKey(AdminApps, on_delete=models.CASCADE,null=True) 
    
    
   