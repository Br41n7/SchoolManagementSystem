import uuid
from .models import FeeConfig


def generate_ref():
    return str(uuid.uuid4()).replace('-', '')[:12]


def get_fee_amount(purpose):
    fee = FeeConfig.objects.filter(purpose=purpose, active=True).first()
    return fee.amount
