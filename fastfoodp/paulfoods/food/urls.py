from django.urls import path
from . import views
from .views import profile
from .views import detailsv
from django.contrib.auth import views as auth_views
from .views import ver_carrito_y_pagar
from .views import  procesar_pago
from .views import  process_payment
from .views import  payment_processp



app_name = 'food'
urlpatterns =[


    # Otras URLs de tu aplicación
path('editar_usuario/<int:user_id>/',views. edit_user, name='editar_usuario'),
path ('actividad', views.chicken, name=('actividad')),
path ('burger', views.burger, name=('burger')),
path ('drink', views.drink, name=('drink')),
path ('contact', views.contact, name=('contact')),
path ('steak', views.steak, name=('steak')),
path ('perfil', views.pizza, name=('perfil')),
path ('order', views.order, name=('order')),
path ('succes', views.succes, name=('succes')),
path ('signup', views.signup, name=('signup')),
path ('login/', views.logIn, name=('login')),
path ('logout', views.logOut, name=('logout')),
path('perfil', profile, name='profile'),
path('details/<int:chicken_id>/', views.detailsv, name=('details')),
path('login/', auth_views.LoginView.as_view(), name='login'),
path('agregar_al_carrito/<int:chicken_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
path ('ver_carrito_y_pagar/',views.ver_carrito_y_pagar, name=('ver_carrito_y_pagar')),
path('procesar-pago/', procesar_pago, name='procesar_pago'),
path('process-payment/', process_payment, name='process_payment'),
path('payment_processp/', views.payment_processp, name='payment_processp'),
path('checkoutp/<int:product_id>/', views.CheckOutp, name='checkoutp'),
    path('payment-success/<int:product_id>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:product_id>/', views.paymentFailed, name='payment-failed'),
path ('ver_carrito_y_pagarp/',views.ver_carrito_y_pagarp, name=('ver_carrito_y_pagarp')),
 path('add_review/', views.add_review, name='add_review'),
 path ('tarjeta', views.tarjeta, name=('tarjeta')),
  path('paypal/', views.paymen, name='paymen'),
     path('checkout/', views.payment_checkout, name='checkout_payment'),

    path('execute_payment', views.execute_payment, name='execute_payment'),
    path('payment_failed', views.payment_failed, name='payment_failed'),
 path ('ordenes/',views.ver_detalles_carrito, name=('ordenes')),




]
