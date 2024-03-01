from django.db import models

# Create your models here.
class Data(models.Model):
    content = models.CharField(max_length=300)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    def __str__(self):
        return self.content[0:6]