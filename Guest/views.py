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

def userreg(request):
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for d in dis:
        dis_data.append({"dis":d.to_dict(),"id":d.id})
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("Password")
        try:
            user = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Guest/Userreg.html",{"msg":error})
        image = request.FILES.get("photo")
        if image:
            path = "UserPhoto/" + image.name
            st.child(path).put(image)
            d_url = st.child(path).get_url(None)

        db.collection("tbl_user").add({"user_id":user.uid,"user_name":request.POST.get("name"),"user_contact":request.POST.get("Contact"),"user_email":request.POST.get("email"),"user_address":request.POST.get("address"),"place_id":request.POST.get("sel_place"),"user_photo":d_url})
        return render(request,"Guest/Userreg.html")
    else:
        return render(request,"Guest/Userreg.html",{"district":dis_data})
# Create your views here.

def ajaxplace(request):
    place = db.collection("tbl_place").where("district_id", "==", request.GET.get("did")).stream()
    place_data = []
    for p in place:
        place_data.append({"place":p.to_dict(),"id":p.id})
    return render(request,"Guest/AjaxPlace.html",{"place":place_data})

def shopreg(request):
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for d in dis:
        dis_data.append({"dis":d.to_dict(),"id":d.id})
    image = request.FILES.get("Photo")
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            shop = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Guest/Shopreg.html",{"msg":error})
        image = request.FILES.get("photo")
    if image:
        path = "ShopPhoto/" + image.name
        st.child(path).put(image)
        d_url = st.child(path).get_url(None) 
    proof = request.FILES.get("proof")
    if proof:
        path = "ShopProof/" + proof.name
        st.child(path).put(proof)
        p_url = st.child(path).get_url(None)  
        db.collection("tbl_shop").add({"shop_id":shop.uid,"shop_name":request.POST.get("name"),"shop_contact":request.POST.get("contact"),"shop_email":request.POST.get("email"),"shop_address":request.POST.get("address"),"place_id":request.POST.get("sel_place"),"shop_photo":d_url,"shop_proof":p_url})
    return render(request,"Guest/Shopreg.html",{"district":dis_data})

def loginpage(request):
    userid = ""
    shopid = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            data = authe.sign_in_with_email_and_password(email,password)
        except:
            return render(request,"Guest/Loginpage.html",{"msg":"Error in Email Or Password"})
        user = db.collection("tbl_user").where("user_id", "==", data["localId"]).stream()
        for u in user:
            userid = u.id
        shop= db.collection("tbl_shop").where("shop_id","==",data["localId"]).stream()    
        for s in shop:
            shopid = s.id
        if userid:
            request.session["uid"] = userid
            return redirect("webuser:homepage")
        elif shopid:
            request.session["sid"] = shopid
            return redirect("webshop:homepage")
        else:
            return render(request,"Guest/Loginpage.html",{"msg":"error"})
    else:
        return render(request,"Guest/Loginpage.html")
