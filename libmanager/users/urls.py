from django.urls import path
from users import views

urlpatterns = [
    path('', views.UserHome.as_view(), name='users'),
    path('<int:user_id>/', views.get_profile, name="getprofile"),
    path('add/', views.adduser, name="adduser"),
    path('del/', views.deluser, name="deluser"),
    path('find/', views.finduser, name="finduser"),
    path('debtors/', views.finduser, name="debtors"),

]