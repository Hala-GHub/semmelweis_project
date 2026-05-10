import pandas as pd

from .models import (
    YearlyRecord,
    MonthlyRecord
)


def import_yearly_csv(csv_file):

    df = pd.read_csv(csv_file)

    for _, row in df.iterrows():

        YearlyRecord.objects.create(
            year=row["year"],
            births=row["births"],
            deaths=row["deaths"],
            clinic=row["clinic"]
        )


def import_monthly_csv(csv_file):

    df = pd.read_csv(csv_file)

    for _, row in df.iterrows():

        MonthlyRecord.objects.create(
            date=row["date"],
            births=row["births"],
            deaths=row["deaths"]
        )
        