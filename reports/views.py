from django.shortcuts import render
from accounting.models import Income,Expense
from loans.models import LoanPayment,LoanIssue,LoansIssue
from shares.models import ShareBuy,ShareSell
from savings.models import SavingDeposit,SavingWithdrawal
from django.db.models import Sum
from datetime import datetime

# Create your views here.

def report(request):
    template = 'reports/reports.html'

    return render(request, template)

def _income(year=datetime.now().year, month=datetime.now().month, yearly=False):
    if yearly == True:
        incomes = Income.objects.filter(delete_status = False, date_created__year = year)
    else:
        incomes = Income.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
    return incomes

def income(request):
    template = 'reports/income.html'

    # Implement date picker or something else that is less error prone
    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        incomes = _income(year=year,month=month)
    else:
        incomes = _income()

    context = {
        'items_income': incomes,
        'title_income': 'Income',
        'total_income': incomes.aggregate(Sum('amount'))['amount__sum']
        }

    return render(request, template, context)

def _expense(year=datetime.now().year, month=datetime.now().month, yearly=False):
    if yearly == True:
        expenses = Expense.objects.filter(delete_status = False, date_created__year = year)
    else:
        expenses = Expense.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
    return expenses

def expense(request):
    template = 'reports/expense.html'

    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        expenses = _expense(year=year,month=month)
    else:
        expenses = _expense()

    context = {
            'items_expenses': _expense(),
            'title_expenses': "Expense",
            'total_expense': expenses.aggregate(Sum('amount'))['amount__sum']
            }

    return render(request, template, context)

def _loan(year=datetime.now().year, month=datetime.now().month, yearly=False):
    if yearly == True:
        loans_rec = LoanPayment.objects.filter(delete_status = False, date_created__year = year)
        loans_issued = LoansIssue.objects.filter(delete_status = False, date_created__year = year)
    else:
        loans_rec = LoanPayment.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
        loans_issued = LoansIssue.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
    return {'loans_rec': loans_rec, 'loans_issued': loans_issued}

def loan(request):
    template = 'reports/loans.html'

    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        loan = _loan(year=year,month=month)
    else:
        loan = _loan()



    context = {
            'items_loans': loan.get("loans_rec","none"),
            'issued_items_loans': loan.get("loans_issued","none"),
            'title_loans': 'Loans',
            }

    return render(request, template, context)

def _capital(year=datetime.now().year, month=datetime.now().month,yearly=False):

    if yearly == True:
        shares_buy = ShareBuy.objects.filter(delete_status = False, date_created__year = year)
        shares_sell = ShareSell.objects.filter(delete_status = False, date_created__year = year)

        savings_deposit = SavingDeposit.objects.filter(delete_status = False, date_created__year = year)
        savings_withdrawal = SavingWithdrawal.objects.filter(delete_status = False, date_created__year = year)

        loan_payment = LoanPayment.objects.filter(delete_status = False, date_created__year = year)
        loans_issued = LoansIssue.objects.filter(delete_status = False, date_created__year = year)
    else:
        shares_buy = ShareBuy.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
        shares_sell = ShareSell.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)

        savings_deposit = SavingDeposit.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
        savings_withdrawal = SavingWithdrawal.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)

        loan_payment = LoanPayment.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
        loans_issued = LoansIssue.objects.filter(delete_status = False, date_created__year = year,
                date_created__month = month)
        loan_payment_sum= loan_payment.aggregate(Sum('principal'))['principal__sum']
        loans_issued_sum = loans_issued.aggregate(Sum('principal'))['principal__sum']

    shares_buy_sum = shares_buy.aggregate(Sum('number'))['number__sum']
    shares_sell_sum = shares_sell.aggregate(Sum('number'))['number__sum']

    savings_deposit_sum = savings_deposit.aggregate(Sum('amount'))['amount__sum']
    savings_withdrawal_sum= savings_withdrawal.aggregate(Sum('amount'))['amount__sum']

    loan_payment_sum= loan_payment.aggregate(Sum('principal'))['principal__sum']
    loans_issued_sum = loans_issued.aggregate(Sum('principal'))['principal__sum']

    return {'shares_buy_sum': shares_buy_sum, 'shares_sell_sum': shares_sell_sum,
	'savings_deposit_sum': savings_deposit_sum, 'savings_withdrawal_sum':savings_withdrawal_sum,
	'loan_payment_sum': loan_payment_sum,'loans_issued_sum': loans_issued_sum,
  	 }



