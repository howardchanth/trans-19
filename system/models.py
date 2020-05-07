from django.db import models


# Create your models here.

class Patient(models.Model):
    caseID = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    IDnum = models.CharField(max_length=20, unique=True)
    DoB = models.DateField(null=True)
    DCC = models.DateField(null=True)

    def __str__(self):
        return f"{self.caseID} {self.name}"


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=200, blank=True)
    DISTRICT_CHOICES = [
        ("Islands", "Islands"),
        ("Kwai Tsing", "Kwai Tsing"),
        ("North", "North"),
        ("Sai Kung", "Sai Kung"),
        ("Sha Tin", "Sha Tin"),
        ("Tai Po", "Tai Po"),
        ("Tsuen Wan", "Tsuen Wan"),
        ("Tuen Mun", "Tuen Mun"),
        ("Yuen Long", "Yuen Long"),
        ("Kowloon City", "Kowloon City"),
        ("Kwun Tong", "Kwun Tong"),
        ("Sham Shui Po", "Sham Shui Po"),
        ("Wong Tai Sin", "Wong Tai Sin"),
        ("Yau Tsim Mong", "Yau Tsim Mong"),
        ("Central and Western", "Central and Western"),
        ("Eastern", "Eastern"),
        ("Southern", "Southern"),
        ("Wan Chai", "Wan Chai"),
    ]
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return self.name


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 blank=True, null=True)
    D_from = models.DateField(null=True)
    D_to = models.DateField(null=True)
    detail = models.CharField(max_length=500, blank=True)
    CATEGORY_CHOICES = [
        ("Residential", "Residential"),
        ("Workplace", "Workplace"),
        ("Visit", "Visit"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.patient.name}/{self.location.name}/{self.D_from} to {self.D_to}"
