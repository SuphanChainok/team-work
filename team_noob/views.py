from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')
<<<<<<< HEAD
def continue_view(request):
    return render(request, 'continue.html')
=======
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # เปลี่ยน 'home' เป็นชื่อ URL ของหน้าหลักที่คุณต้องการให้ผู้ใช้เข้าสู่หลังจาก login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')
def mappage(request):
<<<<<<< HEAD
    return render(request, 'map.html')
>>>>>>> e09930b19ee8f0f38869578d4db7dbdeecd94b04
=======
    return render(request, 'map.html')
>>>>>>> 051f978eebb86c8e562d3a434c2673e9d07c8899
