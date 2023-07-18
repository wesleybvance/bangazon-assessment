from django.db import models

class ThredsUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000)
    uid = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
