from .models import Payment, FeeConfig
from django.contrib import admin


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'amount', 'purpose',
                    'status', 'payment_method', 'created_at']
    list_filter = ['status', 'purpose', 'payment_method']
    search_fields = ['student__username', 'ref_id']


@admin.register(FeeConfig)
class FeeConfigAdmin(admin.ModelAdmin):
    list_display = ('label', 'purpose', 'amount', 'active')
    list_editable = ('amount', 'active')
    search_fields = ['purpose', 'label']
