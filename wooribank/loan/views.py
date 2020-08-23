from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from wooribank.loan.models import LoanInfo


@login_required
def sale(request):
    user = request.user
    loan_list = LoanInfo.objects.filter(user__pk=user.id)
    context = {'loan_list': loan_list}
    return render(request,'loan/sale.html', context)


@login_required
def new_loan(request):
    return render(request,'loan/new.html')

@login_required
def create_or_update(request):
    return render(request,'loan/new.html')