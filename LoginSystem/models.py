from django.db import models

class HospitalData(models.Model):
    Hospital_ID = models.AutoField(primary_key=True) 
    Hospital_Name = models.CharField(max_length=40,unique = True)
    email = models.CharField(max_length=40,unique = True)
    address = models.CharField(max_length=80)
    regNo = models.BigIntegerField(unique = True) 
    phoneNo = models.BigIntegerField(unique = True) 
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()
    test = models.CharField(max_length=20)
    pincode = models.BigIntegerField()

    class Meta:
        db_table = "Hospital Data"
        
class UserData(models.Model): 
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.CharField(max_length=40,unique = True)
    gender = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    blood_group = models.CharField(max_length=20)
    phoneNo = models.BigIntegerField(unique = True) 
    id_proof_name = models.CharField(max_length=20)
    id_proof_no = models.CharField(max_length=20)

    class Meta:
        db_table = "User Data"
        
class Test(models.Model): 
    hospital_id = models.ForeignKey(HospitalData, db_column='Hospital_ID', to_field='Hospital_ID', related_name='+',default=1, on_delete=models.SET_DEFAULT)
    test_name = models.CharField(max_length=40)
    test_price = models.BigIntegerField()

    class Meta:
        db_table = "Test"
        
class BookSlot(models.Model): 
    hospital_id = models.ForeignKey(HospitalData, db_column='Hospital_ID', to_field='Hospital_ID', related_name='+',default=1, on_delete=models.SET_DEFAULT)
    test_name = models.CharField(max_length=100)
    slot_date = models.DateField()
    slot_time = models.TimeField()
    test_price = models.BigIntegerField()
    user_id = models.IntegerField()

    class Meta:
        db_table = "Book Slot"
