from django.db import models
from university.models import University

class College(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="college_images/",null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="colleges")

    def __str__(self):
        return self.name