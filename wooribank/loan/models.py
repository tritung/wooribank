from django.utils import timezone
from enum import IntEnum

from django.db import models

from wooribank.models import UserInfo


class LoanTypes(IntEnum):
    LOAN = 0
    CREDIT_CARD = 1
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    
class LoanStatus(IntEnum):
    NEW = 0
    LEADER_REVIEW = 1
    LEADER_RETURN = 2
    LEADER_APPROVE = 3
    ADMIN_REVIEW = 4
    ADMIN_RETURN = 5
    COMPLETED = 6
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    
class LoanInfo(models.Model):
    user = models.OneToOneField(UserInfo,on_delete=models.CASCADE)
    name = models.TextField(null=True)
    type = models.IntegerField(choices=LoanTypes.choices(), default=LoanTypes.LOAN)
    status = models.IntegerField(choices=LoanStatus.choices(), default=LoanStatus.NEW)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    
    leader_approve_at = models.DateTimeField(null=True)
    leader = models.CharField(max_length=20, null=True)
    admin_approve_at = models.DateTimeField(null=True)
    admin = models.CharField(max_length=20, null=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    

class LoanInfoHistory(models.Model):
    loan_info = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    note = models.TextField(null=True)
    user = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(default=timezone.now)
