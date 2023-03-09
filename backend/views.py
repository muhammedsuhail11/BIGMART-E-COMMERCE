from django.contrib.messages.storage import session
from django.shortcuts import render,redirect
# Create your views here.
from backend.models import admindb, categordb, prodetails,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def viewindex(req):
    return render(req,"index.html")
def viewadmin(req):
    return  render(req,"addadmin.html")
def saveadmin(req):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        num = req.POST.get('number')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        img = req.FILES['image']
        obj = admindb(NAME=na, EMAIL=email, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=img )
        obj.save()
        return redirect(viewadmin)
def displayadmin(req):
    data = admindb.objects.all()
    return render(req,"displayadmin.html", {'data':data})

def editadminpage(req,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html", {'data':data})
def updateadmin(req,dataid):
    if req.method == "post":
        na = req.POST.get('name')
        email = req.POST.get('email')
        num = req.POST.get('number')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).IMAGE
        admindb.objects.filter(id=dataid).update(NAME=na, EMAIL=email, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=file)
        return redirect(displayadmin)

def deleteadmin(req,dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)
def addcategory(req):
    return render(req,"addcategory.html")
def savecategory(req):
    if req.method == "POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        img = req.FILES['image']
        obj =categordb(NAME=na, DISCRIPTION=dis, IMAGE=img)
        obj.save()
        return redirect(addcategory)
def displaycategoryfn(req):
    data = categordb.objects.all()
    return render(req,"displaycategory.html",{'data':data})

def editcategory(req,dataid):
    data = categordb.objects.get(id=dataid)
    print(data)
    return render(req,"editcategory.html",{'data':data})
def updatecategory(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categordb.objects.get(id=dataid).IMAGE
        categordb.objects.filter(id=dataid).update(NAME=na, DISCRIPTION=dis, IMAGE=file)
        return redirect(displaycategoryfn)
def deletecategory(req,dataid):
    data = categordb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategoryfn)
def productdetails(req):
    da = categordb.objects.all()
    return render(req,"addproduct.html",{'da':da})
def saveproductdetails(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ca= req.POST.get('category')
        pri= req.POST.get('price')
        qunty= req.POST.get('quantity')
        dis = req.POST.get('description')
        img = req.FILES['image']
        obj =prodetails(Category=ca,NAME=na,DESCRIPTION=dis,IMAGE=img,PRICE=pri,QUNTITY=qunty)
        obj.save()
        return redirect(productdetails)

def displayproduct(req):
        data = prodetails.objects.all()
        return render(req,"displayproduct.html",{'data':data})
def editproductpage(req,dataid):
    data = prodetails.objects.get(id=dataid)
    da = categordb.objects.all()
    print(data)
    print(da)
    return render(req,"editproduct.html", {'datas':data,'da':da})
def updateproduct(req,dataid):
    if req.method == "POST":
        ca = req.POST.get('category')
        na = req.POST.get('name')
        pri = req.POST.get('prize')
        qunty = req.POST.get('quantity')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = prodetails.objects.get(id=dataid).IMAGE
        prodetails.objects.filter(id=dataid).update(Category=ca,NAME=na,PRICE=pri,QUNTITY=qunty, DESCRIPTION=dis, IMAGE=file)
        return redirect(displayproduct)


def deleteproduct(req,dataid):
    data = prodetails.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)
def loginpagee(req):
    return render(req,"loginpage.html")
def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(viewindex)
            else:
                return redirect(viewindex)
        else:
            return redirect(loginpagee)

def adminlogut(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpagee)
def displaycomplaint(req):
    data = contactdb.objects.all()
    return render(req, "displaycomplaint.html", {'data': data})
def deletecomplaint(req,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycomplaint)


