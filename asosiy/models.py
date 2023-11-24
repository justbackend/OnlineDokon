from django.db import models
from userapp.models import Account

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

    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Izoh(models.Model):
    matn = models.TextField()
    sana = models.DateTimeField(null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    baho = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.matn