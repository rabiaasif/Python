from django.db import models

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length = 256)
    def __str__(self):
        return str(self.id) #+ "-"+ str(self.mib_id) + "-" + str(self.time_played)[:19]

class LastName(models.Model):
    last_name = models.ForeignKey('webapp.Name', default = None, on_delete=models.CASCADE,related_name='name_id')
    class Meta:
        ordering = ('id',)
    def __str__(self):
        return  str(self.id)