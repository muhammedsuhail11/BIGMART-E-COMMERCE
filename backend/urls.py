from django.urls import path
from backend import views
urlpatterns=[
    path('viewindex/', views.viewindex, name="viewindex"),
    path('viewadmin/', views.viewadmin, name="viewadmin"),
    path('saveadmin/', views.saveadmin, name="saveadmin"),
    path('displayadmin/', views.displayadmin, name="displayadmin"),
    path('editadminpage/<int:dataid>/', views.editadminpage, name="editadminpage"),
    path('updateadmin/<int:dataid>/',views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),

    path('addcategory/',views.addcategory, name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategoryfn/', views.displaycategoryfn, name="displaycategoryfn"),
    path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory, name="deletecategory"),
    path('displaycomplaint/',views.displaycomplaint,name="displaycomplaint"),
    path('deletecomplaint/<int:dataid>/', views.deletecomplaint, name="deletecomplaint"),






    path('productdetails/',views.productdetails,name="productdetails"),
    path('saveproductdetails/', views.saveproductdetails, name="saveproductdetails"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproductpage/<int:dataid>/',views.editproductpage, name="editproductpage"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),

    path('loginpagee/', views.loginpagee, name="loginpagee"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/',views.adminlogut, name="adminlogout")




]