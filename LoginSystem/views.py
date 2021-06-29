from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import redirect, render
from django.utils.html import strip_tags
import json,base64,requests,io 
from PIL import Image
from datetime import date,timedelta
from django.http.response import JsonResponse
from LoginSystem.forms import *
from LoginSystem.models import *
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

API_KEY = 'cfff528b915d4bbc8ef789472fe7041d'


def index(request):
    messages.add_message(request, messages.INFO, 'Welcome to The Hospital Portal !')
    return render(request, 'index.html')


def home(request):
    return render(request,'index.html')
    
def mailer(request):
    if request.method == 'POST':
        val = request.POST.get('value')
        data = base64.b64decode(val.encode('UTF-8'))
        buf = io.BytesIO(data)
        img = Image.open(buf)
        arr = []
        
        get_user_data = UserData.objects.get(username = request.user.username)
        user_email = str(get_user_data.email)
        print(user_email)
        arr.append(user_email)
        img.save(r'Hospital_Management/static/img/test.png',resolution=200)
        mail_content = render_to_string('mailer.html', {'context': 'values'})
        plain_message = strip_tags(mail_content)
        plain_message = plain_message.replace("User",request.user.username)
        print(plain_message)
        email = EmailMessage(str("Welcome to Medcheck")+' || '+str("Thanks for Slot Booking"),plain_message,settings.EMAIL_HOST_USER,arr)
        email.attach_file('Hospital_Management/static/img/test.png')
        email.send()
        return JsonResponse({"message":"Successfull !!"})
    return render(request,'mailer.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('Lab_Login')

@login_required(login_url='Lab_Login')        
def book_slot(request):
    today = date.today()
    current_user = request.user.username
    # print(current_user)
    get_user_data = UserData.objects.get(username = current_user)
    hospital_list = HospitalData.objects.all()
    test_list = Test.objects.all()
    context = {'hospital_list': hospital_list,"test_list":test_list,"get_user_data":get_user_data,"date":today}
    if(request.method == 'GET'):
        data = request.GET.get('value')
        if(data):
            result = Test.objects.filter(hospital_id=data)
            send_json = {}
            for i in result:
                send_json[i.test_name] = i.test_price
            # print(send_json)
            return JsonResponse(send_json)
    if request.method == 'POST':
        form = BookSlotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Slot Added!') 
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return render(request, 'book_slot.html',context)
    return render(request,'book_slot.html',context )
    
def hospital_search(request):
    hospital_list = HospitalData.objects.all()
    return render(request,'hospital_search.html', {'hospital_list': hospital_list})
    
def hot_module(request):
    today = date.today()
    yesterday = today - timedelta(days = 1)
    # print(today)
    country = request.GET.get('country')
    category = request.GET.get('category')
    # print(country)
    # print(category)

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
    else:
        url = f'https://newsapi.org/v2/everything?q={category}&from={yesterday}&sortBy=popularity&language=en&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
    articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request,'hot_module.html',context)
    

def add_test(request):
    current_user = request.user.username
    # print(current_user)
    hospital_list = HospitalData.objects.get(email = current_user )
    # print(hospital_list.Hospital_Name)
    context = {'hospital_list': hospital_list}
    if request.method == 'POST':
        if Test.objects.filter(test_name=request.POST['test_name'],hospital_id=request.POST['hospital_id']) :
            messages.error(request,"The Test "+request.POST['test_name'] + ' already exits in '+ HospitalData.objects.get(Hospital_ID=request.POST['hospital_id']).Hospital_Name)
            return render(request, 'test_data.html',context)

        form = AddTest(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Test Added!') 
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return render(request, 'test_data.html',context)
    return render(request,'test_data.html',context)


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
        # print(formData)
        i=1
        form_data_list = json.loads(formData)
        Hospital_Name = form_data_list[i]["value"]
        regNo = form_data_list[i+1]["value"]
        email = form_data_list[i+2]["value"]
        password1 = form_data_list[i+3]["value"]
        password2 = form_data_list[i+4]["value"]
        address1 = form_data_list[i+5]["value"]
        address2 = form_data_list[i+6]["value"]
        address = address1 + ","+ address2
        phoneNo = form_data_list[i+7]["value"]
        pincode = form_data_list[i+8]["value"]
        city = form_data_list[i+9]["value"]
        state = form_data_list[i+10]["value"]
        open_time = form_data_list[i+11]["value"]
        close_time = form_data_list[i+12]["value"]
        # print(Hospital_Name,email,phoneNo,address,city,state,open_time,close_time,pincode)
        New_Data = HospitalData(Hospital_Name= Hospital_Name,regNo = regNo,email=email,phoneNo=phoneNo,address=address,city=city,state=state,open_time=open_time,close_time=close_time,pincode=pincode)
        main_form = {"username":email,"password1":password1,"password2":password2,"password":password1,"is_staff":1}
        form = SignupForm(main_form)
        try: 
            if form.is_valid():
                New_Data.save()
                form.save()
            else:
                x = form.errors
                context={"success":"false","messages":x}
                return JsonResponse(context)
        except Exception as e:
            # print(str(e))
            context={"success":"false","messages":str(e)}
            return JsonResponse(context)
        context={"success":"true","messages":"Hospital Registration done successfully !!"}
        return JsonResponse(context)
    return render(request, 'Lab_Register.html')
    
    
    
def User_Register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        username = request.POST.get("username")
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        address = request.POST.get("Address")
        blood_group = request.POST.get("blood_group")
        phoneNo = request.POST.get("phoneNo")
        id_proof_no = request.POST.get("id_proof_no")
        id_proof_name = request.POST.get("id_proof_name")     
        if form.is_valid():
            New_Data = UserData.objects.create(username = username,name=name,age = age,email = email ,gender = gender,address = address,
                            blood_group = blood_group,phoneNo = phoneNo,id_proof_no = id_proof_no,
                            id_proof_name = id_proof_name)
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
        else:
            messages.success(request, 'Please Enter Valid Details !')
            return redirect('User_Register')
    form = SignupForm()
    return render(request, 'User_Register.html', {'form': form})

