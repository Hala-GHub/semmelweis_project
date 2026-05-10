from django.urls import path
from . import views

app_name = "analysis"

urlpatterns = [

    # =========================
    # DASHBOARD
    # =========================

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    # =========================
    # YEARLY RECORDS
    # =========================

    path(
        "yearly/",
        views.yearly_list,
        name="yearly-list"
    ),

    path(
        "yearly/add/",
        views.yearly_create,
        name="yearly-create"
    ),

    path(
        "yearly/upload/",
        views.upload_yearly_csv,
        name="yearly-upload"
    ),

    path(
        "yearly/<int:pk>/edit/",
        views.yearly_update,
        name="yearly-update"
    ),

    path(
        "yearly/<int:pk>/delete/",
        views.yearly_delete,
        name="yearly-delete"
    ),

    # =========================
    # MONTHLY RECORDS
    # =========================

    path(
        "monthly/",
        views.monthly_list,
        name="monthly-list"
    ),

    path(
        "monthly/add/",
        views.monthly_create,
        name="monthly-create"
    ),
]