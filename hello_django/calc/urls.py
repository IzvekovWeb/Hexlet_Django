from django.urls import path
from hello_django.calc.views import CalcView
from hello_django.calc import views

urlpatterns = [
    path('<int:A>/<int:B>', CalcView.as_view(), name="calc"),
    # path('', views.show_history),
]
