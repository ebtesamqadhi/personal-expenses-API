from rest_framework import generics
from .serializers import TransactionSerializer
from .models import Transaction
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TransactionList(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    # البيانات اللي بيتم عرضه عند GET
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    # عند POST يخزن المستخدم تلقائيا
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user= self.request.user)
