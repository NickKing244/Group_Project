from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('register',views.register),
    path('main', views.main),
    path('login', views.login),
    path('logout', views.logout),
    path('details/<str:place_id>', views.bizdetails),
<<<<<<< HEAD
    path('search', views.search)
]
=======
    path('search', views.search),
    path('favorite/<str:place_id>', views.favorite),
    path('account', views.account),
    path('update', views.update),
]
>>>>>>> bbf3621e833ac7e602eaf8b50eefa17b1abb660b
