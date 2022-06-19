import mpld3
import matplotlib
import psutil
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
from email.mime import message
# from pyexpat.errors import messages
from django.shortcuts import render
from urllib import response
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.test import ignore_warnings
from django.shortcuts import redirect, render
from urllib3 import HTTPResponse
from .forms import *
from .models import *

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login as login2, logout
from django.contrib.auth.decorators import login_required
# from PIL import Image
# from PIL.Image import fromstring
import io


def index(request):
    user = userform()
    if request.method == "POST":
        user = userform(request.POST)

        print(user.errors)
        if user.is_valid():
            user.save()
            # username = user.cleaned_data.get('name')

            return redirect('login')
    if request.user.is_authenticated:
        return render(request, 'index.html', {"user": user, "home": "abc"})

    return render(request, 'index.html', {"user": user})


def login(request):

    if request.method == "POST":
        email2 = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email2, password=password)
        # print(user)
        # messages.success(request, "successful login")

        if user is not None:
            login2(request, user)

            messages.success(request, "successful login")
            # time = User.objects.get(username=email2).last_login
            return redirect('home')
        else:

            return render(request, "login.html", {"error": "Email or password is incorrect"})

    user = {}
    return render(request, 'login.html', user)


@login_required(redirect_field_name='accounts/login')
def home(request):
    now = "abc"
    print("user:", now)

    return render(request, 'home.html', {"name": now})


def logoutuser(request):
    logout(request)
    return redirect('login')


def check_cpu(request):
    if not request.user.is_authenticated:
        return redirect('error')
    import psutil
    # Getting % usage of virtual_memory ( 3rd field)
    print('RAM memory % used:', psutil.virtual_memory()[2])
    # Calling psutil.cpu_precent() for 5 seconds
    print('The CPU usage is: ', psutil.cpu_percent(5))

    return render(request, "home.html", {"vm": psutil.virtual_memory()[2], "cpu": psutil.cpu_percent(5)})


def error(request):
    return render(request, 'error.html', {})


def error2(request):
    return render(request, 'error2.html', {})
# def cpu(request):
#     import matplotlib.pyplot as plt
#     from matplotlib.animation import FuncAnimation

# def path_not_avai(request):
#     if request.path
#     FuncAnimation(plt.gcf(),plot_cpu,interval=1000)
# def plot_cpu():
#     import psutil
#     import matplotlib.pyplot as plt
#     from matplotlib.animation import FuncAnimation
#     frame_len=200
#     y=[]
#     y.append(psutil.cpu_percent())
#     if len(y)<=frame_len:
#         plt.cla()
#         plt.plot(y,'r',label='Real-Time CPU usage')
#     plt.tight_layout()


frame_len = 200
y = []


def cpu(request):

    y.append(psutil.cpu_percent())
    if len(y) <= frame_len:
        plt.cla()
        plt.plot(y, 'r', label='Real-Time CPU usage')
    plt.tight_layout()
    fig = plt.figure(figsize=(6, 2))

    anim = FuncAnimation(plt.gcf(), cpu, interval=1000)
    # context = {"show": show}

    # fill the report here

    # fig.savefig(response)
    # return response

    # Send buffer in a http response the the browser with the mime type image/png set
    # return HttpResponse(buffer.getvalue(), mimetype="image/png")
    # return render(request, 'home.html', context)
