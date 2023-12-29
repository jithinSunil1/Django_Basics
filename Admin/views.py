from django.shortcuts import render,redirect
import firebase_admin 
from firebase_admin import firestore,credentials,storage,auth
import pyrebase


db=firestore.client()

# Create your views here.
def district(request):
    dis=db.collection("tbl_district").stream()
    dis_data=[]
    for i in dis:
        data=i.to_dict()
        dis_data.append({"dis":data,"id":i.id})
    if request.method=="POST":
        data={"district_name":request.POST.get("district")}
        db.collection("tbl_district").add(data)
        return redirect("webadmin:district")
    else:
        return render(request,"Main/District.html",{"district":dis_data})
    

def editdistrict(request,id):
    dis=db.collection("tbl_district").document(id).get().to_dict()
    if request.method=="POST":
       data={"district_name":request.POST.get("district")}
       db.collection("tbl_district").document(id).update(data)
       return redirect("webadmin:district")
    else:
        return render(request,"Main/District.html",{"dis_data":dis})


def deldistrict(request,id):
    db.collection("tbl_district").document(id).delete()
    return redirect("webadmin:district")


def place(request):
    dis=db.collection("tbl_district").stream()
    dis_data=[]
    for i in dis:
        data=i.to_dict()
        dis_data.append({"dis":data,"id":i.id})
    result=[]
    place_data=db.collection("tbl_place").stream()
    for place in place_data:
        place_dict=place.to_dict()
        district=db.collection("tbl_district").document(place_dict["district_id"]).get()
        district_dict=district.to_dict()
        result.append({'districtdata':district_dict,'place_data':place_dict,'placeid':place.id})
    if request.method=="POST":
        data={"place_name":request.POST.get("place"),"district_id":request.POST.get("district")}
        db.collection("tbl_place").add(data)
        return redirect("webadmin:place")
    else:
        return render(request,"Main/Place.html",{"place":result})
    
    
def editplace(request,id):
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for d in dis:
        dis_data.append({"dis":d.to_dict(),"id":d.id})
    place_data=db.collection("tbl_place").document(id).get().to_dict()
    if request.method=="POST":
       place_data={"place_name":request.POST.get("place"),"district_id":request.POST.get("district")}
       db.collection("tbl_place").document(id).update(place_data)
       return redirect("webadmin:place")
    else:
        return render(request,"Main/Place.html",{"place_data":place_data,"district":dis_data})
   

def delplace(request,id):
    place= db.collection("tbl_place").document(id).delete()
    return redirect("webadmin:place")



