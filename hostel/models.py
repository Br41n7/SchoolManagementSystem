from django.conf import settings
from django.db import models


class Hostel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.name


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    current_occupants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True)

    def is_full(self):
        return self.current_occupants.count() >= self.capacity

    def _str_(self):
        return f"{self.hostel.name} - Room {self.number}"


class HostelApplication(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[(
        'pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')])
    payment_status = models.CharField(max_length=10, default='unpaid')

    def _str_(self):
        return f"{self.student.username} - {self.hostel.name}"
