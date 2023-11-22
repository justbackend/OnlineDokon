from django.db import models

class Bolim(models.Model):
    nom=models.CharField(max_length=100)
    rasm=models.FileField(null=True)

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=30)
    brend = models.CharField(max_length=20)
    narx = models.CharField(max_length=30)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    batafsil = models.CharField(max_length=30, blank=True, null=True)

    def str(self):
        return self.nom