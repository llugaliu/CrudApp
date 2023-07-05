from django.db import models
class Position(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.title

class Employer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100,null=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.name