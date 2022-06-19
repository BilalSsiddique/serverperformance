from django.utils.timezone import now
import os
from django.shortcuts import render
import psutil
import sys
from django.utils.deprecation import MiddlewareMixin
from urllib3 import HTTPResponse
from .models import *

# from django.renderers

THRESHOLD = 2*1024*1024


class MemoryUsageMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request._mem = psutil.Process(os.getpid()).memory_info()

    def process_response(self, request, response):
        mem = psutil.Process(os.getpid()).memory_info()
        diff = mem.rss

        # if diff > THRESHOLD:
        if request.user.is_authenticated:
            user = request.user.name._wrapped if hasattr(
                request.user.name, '_wrapped') else request.user.name
        # print(sys.stderr, "MEMORY USAGE '{0}'".format(
        #     (diff, request.user.name)))
        # response.accepted_renderer = JSONRenderer()

    # Getting % usage of virtual_memory ( 3rd field)
    #     print('RAM memory % used:', psutil.virtual_memory()[2])
    # # Calling psutil.cpu_precent() for 5 seconds
    #     print('The CPU usage is: ', psutil.cpu_percent(5))
        print(request.path)
        if request.path == '/check':
            return render(request, "home.html", {"vm": psutil.virtual_memory()[2], "cpu": psutil.cpu_percent(5), "sys": user, "mem": diff, "req": request.path})
    # return render(request, "home.html", {"sys": user, "mem": diff, "req": request.path})
        return response

        # response.render()
        # if hasattr(response, "render") is not None:
        #     return response


class SetLastVisitMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_authenticated:
            # Update last visit time after request finished processing.
            now2 = user.objects.get(email=request.user).last_login.strftime(
                '%y-%m-%d %a %H:%M:%S')

            print("user:", now2)
            if request.path == '/home':
                return render(request, 'home.html', {"name": now2})
        return response
