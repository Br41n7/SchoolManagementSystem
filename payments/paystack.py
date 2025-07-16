from django.conf import settings
import requests


def initialize_payment(email, amount, ref):
    url = f"{settings.PAYSTACK_BASE_URL}/transaction/initialize"
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "amount": int(amount * 100),  # Convert to kobo
        "reference": ref
    }
    res = requests.post(url, json=data, headers=headers)
    return res.json()


def verify_payment(ref):
    url = f"{settings.PAYSTACK_BASE_URL}/transaction/verify/{ref}"
    headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
    res = requests.get(url, headers=headers)
    return res.json()
