from django.shortcuts import render,HttpResponse,redirect

from django.views import View

from app1.models import Product,Demo

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

# Create your views here.


def homepage(request,name):

    return HttpResponse("<h4> Welcome "+name+" </h4>")


class Demo1(View):

    def get(self,request):

        return HttpResponse("<h2>Hello from Class View</h2>")

   

def demoHtml(request,name):

    context={'uname':name}

    return render(request,'index.html',context)


def cal(request,no1,no2):

    data={}

    data['sum']=int(no1)+int(no2)

    data['sub']=int(no1)-int(no2)

    data['a']=int(no1)

    data['b']=int(no2)

    return render(request,'index2.html',data)


def loop(request):

    data={}

    data['l1']=[10,20,30,40,50,60,70,80,90,100]

    return render(request,'loopdtl.html',data)


def products(request):

    data={}

    # data['product']=[

    #     {'id':1,'name':'Samsung S23','price':32000,'cat':'Mobile'},

    #     {'id':3,'name':'Active Wear','price':2499,'cat':'Clothes'},

        #   {'id':4,'name':'Woodland Shoes','price':6000,'cat':'Shoes'},

    #     {'id':12,'name':'Motorolla','price':9999,'cat':'Mobile'},

    #     {'id':5,'name':'Warm clothes','price':2000,'cat':'Clothes'}

    # ]

    uid=request.user.id

    uname=request.user.username

    print(uid,uname,sep='\n')

    print(request.user.is_authenticated)

    obj=Product.objects.all()

    data['product']=obj

    return render(request,'index.html',data)


def userinput(request):

    if request.method=='GET':

        return render(request,'demoinput.html')

    else:

        nm=request.POST['name']

        email=request.POST['email']

        mno=request.POST['mno']

        print(nm,email,mno)

        obj=Demo.objects.create(name=nm,email=email,mobile=mno)

        obj.save()

        return redirect("/dashboard")


def display(request):

    obj=Demo.objects.all()

    return render(request,'display.html',{'user':obj})


def edit(request,uid):

    if request.method=='GET':

        obj=Demo.objects.filter(id=uid)

        return render(request,'edituser.html',{'user':obj})

    else:

        nm=request.POST['name']

        email=request.POST['email']

        mno=request.POST['mno']

        obj=Demo.objects.filter(id=uid)

        obj.update(name=nm,email=email,mobile=mno)

        return redirect("/dashboard")


def delete(request,uid):

    obj=Demo.objects.filter(id=uid)

    obj.delete()

    return redirect("/dashboard")


def register(request):

    if request.method=='GET':

        return render(request,'register.html')

    else:

        fnm=request.POST['fname']

        lnm=request.POST['lname']

        email=request.POST['email']

        unm=request.POST['uname']

        upass=request.POST['pass']

        print(fnm,lnm,email,unm,upass,sep='\n')

        obj=User.objects.create(username=unm,email=email,first_name=fnm,last_name=lnm)

        obj.set_password(upass)

        obj.save()

        return redirect('/login')

   

def user_login(request):

    if request.method=='GET':

        return render(request,'login.html')

    else:

        unm=request.POST['uname']

        upass=request.POST['pass']

        a=authenticate(username=unm,password=upass)

        print("Authentication result:",a)

        if a is None:

            return redirect('/login')

        else:

            login(request,a)

            print(a.id,a.username,a.password,sep='\n')

            return redirect('/')


def user_logout(request):

    logout(request)

    return redirect("/")


def catfilter(request,cv):

    obj=Product.objects.filter(cat=int(cv))

    data={}

    data['product']=obj

    return render(request,'index.html',data)


from django.db.models import Q


def range(request):

    max=request.POST['max']

    min=request.POST['min']

    c1=Q(price__gte=min)

    c2=Q(price__lte=max)

    obj=Product.objects.filter((c1) & (c2))

    data={}

    data['product']=obj

    return render(request,'index.html',data)


def sort(request,sv):

    if sv == '1':

        o="-price"

    else:

        o="price"

    obj=Product.objects.filter().order_by(o)

    data={}

    data['product']=obj

    return render(request,'index.html',data)


def details(request,pid):

    obj=Product.objects.filter(id=pid)

    data={'product':obj}

    return render(request,"detail.html",data)