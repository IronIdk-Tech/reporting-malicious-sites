from django.shortcuts import render
from .models import Report

def report_list(request):
    reports = Report.objects.all().order_by('-date_reported')
    context = {'reports': reports, 'total': reports.count()}
    return render(request, 'reports/report_list.html', context)
