from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)
    phone = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name

class Pathology(models.Model):
    pathology = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pathology