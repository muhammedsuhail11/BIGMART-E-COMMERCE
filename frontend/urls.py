from django.urls import path
from frontend import views
urlpatterns=[
    path('homepage1/',views.homepage1,name="homepage1"),
    path('viewaboutus/',views.viewaboutus,name="viewaboutus"),
    path('viewcontactus/',views.viewcontactus,name="viewcontactus"),
    path('categories/',views.categories,name="categories"),
    path('discategory/<itemcatg>',views.discategory,name="discategory"),
    path('proddetails/<int:dataid>',views.proddetails,name="proddetails"),
    path('registarction/',views.registarction,name="registarction"),
    path('saveregistration/',views.saveregistration,name="saveregistration"),
    path('displayloginpage/',views.displayloginpage,name="displayloginpage"),
    path('customerloginpg/',views.customerloginpg,name="customerloginpg"),
    path('logoutfront/',views.logoutfront,name="logoutfront"),
    path('contact/',views.contact,name="contact")
    ]