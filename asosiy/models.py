from django.db import models

class Bolim(models.Model):
    nom=models.CharField(max_length=100)
    rasm=models.FileField(null=True)

    def __str__(self):
        return self.nom
