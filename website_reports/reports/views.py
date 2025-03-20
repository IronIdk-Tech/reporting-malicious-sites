from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm

def report_list(request):
    reports = Report.objects.all().order_by('-date_reported')
    context = {'reports': reports, 'total': reports.count()}
    return render(request, 'reports/report_list.html', context)

def add_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')  # Redirect to the report list after saving
    else:
        form = ReportForm()
    return render(request, 'reports/add_report.html', {'form': form})
