from django.db import models
from college.models import College

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="college_images/",null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="majors")
    categories = models.ManyToManyField(Category, related_name="majors")
    fees_per_term = models.DecimalField(decimal_places=2, max_digits=10, default=100)

    def __str__(self):
        return self.name
    

