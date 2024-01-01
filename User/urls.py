from django.urls import path
from  User import views
app_name="webuser"

urlpatterns = [
path('homepage/',views.homepage,name="homepage"),
path('myprofile/',views.myprofile,name="myprofile"),
path('editprofile/',views.editprofile,name="editprofile"),
path('changepass/',views.changepass,name="changepass"),
]
