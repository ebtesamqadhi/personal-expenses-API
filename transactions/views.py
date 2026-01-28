from rest_framework import generics, permissions
from .serializers import TransactionSerializer
from .models import Transaction
# Create your views here.

class TransactionList(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # البيانات اللي بيتم عرضه عند GET
    def get_queryset(self):
        print("USER:", self.request.user)
        return Transaction.objects.filter(user=self.request.user)

    # عند POST يخزن المستخدم تلقائيا
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class Transaction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    