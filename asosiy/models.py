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

    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Izoh(models.Model):
    matn = models.CharField(max_length=30)
    sana = models.DateTimeField(null=True, blank=True)
    baho = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.matn

# 1. Localda abdulhamid branchida o'zgarish qildim.
# 2. add va commit qildim
# 3. git fetch origin
# 4. git rebase origin/master
# Mabodo rebase o'xshamasa, conflictlarni(kelishmovchiliklarni)
# to'g'rilash kerak. Keyin:
#   git add ., git commit, git rebase --continue
# 5. git push origin abdulhamid

