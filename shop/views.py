from django.shortcuts import render

# Create your views here.
from accounts.models import User
from shop.models import Smartphone, Purchase, Claim


def features(request):
    return render(request, '../templates/shop/features.html')


def insurance(request):
    insurances = Purchase.objects.all()
    i = {'insurances': insurances}
    return render(request, 'shop/insurance.html', i)


def shop(request):
    return render(request, 'shop/shop.html')


def repair(request):
    return render(request, 'shop/repair.html')


def police(request):
    return render(request, 'shop/police.html')


def auto_mobile(request):
    return render(request, 'shop/auto-mobile-shop.html')


def mobile(request):
    smartphones = Smartphone.objects.all()
    s = {'smartphones': smartphones}
    return render(request, 'shop/mobile-shop.html', s)


def laptop(request):
    return render(request, 'shop/laptop-shop.html')


def purchase(request):
    p = request.POST.get('snumber')
    smartphones = Smartphone.objects.get(serial_number=p)
    insurance_price = round((smartphones.price * 30) / 100, 2)
    s = {'smartphones': smartphones, 'insurance_price': insurance_price}
    return render(request, 'shop/purchase-mobile.html', s)


def buy_now(request):
    serial_number = request.POST.get('serial-number')
    smartphone = Smartphone.objects.get(serial_number=serial_number)
    username = request.user.username
    u = User.objects.filter(username=username).first()

    try:
        Purchase.objects.create(username=u, serial_number=smartphone)
        error = "no"
    except:
        error = "yes"

    x = {'error': error}
    return render(request, 'shop/purchase-mobile.html', x)


def file_claim(request):
    error = "no"
    purchase_id = request.POST.get('purchase-id')

    my_id = request.POST.get('myid')
    subject = request.POST.get('subject')
    theft = request.POST.get('theft')
    message = request.POST.get('message')
    try:
        form_owner = Purchase.objects.get(id=my_id)
        Claim.objects.create(owner=form_owner, subject=subject, theft=theft, message=message)
        error = "no"
    except:
        error = "yes"
    x = {'error': error, 'purchased_id': purchase_id}
    return render(request, 'insurance/file-new-claim.html', x)


def view_claim(request):
    purchase_id = request.POST.get('purchase-id')
    purchase_id = int(purchase_id)
    claims = Claim.objects.all()
    x = {'claims': claims, 'purchase_id': purchase_id}
    return render(request, 'insurance/view-claim.html', x)