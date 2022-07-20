from django.db import models

# Create your models here.

class Urunler(models.Model):
    baslik = models.CharField(max_length=150)
    kisa_aciklama = models.TextField(max_length=150)
    resim = models.CharField(max_length=300)
    tarih = models.DateTimeField(auto_now_add=True)
    aciklama = models.TextField()

    def __str__(self):
        return self.baslik
