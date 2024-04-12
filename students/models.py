from django.db import models

class students(models.Model):
    image=models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    name=models.CharField(max_length=50,null=True)
    section=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self):
        return self.name





