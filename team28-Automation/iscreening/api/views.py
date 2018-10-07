from django.shortcuts import render
import pyrebase 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate

config = {
    apiKey: "AIzaSyCOpasPOo620XMm0-JCVnllJSwJ4v4WVkE",
    authDomain: "int-screening.firebaseapp.com",
    databaseURL: "https://int-screening.firebaseio.com",
    projectId: "int-screening",
    storageBucket: "int-screening.appspot.com",
    messagingSenderId: "691103875926"
  }

firebase = pyrebase.initialize_app(config)
