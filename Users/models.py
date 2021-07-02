from django.db import models


class UsersModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    salary = models.FloatField()

    def __str__(self):
        return self.name
