from django.contrib import admin
from .models import YearlyRecord, MonthlyRecord


admin.site.register(YearlyRecord)
admin.site.register(MonthlyRecord)