from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Transaction
        fields = ["user", "type", "amount", "description", "date", "created_at"]
        read_only_fields = ['created_at']