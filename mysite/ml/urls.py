#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 06:37:46 2020

@author: Alaa
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]