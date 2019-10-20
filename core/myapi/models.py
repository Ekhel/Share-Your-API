from django.db import models
from django.conf import settings

class website(models.Model):
    id_web = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=200)
    link = models.CharField(max_length=250, blank=True, null=True)
    deskripsi = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id_web',)

    def __str__(self):
        return self.nama

class linkapi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_link = models.AutoField(primary_key=True)
    link_web = models.ForeignKey(website, on_delete=models.CASCADE)
    urlapi = models.CharField(max_length=250)
    deksripsi_link = models.TextField()
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return self.link_web.nama
