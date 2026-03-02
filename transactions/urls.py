from django.urls import path
from .views import *

urlpatterns = [
    path('', TransactionList.as_view()),
    path('<int:pk>', TransactionDetail.as_view()),
    path('category', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
]