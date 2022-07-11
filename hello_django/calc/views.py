from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('calc')


from django.views import View

class CalcView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'calc/index.html', context={
            'A':  kwargs['A'],
            'B': kwargs['B'],
            'SUM': kwargs['A'] + kwargs['B'],
        })
