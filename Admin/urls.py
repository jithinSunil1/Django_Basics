from django.urls import path
from Admin import views
app_name="webadmin"

urlpatterns = [
        path('District/',views.district,name="district"),
        path('Place/',views.place,name="place"),
        path('editdistrict/<str:id>',views.editdistrict,name="editdistrict"),
        path('deldistrict/<str:id>',views.deldistrict,name="deldistrict"),
        path('delplace/<str:id>',views.delplace,name="delplace"),
        path('editplace/<str:id>',views.editplace,name="editplace"),
]

    
    

