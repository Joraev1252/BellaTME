from uuid import uuid4

from django.db import models

# Create your models here.


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'logo/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class PartnersModel(models.Model):
    logo = models.ImageField('Photo', upload_to=upload_location)
    link = models.URLField('Link', max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.link)