def capital(request):
    template = 'reports/capital.html'

    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        capital = _capital(year=year,month=month)
    else:
        capital = _capital()

    context = {
            'shares_buy_sum_capital': capital.get('shares_buy_sum','none'),
            'shares_sell_sum_capital': capital.get('shares_sell_sum','none'),
            'savings_deposit_sum_capital': capital.get('savings_deposit_sum','none'),
            'savings_withdrawal_sum_capital': capital.get('savings_withdrawal_sum','none'),
            'loan_payment_sum_capital': capital.get('loan_payment_sum','none'),
            'loans_issued_sum_capital': capital.get('loans_issued_sum','none'),
            'title_capital': 'Capital',
            }

    return render (request, template, context)

def monthly(request):
    template = 'reports/monthly.html'

    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        loan = _loan(year=year,month=month)
        capital = _capital(year=year,month=month)
        incomes = _income(year=year,month=month)
        expenses = _expense(year=year,month=month)
    else:
        loan = _loan()
        capital = _capital()
        incomes = _income()
        expenses = _expense()

    context = {
        'title_yearly': 'Monthly',
        'items_income': incomes,
        'title_income': 'Income',
        'items_expenses': expenses,
        'title_expenses': 'Expense',
        'items_loans': loan.get('loans_rec','none'),
        'issued_items_loans': loan.get('loans_issued','none'),
        'title_loans': 'Loans',
        'shares_buy_sum_capital': capital.get('shares_buy_sum','none'),
        'shares_sell_sum_capital': capital.get('shares_sell_sum','none'),
        'savings_deposit_sum_capital': capital.get('savings_deposit_sum','none'),
        'savings_withdrawal_sum_capital': capital.get('savings_withdrawal_sum','none'),
        'loan_payment_sum_capital': capital.get('loan_payment_sum','none'),
        'loans_issued_sum_capital': capital.get('loans_issued_sum','none'),
        'title_capital': 'Capital',
        }

    return render(request, template, context)


def yearly(request):
    template = 'reports/yearly.html'

    if request.method == 'POST':
        year = request.POST.get('year')
        loan = _loan(year=year,yearly=True)
        capital = _capital(year=year,yearly=True)
        incomes = _income(year=year,yearly=True)
        expenses = _expense(year=year,yearly=True)
    else:
        loan = _loan(yearly=True)
        capital = _capital(yearly=True)
        incomes = _income(yearly=True)
        expenses = _expense(yearly=True)

    context = {
        'title_yearly': 'Yearly',
        'items_income': incomes,
        'title_income': 'Income',
        'items_expenses': expenses,
        'title_expenses': 'Expense',
        'items_loans': loan.get('loans_rec','none'),
        'issued_items_loans': loan.get('loans_issued','none'),
        'title_loans': 'Loans',
        'shares_buy_sum_capital': capital.get('shares_buy_sum','none'),
        'shares_sell_sum_capital': capital.get('shares_sell_sum','none'),
        'savings_deposit_sum_capital': capital.get('savings_deposit_sum','none'),
        'savings_withdrawal_sum_capital': capital.get('savings_withdrawal_sum','none'),
        'loan_payment_sum_capital': capital.get('loan_payment_sum','none'),
        'loans_issued_sum_capital': capital.get('loans_issued_sum','none'),
        'title_capital': 'Capital',
        }

    return render(request, template, context)
