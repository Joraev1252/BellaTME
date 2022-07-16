from uuid import uuid4

from django.db import models


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'course/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class CoursesModels(models.Model):
    title = models.CharField('Title', max_length=255)
    body = models.TextField(max_length=255)
    image = models.ImageField('Photo', upload_to=upload_location)

    def __str__(self):
        return str(self.title)

