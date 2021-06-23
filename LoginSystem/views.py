from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import strip_tags
import json
from django.http.response import HttpResponseRedirect, JsonResponse
from LoginSystem.forms import SignupForm
from LoginSystem.models import HospitalData,UserData,Test


def index(request):
    return render(request, 'index.html')


@login_required(login_url='Lab_Login')
def homepage(request):
    return render(request, 'index.html')


@login_required(login_url='Lab_Login')
def home(request):
    return render(request,'index.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('Lab_Login')


def Lab_Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully login!')
            return redirect('home')
        else:
            messages.success(request, ' Error Logging In / Please try again !')
            return redirect('Lab_Login')
    return render(request, 'Lab_Login.html')


def Lab_Register(request):
    if request.method == 'POST':
        formData = request.POST.get('value')
        print(formData)
        i=1
        form_data_list = json.loads(formData)
        Hospital_Name = form_data_list[i]["value"]
        regNo = form_data_list[i+1]["value"]
        email = form_data_list[i+2]["value"]
        phoneNo = form_data_list[i+3]["value"]
        address1 = form_data_list[i+4]["value"]
        address2 = form_data_list[i+5]["value"]
        address = address1 + ","+ address2
        city = form_data_list[i+6]["value"]
        state = form_data_list[i+7]["value"]
        open_time = form_data_list[i+8]["value"]
        close_time = form_data_list[i+9]["value"]
        pincode = form_data_list[i+10]["value"]
        print(Hospital_Name,email,phoneNo,address,city,state,open_time,close_time,pincode)
        New_Data = HospitalData(Hospital_Name= Hospital_Name,regNo = regNo,email=email,phoneNo=phoneNo,address=address,city=city,state=state,open_time=open_time,close_time=close_time,pincode=pincode)
        try: 
            New_Data.save()
        except Exception as e:
            print(str(e))
            context={"success":"false","messages":str(e)}
            return JsonResponse(context)
        context={"success":"true","messages":"Hospital Registration done successfully !!"}
        return JsonResponse(context)
    return render(request, 'Lab_Register.html')
    
    
    
def User_Register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        address = request.POST.get("Address")
        blood_group = request.POST.get("blood_group")
        phoneNo = request.POST.get("phoneNo")
        id_proof_no = request.POST.get("id_proof_no")
        id_proof_name = request.POST.get("id_proof_name")

        New_Data = UserData(name=name,age = age,email = email ,gender = gender,address = address,
                            blood_group = blood_group,phoneNo = phoneNo,id_proof_no = id_proof_no,
                            id_proof_name = id_proof_name)
        New_Data.save()

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
        else:
            messages.success(request, 'Please Enter Valid Details !')
            return redirect('User_Register')
    form = SignupForm()
    return render(request, 'User_Register.html', {'form': form})

