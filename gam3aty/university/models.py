from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null=True, blank=True)
    location = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="university_images/",null=True, blank=True)

    def __str__(self):
        return self.name
    def get_total_majors(self):
        return self.colleges.aggregate(
            total=models.Count('majors')
        )['total']