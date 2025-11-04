from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def total_paid(self):
        return sum(p.amount for p in self.payments.all())

    def balance_due(self):
        return float(self.total_fee) - float(self.total_paid())

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI'),
        ('Other', 'Other'),
    ]

    student = models.ForeignKey(Student, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='Cash')
    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.amount} on {self.date}"

