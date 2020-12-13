

# Create your models here.
from django.db import models

# Create your models here.
class SiteLoc(models.Model):
    site_id = models.AutoField
    site_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=800)
    image = models.ImageField(upload_to="blog/images", default="")
    image2 = models.ImageField(upload_to="blog/images", default="")
    image3 = models.ImageField(upload_to="blog/images", default="")
    image4 = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return self.site_name




class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=122, null=True, blank=True)
    user_email = models.CharField(max_length=122, null=True, blank=True)

    def __str__(self):
        return str(self.user_name)
