from django.urls import path

from accounts import views

urlpatterns = [
    path('auth/', views.user_sign_in, name='sign-in'),
    path('auth/role', views.user_register, name='user-register'),
    path('account/logout/', views.sign_out, name='logout'),
]
