from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=12)
    

    def __str__(self) -> str:
        return self.name
