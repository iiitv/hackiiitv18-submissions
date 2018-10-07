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
    apiKey: "",
    authDomain: "",
    databaseURL: "",
    projectId: "",
    storageBucket: "",
    messagingSenderId: ""
  }

firebase = pyrebase.initialize_app(config)
