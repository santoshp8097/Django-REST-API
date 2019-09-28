
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from app.models import FibonacciTest
from django.views import View


import time



def fibonacci(numeric):
    if numeric<0:
        print("Incorrect Input")
    elif numeric<=2:
        return 1
    elif numeric ==3:
        return 2
    else:
        return fibonacci(numeric-1) + fibonacci(numeric-2)


class FibonacciAPIView(View):
    def get(self, request):
        number = request.GET.get('value')
    
        if number is None:
            return render(request, 'index.html')
        else:
            start_time = time.time()
            numeric = int(number)
            output = fibonacci(numeric)
            end_time = time.time() - start_time
            latency = str(end_time)[0:3]
            fibonacci_qs = FibonacciTest.objects.create(numeric=numeric,output=output,latency=latency)
            fibonacci_qs.save()
            data = {'numeric':numeric,'output':output,'latency':latency}         
            return render(request, 'index.html', data)