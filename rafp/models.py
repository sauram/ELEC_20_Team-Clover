from django.db import models

class data(models.Model):
    #name=models.CharField(max_length=20)
    a=models.FloatField(default=0.0)
    b=models.FloatField(default=0.0)
    c=models.FloatField(default=0.0)
    d=models.FloatField(default=0.0)
    e=models.FloatField(default=0.0)
    f=models.FloatField(default=0.0)
    g=models.FloatField(default=0.0)
    h=models.FloatField(default=0.0)
    x=models.IntegerField(default=0)
    y=models.IntegerField(default=0)
    today=models.DateField(auto_now=False)
    time=models.TimeField(auto_now=False)
    area=models.FloatField(default=0.0)
    fire=models.IntegerField(default=0)

    def __str__(self):
        return "data"

