from django.db import models


class LabData(models.Model):
    email = models.CharField(max_length=40,unique = True)
    address1 = models.CharField(max_length=80)
    address2 = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()
    test = models.CharField(max_length=20)
    pincode = models.BigIntegerField()

    class Meta:
        db_table = "Lab Data"