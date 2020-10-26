from django.contrib import auth
from django.shortcuts import render
import pyautogui

# Create your views here.

def login(request):
    if request.method=="POST":
        user1=request.POST["username"]
        pass1=request.POST["pass"]
        user=auth.authenticate(username=user1, password=pass1)

        if user is not None:
            auth.login(request,user)
            from .models import uploads
            d = uploads.objects.all()
            # p=d[len(d-1].pic
            return render(request, "login.html", {'d': d})
        else:
            pyautogui.alert("Wrong username & password!")
            return render(request, "loginpage.html")

    else:
        return render(request, "loginpage.html")



def upload(request):
    if request.method == 'POST':
        p=request.FILES['image']
        from .models import uploads
        d=uploads(pic=p)
        d.save()
        pyautogui.alert("Upload done!")
        d=uploads.objects.all()
        # p=d[len(d-1)].pic
        return render(request, "login.html", {'d': d})


