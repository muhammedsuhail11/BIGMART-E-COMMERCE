from django.shortcuts import render,redirect
from backend.models import categordb,contactdb
from backend.models import prodetails
from frontend.models import registrationdb
from django.contrib import messages



# Create your views here.
def homepage1(req):
    data=categordb.objects.all()
    return render(req,"home.html",{'data':data})
def viewaboutus(req):
    return render(req,"aboutus.html")
def viewcontactus(req):
    return render(req,"contact.html")
def categories(req):
    return render(req,"categorydisplay.html")

def discategory(req,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = prodetails.objects.filter(Category=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(req,"categorydisplay.html",context)

def proddetails(req,dataid):
    data=prodetails.objects.get(id=dataid)
    return render(req,"singleproduct.html",{'dat':data})
def registarction(req):
    return render(req,"registarction.html")
def saveregistration(req):
    if req.method == "POST":
        na = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('pass1')
        cmfpass = req.POST.get('pass2')
        obj = registrationdb(Name=na, Email=email, Password=password, Conformpassword=cmfpass)
        obj.save()
        messages.success(req,"rRegistered")
        return redirect(registarction)
    else:

        return render(req,'')
def displayloginpage(req):
    return render(req,"registarction.html")
def customerloginpg(req):
    if req.method=='POST':
        username_r=req.POST.get("username1")
        password_r=req.POST.get("password1")
        if registrationdb.objects.filter(Name=username_r,Password=password_r).exists():
            req.session['username1']=username_r
            req.session['password1']=password_r
            messages.success(req, "lgined successfully")
            return redirect(homepage1)
        else:
            messages.error(req, "Error")
            return render(req,'registarction.html',{'msg':"sorry.....invalid username or password"})

def logoutfront(req):
   del req.session['username1']
   del req.session['password1']
   return redirect(registarction)
def contact(req):
    if req.method == "POST":
        na = req.POST.get('NAME')
        email = req.POST.get('EMAIL')
        sub = req.POST.get('SUBJECT')
        msg = req.POST.get('MESSAGE')
        obj = contactdb(Name=na, Email=email, Subject=sub, Message=msg)
        obj.save()
        return redirect(viewcontactus)




