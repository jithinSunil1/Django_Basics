from django.shortcuts import render,redirect
import firebase_admin 
from firebase_admin import firestore,credentials,storage,auth
import pyrebase

db=firestore.client()

config = {
  "apiKey": "AIzaSyACsnzsDlV_CNGJHIJNK86BgUwfv1unCvM",
  "authDomain": "mainproject-bc028.firebaseapp.com",
  "projectId": "mainproject-bc028",
  "storageBucket": "mainproject-bc028.appspot.com",
  "messagingSenderId": "20625920499",
  "appId": "1:20625920499:web:9f7452ac379b5990fe4286",
  "measurementId": "G-C55K2C0X8H",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
st = firebase.storage()

def myprofile(request):
    return render(request,"User/Myprofile.html")

# Create your views here.
