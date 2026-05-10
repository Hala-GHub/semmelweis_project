from django.db import models


class YearlyRecord(models.Model):
    year = models.IntegerField()
    births = models.IntegerField()
    deaths = models.IntegerField()
    clinic = models.CharField(max_length=20)

    class Meta:
        ordering = ["clinic", "year"]

    def __str__(self):
        return f"{self.clinic} - {self.year}"

    @property
    def proportion_deaths(self):
        if self.births:
            return round(self.deaths / self.births, 6)
        return 0


class MonthlyRecord(models.Model):
    date = models.DateField()
    births = models.IntegerField()
    deaths = models.IntegerField()

    HANDWASHING_START = "1847-06-01"

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return str(self.date)

    @property
    def proportion_deaths(self):
        if self.births:
            return round(self.deaths / self.births, 6)
        return 0