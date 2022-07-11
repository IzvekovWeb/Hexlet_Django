from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('calc')


from django.views import View
from hello_django.calc.models import History

class CalcView(View):

    def get(self, request, *args, **kwargs):
        h = History()
        h.value = kwargs['A'] + kwargs['B']
        h.save()

        history = History.objects.order_by('-timestamp')[:10]

        return render(request, 'calc/index.html', context={
            'A':  kwargs['A'],
            'B': kwargs['B'],
            'SUM': kwargs['A'] + kwargs['B'],
            'results': history
        })
    

# def show_history(request):
#     sums = History.objects.order_by('-timestamp').all()[:10]
#     return render(request, 'calc/history.html', context={'sums': sums})
