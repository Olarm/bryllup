from django.db import models

from sorl.thumbnail import ImageField

# Create your models here.




class FrontpageImage(models.Model):
    image = ImageField(upload_to="frontpage_images")
