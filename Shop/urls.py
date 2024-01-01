from django.urls import path
from Shop import views
app_name="webshop"

urlpatterns = [

    path("homepage/",views.homepage,name="homepage"),
    path("Myprofile/",views.Myprofile,name="Myprofile"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path('changepass/',views.changepass,name="changepass"),


]