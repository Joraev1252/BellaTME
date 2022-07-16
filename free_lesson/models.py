from django.db import models


class FreeLessonModel(models.Model):   #Student's info for free lesson
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    sex = models.BooleanField(default=True, verbose_name="Gender", blank=True, null=True)

    def __str__(self):
        return str(self.name)



