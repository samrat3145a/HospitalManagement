from django.contrib import admin
from .models import *

@admin.register(HospitalData)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('Hospital_ID','Hospital_Name','email' ,'address','regNo' ,'phoneNo','city','state','open_time','close_time','pincode')
    list_editable = ('Hospital_Name','email' ,'address','regNo' ,'phoneNo','city','state','open_time','close_time','pincode')
    
# @admin.register(UserData)
# class UserAdmin(admin.ModelAdmin):
#     test_display = ('username' ,'name ','age ','email ','gender ','address ','blood_group ','phoneNo ','id_proof_name' ,'id_proof_no ')