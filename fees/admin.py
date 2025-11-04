from django.contrib import admin
from .models import Student, Payment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','roll_no','course','total_fee')
    search_fields = ('name','roll_no','course')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student','amount','date','method')
    list_filter = ('method','date')
    search_fields = ('student__name','student__roll_no')
