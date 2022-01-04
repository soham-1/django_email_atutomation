from django.db import models

# Create your models here.

class EmailModel(models.Model):

    CITIES = [
        ("Mumbai", "Mumbai"),
        ("Delhi", "Delhi"),
        ("Chennai", "Chennai"),
        ("Bengaluru", "Bengaluru"),
        ("Kolkata", "Kolkata")
    ]

    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    city = models.CharField(max_length=100, choices=CITIES, default="Mumbai")
    send_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + "_" + self.send_time.strftime("%d-%m-%Y")