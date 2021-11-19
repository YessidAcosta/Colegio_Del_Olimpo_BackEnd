from authApp.models.account import Account
from authApp.models.transaction import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['origin_account','destiny_account','amount', 'register_date','note']

    def to_representation(self,obj):
        origin_account = Account.objects.get(id=obj.origin_account)
        destiny_account = Account.objects.get(id=obj.destiny_account)
        transaction = Transaction.objects.get(id=obj.id)

        return {
            'id': transaction.id,
            'amount': transaction.amount,
            'register_date': transaction.register_date,
            'note': transaction.note,
            'origin_account':{
                'id': origin_account.id,
                'balance': origin_account.balance,
                'lastChangeDate': origin_account.lastChangeDate,
                'isActive': origin_account.isActive
            },
            'destiny_account':{
                'id': destiny_account.id,
                'balance': destiny_account.balance,
                'lastChangeDate': destiny_account.lastChangeDate,
                'isActive': destiny_account.isActive
            }
        }