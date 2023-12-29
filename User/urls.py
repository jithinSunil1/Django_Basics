from django.urls import path
from  User import views
app_name="webuser"

urlpatterns = [

path('myprofile/',views.myprofile,name="myprofile"),
 
]
