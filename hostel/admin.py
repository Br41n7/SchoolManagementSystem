from .models import Hostel, Room, HostelApplication
from django.contrib import admin


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ['name', 'fee']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hostel', 'number', 'capacity']


@admin.register(HostelApplication)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'hostel', 'status', 'payment_status']
    list_filter = ['status', 'payment_status']
