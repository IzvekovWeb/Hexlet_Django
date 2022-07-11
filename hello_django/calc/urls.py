from django.urls import path
from hello_django.calc.views import CalcView

urlpatterns = [
    path('<int:A>/<int:B>', CalcView.as_view(), name="calc"),
]
