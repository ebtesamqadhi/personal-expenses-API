from django.urls import path
from .views import *

urlpatterns = [
    path('', TransactionList.as_view()),
    path('<int:pk>', Transaction.as_view())
]