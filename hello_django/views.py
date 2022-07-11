from django.shortcuts import render

from django.shortcuts import redirect
from django.urls import reverse

# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })


from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


class Index(TemplateView):
    def get(self, request):
        return redirect(reverse('calc', kwargs={'A': 40, 'B': 2}))

        # reverse можно опустить, он будет вызван неявно
        # return redirect('calc', A=40, B=2)
