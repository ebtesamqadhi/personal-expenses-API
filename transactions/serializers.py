from rest_framework import serializers
from .models import Transaction, Category

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Transaction
        fields = ["user", 'id', "type", "amount", "category", "description", "date", "created_at"]
        read_only_fields = ['created_at']
        
    def validate_amount(self, value):
        if self.instance:
            raise serializers.ValidationError("The amount cannot be modified after creation.")
        if value <= 0:
            raise serializers.ValidationError('The amount must be greater than 0.')
        return value
    
    def validate_type(self, value):
        if self.instance:
            raise serializers.ValidationError("لا يمكن تعديل نوع المعاملة بعد الإنشاء.")
        return value
        
    def validate(self, data):
        if self.instance:
            return data
        
        amount = data.get('amount')
        transaction_type = data.get('type')
        balance = self.context.get('balance',0)
        
        if transaction_type =='expense':
            if amount > balance :
                raise serializers.ValidationError('The amount is greater than the balance.')
        return data
        
class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
    