from django.urls import path

from shop import views

urlpatterns = [
    path('features-list/', views.features, name='features'),
    path('features-list/Insurance', views.insurance, name='insurance'),
    path('features-list/shop', views.shop, name='shop'),
    path('features-list/repair', views.repair, name='repair'),
    path('features-list/police-help', views.police, name='police'),

    path('features-list/shop/auto-mobile', views.auto_mobile, name='auto-mobile-shop'),
    path('features-list/shop/mobile', views.mobile, name='mobile-shop'),
    path('features-list/shop/laptop', views.laptop, name='laptop-shop'),

    path('features-list/shop/mobile/buy-now/smartphones', views.purchase, name='purchase'),
    path('features-list/shop/mobile/buy-now/laptops', views.purchase_laptop, name='purchase-laptop'),
    path('features-list/shop/mobile/buy-now/automobiles', views.purchase_automobile, name='purchase-automobile'),

    path('features-list/shop/mobile/buy-now/buy/smartphones', views.buy_now, name='buy'),
    path('features-list/shop/mobile/buy-now/buy/laptop', views.buy_now_laptop, name='buy-laptop'),
    path('features-list/shop/mobile/buy-now/buy/automobile', views.buy_now_automobile, name='buy-automobile'),

    path('features-list/insurance/file-new-claim/smartphone', views.file_claim, name='file-claim'),
    path('features-list/insurance/view-claim/smartphone', views.view_claim, name='view_claim'),

    path('features-list/insurance/file-new-claim/laptop', views.file_claim_laptop, name='file-claim-laptop'),
    path('features-list/insurance/view-claim/laptop', views.view_claim_laptop, name='view_claim-laptop'),

    path('features-list/insurance/file-new-claim/automobile', views.file_claim_automobile, name='file-claim-automobile'),
    path('features-list/insurance/view-claim/automobile', views.view_claim_automobile, name='view_claim-automobile'),
]
