from uuid import uuid4

from django.db import models

# Create your models here.
RATING_CHOICES =(
    ('1', 1),
    ('2️', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)



def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'comment/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class CommentsModel(models.Model):
    user_name = models.CharField('name', max_length=50)
    user_image = models.ImageField('photo', upload_to=upload_location)
    rating = models.CharField(max_length=255,choices=RATING_CHOICES)

    def __str__(self):
        return str(self.user_name) and str(self.rating)