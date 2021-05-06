from django.shortcuts import render

# Create your views here.
from accounts.models import User
from shop.models import *


def features(request):
    return render(request, '../templates/shop/features.html')


def insurance(request):
    insurances_smartphones = Purchase.objects.all()
    insurances_laptops = PurchaseLaptop.objects.all()
    insurances_automobile = PurchaseAutomobile.objects.all()
    i = {'insurances_smartphones': insurances_smartphones, 'insurance_laptops': insurances_laptops,
         'insurance_automobiles': insurances_automobile}
    return render(request, 'shop/insurance.html', i)


def shop(request):
    return render(request, 'shop/shop.html')


def repair(request):
    claim_smartphones = Claim.objects.all()
    claim_laptops = ClaimLaptop.objects.all()
    claim_automobiles = ClaimAutomobile.objects.all()

    c = {'claim_smartphones': claim_smartphones, 'claim_laptops': claim_laptops,
         'claim_automobiles': claim_automobiles}

    return render(request, 'shop/repair.html', c)


def police(request):
    claim_smartphones = Claim.objects.all()
    claim_laptops = ClaimLaptop.objects.all()
    claim_automobiles = ClaimAutomobile.objects.all()

    c = {'claim_smartphones': claim_smartphones, 'claim_laptops': claim_laptops,
         'claim_automobiles': claim_automobiles}

    return render(request, 'shop/police.html', c)


def auto_mobile(request):
    automobiles = Automobile.objects.all()
    s = {'automobiles': automobiles}
    return render(request, 'shop/auto-mobile-shop.html', s)


def mobile(request):
    smartphones = Smartphone.objects.all()
    s = {'smartphones': smartphones}
    return render(request, 'shop/mobile-shop.html', s)


def laptop(request):
    laptops = Laptop.objects.all()
    l = {'laptops': laptops}
    return render(request, 'shop/laptop-shop.html', l)


def purchase(request):
    p = request.POST.get('snumber')
    smartphones = Smartphone.objects.get(serial_number=p)
    insurance_price = round((smartphones.price * 30) / 100, 2)
    s = {'smartphones': smartphones, 'insurance_price': insurance_price}
    return render(request, 'shop/purchase-mobile.html', s)


def purchase_laptop(request):
    p = request.POST.get('snumber')
    laptop = Laptop.objects.get(serial_number=p)
    insurance_price = round((laptop.price * 30) / 100, 2)
    l = {'laptop': laptop, 'insurance_price': insurance_price}
    return render(request, 'shop/purchase-laptop.html', l)


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


def buy_now_laptop(request):
    serial_number = request.POST.get('serial-number')
    laptop = Laptop.objects.get(serial_number=serial_number)
    username = request.user.username
    u = User.objects.filter(username=username).first()

    try:
        PurchaseLaptop.objects.create(username=u, serial_number=laptop)
        error = "no"
    except:
        error = "yes"

    x = {'error': error}
    return render(request, 'shop/purchase-laptop.html', x)


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


def purchase_automobile(request):
    p = request.POST.get('snumber')
    automobile = Automobile.objects.get(serial_number=p)
    insurance_price = round((automobile.price * 30) / 100, 2)
    l = {'automobile': automobile, 'insurance_price': insurance_price}
    return render(request, 'shop/purchase-automobile.html', l)


def buy_now_automobile(request):
    serial_number = request.POST.get('serial-number')
    automobile = Automobile.objects.get(serial_number=serial_number)
    username = request.user.username
    u = User.objects.filter(username=username).first()

    try:
        PurchaseAutomobile.objects.create(username=u, serial_number=automobile)
        error = "no"
    except:
        error = "yes"

    x = {'error': error}
    return render(request, 'shop/purchase-automobile.html', x)


def file_claim_laptop(request):
    error = "no"
    purchase_id = request.POST.get('purchase-id')

    my_id = request.POST.get('myid')
    subject = request.POST.get('subject')
    theft = request.POST.get('theft')
    message = request.POST.get('message')
    try:
        form_owner = PurchaseLaptop.objects.get(id=my_id)
        ClaimLaptop.objects.create(owner=form_owner, subject=subject, theft=theft, message=message)
        error = "no"
    except:
        error = "yes"
    x = {'error': error, 'purchased_id': purchase_id}
    return render(request, 'insurance/file-new-claim.html', x)


def view_claim_laptop(request):
    purchase_id = request.POST.get('purchase-id')
    purchase_id = int(purchase_id)
    claims = ClaimLaptop.objects.all()
    x = {'claims': claims, 'purchase_id': purchase_id}
    return render(request, 'insurance/view-claim-laptop.html', x)


def file_claim_automobile(request):
    error = "no"
    purchase_id = request.POST.get('purchase-id')

    my_id = request.POST.get('myid')
    subject = request.POST.get('subject')
    theft = request.POST.get('theft')
    message = request.POST.get('message')
    try:
        form_owner = PurchaseAutomobile.objects.get(id=my_id)
        ClaimAutomobile.objects.create(owner=form_owner, subject=subject, theft=theft, message=message)
        error = "no"
    except:
        error = "yes"
    x = {'error': error, 'purchased_id': purchase_id}
    return render(request, 'insurance/file-new-claim.html', x)


def view_claim_automobile(request):
    purchase_id = request.POST.get('purchase-id')
    purchase_id = int(purchase_id)
    claims = ClaimAutomobile.objects.all()
    x = {'claims': claims, 'purchase_id': purchase_id}
    return render(request, 'insurance/view-claim-automobile.html', x)
