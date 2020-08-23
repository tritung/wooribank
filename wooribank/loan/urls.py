'''
Created on Aug 23, 2020

@author: autonomous
'''
from django.urls.conf import path
from wooribank.loan import views

urlpatterns=[
    path('sale/', views.sale, name='sale'),
    path('new', views.new_loan, name='new_loan'),
    path('save', views.create_or_update, name='create_or_update'),
]