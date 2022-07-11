from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('calc')

from django.views import View

class CalcView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')
