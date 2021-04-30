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
    path('features-list/shop/mobile/buy-now', views.purchase, name='purchase'),
    path('features-list/shop/mobile/buy-now/buy', views.buy_now, name='buy'),
    path('features-list/insurance/file-new-claim', views.file_claim, name='file-claim'),
    path('features-list/insurance/view-claim', views.view_claim, name='view_claim'),
]
