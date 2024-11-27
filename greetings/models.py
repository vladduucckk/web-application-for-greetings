from django.db import models


class Researcher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    joined_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
