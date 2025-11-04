from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Payment
from django import forms
from django.urls import reverse
from django.db.models import Sum

# Simple form for payments (we use in template)
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount', 'method', 'note', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

def home(request):
    # show dashboard quick stats
    total_students = Student.objects.count()
    total_fee = Student.objects.aggregate(total=Sum('total_fee'))['total'] or 0
    total_paid = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    total_due = float(total_fee) - float(total_paid)
    context = {
        'total_students': total_students,
        'total_fee': total_fee,
        'total_paid': total_paid,
        'total_due': total_due
    }
    return render(request, 'home.html', context)

def students(request):
    data = Student.objects.all().order_by('roll_no')
    return render(request, 'students.html', {'students': data})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    payments = student.payments.all().order_by('-date')
    return render(request, 'student_detail.html', {'student': student, 'payments': payments})

def payments(request):
    data = Payment.objects.all().order_by('-date')
    return render(request, 'payments.html', {'payments': data})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect(reverse('receipt', args=[payment.pk]))
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form})

def receipt(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'receipt.html', {'payment': payment})

def stats(request):
    total_fee = Student.objects.aggregate(total=Sum('total_fee'))['total'] or 0
    total_paid = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'stats.html', {
        'total_fee': total_fee,
        'total_paid': total_paid,
        'total_due': float(total_fee) - float(total_paid)
    })

