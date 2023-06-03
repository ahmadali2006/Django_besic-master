from django.db import models



car_models=(
    ("1","Yengil automobil"),
    ("2","Yuk automobil"),
    ("3","sport automobil")
)

fuels=(
    ("1","Benzin"),
    ("2","Dizel"),
    ("3","Gas")
)
class Transport(models.Model):
    driver_id=models.ForeignKey(to="Driver",on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    model=models.CharField(choices=car_models,max_length=50)
    year=models.IntegerField()
    description=models.TextField(help_text="Mashina haqida qisqacha ma`lumot",null=True,blank=True)
    price=models.DecimalField(decimal_places=2,max_digits=15)
    color=models.CharField(max_length=50,null=True,blank=True)
    fuel=models.CharField(choices=fuels,default="1",max_length=15)

    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name=models.CharField(max_length=30)
    surename=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    tel=models.CharField(max_length=15)

    def __str__(self):
        return self.name

