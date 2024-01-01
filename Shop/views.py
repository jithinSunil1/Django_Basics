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
    shop = db.collection("tbl_shop").document(request.session["sid"]).get().to_dict()

    return render(request,"Shop/Homepage.html")
# Create your views here.


def Myprofile (request):
    shop = db.collection("tbl_shop").document(request.session["sid"]).get().to_dict()

    return render(request,"Shop/Myprofile.html",{"shop":shop})



def editprofile (request):
    shop = db.collection("tbl_shop").document(request.session["sid"]).get().to_dict()
    if request.method=="POST":
      data={"shop_name":request.POST.get("name"),"shop_contact":request.POST.get("contact"),"shop_address":request.POST.get("address")}
      db.collection("tbl_shop").document(request.session["sid"]).update(data)
      return redirect("webshop:Myprofile")
    else:
      return render(request,"Shop/Editprofile.html",{"shop":shop})
    
def changepass(request):
  shop = db.collection("tbl_shop").document(request.session["sid"]).get().to_dict()
  email = shop["shop_email"]
  password_link = firebase_admin.auth.generate_password_reset_link(email) 
  send_mail(
    'Reset your password ', #subject
    "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + password_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
    settings.EMAIL_HOST_USER,
    [email],
  )
  return render(request,"Shop/Homepage.html",{"msg":email})


# Create your views here.
