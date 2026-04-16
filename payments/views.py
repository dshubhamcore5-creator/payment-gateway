
from django.shortcuts import render
from django.conf import settings
from .models import Plan, Payment
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def create_order(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    order = client.order.create({"amount": plan.price, "currency": "INR"})
    Payment.objects.create(user=request.user, order_id=order["id"])
    return render(request, "checkout.html", {"order_id": order["id"], "key": settings.RAZORPAY_KEY_ID, "amount": plan.price})
