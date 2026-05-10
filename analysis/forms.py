from django import forms

from .models import (
    YearlyRecord,
    MonthlyRecord
)


class YearlyRecordForm(forms.ModelForm):

    class Meta:

        model = YearlyRecord

        fields = [
            "year",
            "births",
            "deaths",
            "clinic",
        ]

        widgets = {

            "year": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full"
                }
            ),

            "births": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full"
                }
            ),

            "deaths": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full"
                }
            ),

            "clinic": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full"
                }
            ),
        }


class MonthlyRecordForm(forms.ModelForm):

    class Meta:

        model = MonthlyRecord

        fields = [
            "date",
            "births",
            "deaths",
        ]

        widgets = {

            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "input input-bordered w-full"
                }
            ),

            "births": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full"
                }
            ),

            "deaths": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full"
                }
            ),
        }


class CSVUploadForm(forms.Form):

    file = forms.FileField(

        widget=forms.FileInput(
            attrs={
                "class": "file-input file-input-bordered w-full"
            }
        )
    )