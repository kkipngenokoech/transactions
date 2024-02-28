from django.db import models

# Create your models here.
class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_id = models.ForeignKey('Account', related_name='transactions', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.transaction_description
    
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_name = models.CharField(max_length=100)
    def __str__(self):
        return self.account_name