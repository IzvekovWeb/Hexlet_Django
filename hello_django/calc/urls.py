from django.urls import path
from hello_django.calc.views import CalcView

urlpatterns = [
    path('', CalcView.as_view(), name='cal'),
]
