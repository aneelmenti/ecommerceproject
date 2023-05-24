from django.urls import path
from . import views
from django.urls import path
app_name = 'registration'
urlpatterns = [
    path('reg', views.reg,name='reg'),
    path('otpvalidation',views.otpvalidation),
    path('login/',views.login),
    path('my_logout/',views.my_logout),
    path('cart/', views.cart, name='cart'),
    path('addcart/', views.addcart, name='addcart'),
    path('insertcart/', views.insertcart, name='insertcart'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('deletecart/', views.deletecart, name='deletecart'),
    path('modifycart/', views.modifycart, name='modifycart'),
    path('modifiedcart/', views.modifiedcart, name='modifiedcart'),
    path('track/', views.track, name='track'),
    path('cancel/',views.cancel, name='cancel'),
]