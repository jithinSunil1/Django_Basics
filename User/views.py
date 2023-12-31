from django.shortcuts import render,redirect
import firebase_admin 
from firebase_admin import firestore,credentials,storage,auth
import pyrebase
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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

def homepage(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    return render(request,"User/Homepage.html",{"user":user})

def myprofile(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    return render(request,"User/Myprofile.html",{"user":user})
def editprofile(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    if request.method=="POST":
      data={"user_name":request.POST.get("name"),"user_contact":request.POST.get("contact"),"user_address":request.POST.get("address")}
      db.collection("tbl_user").document(request.session["uid"]).update(data)
      return redirect("webuser:myprofile")
    else:
      return render(request,"User/Editprofile.html",{"user":user})

  
def changepass(request):
  user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
  email = user["user_email"]
  password_link = firebase_admin.auth.generate_password_reset_link(email) 
  send_mail(
    'Reset your password ', #subject
    "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + password_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
    settings.EMAIL_HOST_USER,
    [email],
  )
  return render(request,"User/Homepage.html",{"msg":email})
