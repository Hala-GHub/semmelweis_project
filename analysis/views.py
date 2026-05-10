import json

from django.shortcuts import render, redirect

from .models import (
    YearlyRecord,
    MonthlyRecord
)

from .forms import (
    YearlyRecordForm,
    MonthlyRecordForm,
    CSVUploadForm
)

from .services import import_yearly_csv


def dashboard(request):

    return render(
        request,
        "analysis/dashboard.html"
    )


# =========================
# YEARLY RECORDS
# =========================

def yearly_list(request):

    records = YearlyRecord.objects.all()

    labels = []
    clinic1 = []
    clinic2 = []

    for record in records:

        if record.year not in labels:
            labels.append(record.year)

    for year in labels:

        c1 = YearlyRecord.objects.filter(
            year=year,
            clinic="clinic 1"
        ).first()

        c2 = YearlyRecord.objects.filter(
            year=year,
            clinic="clinic 2"
        ).first()

        clinic1.append(
            c1.proportion_deaths if c1 else 0
        )

        clinic2.append(
            c2.proportion_deaths if c2 else 0
        )

    chart_data = {
        "labels": labels,
        "clinic1": clinic1,
        "clinic2": clinic2,
    }

    context = {
        "records": records,
        "chart_data": json.dumps(chart_data)
    }

    return render(
        request,
        "analysis/yearly_list.html",
        context
    )


def yearly_create(request):

    if request.method == "POST":

        form = YearlyRecordForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("analysis:yearly-list")

    else:

        form = YearlyRecordForm()

    context = {
        "form": form
    }

    return render(
        request,
        "analysis/yearly_form.html",
        context
    )


def yearly_update(request, pk):

    record = YearlyRecord.objects.get(pk=pk)

    if request.method == "POST":

        form = YearlyRecordForm(
            request.POST,
            instance=record
        )

        if form.is_valid():

            form.save()

            return redirect("analysis:yearly-list")

    else:

        form = YearlyRecordForm(
            instance=record
        )

    context = {
        "form": form
    }

    return render(
        request,
        "analysis/yearly_form.html",
        context
    )


def yearly_delete(request, pk):

    record = YearlyRecord.objects.get(pk=pk)

    if request.method == "POST":

        record.delete()

        return redirect("analysis:yearly-list")

    context = {
        "record": record
    }

    return render(
        request,
        "analysis/yearly_confirm_delete.html",
        context
    )


def upload_yearly_csv(request):

    if request.method == "POST":

        form = CSVUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            csv_file = request.FILES["file"]

            import_yearly_csv(csv_file)

            return redirect("analysis:yearly-list")

    else:

        form = CSVUploadForm()

    context = {
        "form": form
    }

    return render(
        request,
        "analysis/upload_csv.html",
        context
    )


# =========================
# MONTHLY RECORDS
# =========================

def monthly_list(request):

    records = MonthlyRecord.objects.all()

    labels = []
    deaths = []

    for record in records:

        labels.append(
            record.date.strftime("%Y-%m")
        )

        deaths.append(
            record.proportion_deaths
        )

    chart_data = {
        "labels": labels,
        "deaths": deaths,
    }

    context = {
        "records": records,
        "chart_data": json.dumps(chart_data)
    }

    return render(
        request,
        "analysis/monthly_list.html",
        context
    )


def monthly_create(request):

    if request.method == "POST":

        form = MonthlyRecordForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("analysis:monthly-list")

    else:

        form = MonthlyRecordForm()

    context = {
        "form": form
    }

    return render(
        request,
        "analysis/monthly_form.html",
        context
    )