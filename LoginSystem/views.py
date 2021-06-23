from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import strip_tags
import json
from django.http.response import HttpResponseRedirect, JsonResponse
from LoginSystem.forms import SignupForm
from LoginSystem.models import LabData


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
        percentage = request.POST.get('value')
        print(percentage)
        form_data_list = json.loads(percentage)
        email = form_data_list[1]["value"]
        password1 = form_data_list[2]["value"]
        password2 = form_data_list[3]["value"]
        address1 = form_data_list[4]["value"]
        address2 = form_data_list[5]["value"]
        city = form_data_list[6]["value"]
        state = form_data_list[7]["value"]
        open_time = form_data_list[8]["value"]
        close_time = form_data_list[9]["value"]
        test = form_data_list[10]["value"]
        pincode = form_data_list[11]["value"]
        print(email,password1,password2,address1,address2,city,state,open_time,close_time,test,pincode)
        main_form = {"username":email,"password1":password1,"password2":password2,"password":password1}
        form = SignupForm(main_form)
        if form.is_valid():
            New_Data = LabData(email=email,address1=address1,address2=address2,city=city,state=state,open_time=open_time,close_time=close_time,test=test,pincode=pincode)
            try: 
                New_Data.save()
                form.save()
            except Exception as e:
                print(str(e))
                context={"success":"false","messages":str(e)}
                return JsonResponse(context)
            context={"success":"true","messages":"Account created successfully !!"}
            return JsonResponse(context)
        else:
            x = form.errors
            context={"success":"false","messages":x}
            return JsonResponse(context)
    return render(request, 'Lab_Register.html')

