from django.shortcuts import render,redirect
from app2.models import recharge1,register1,broadband,creditcard,cylenderbook,educationfees,electricity,loan,rentpay
from django.contrib import messages
from django.core.mail import send_mail


def login(request):
    if (request.method=='POST'):
        em=request.POST['email']
        pas = request.POST['password']
        code=register1.objects.filter(email=em,password=pas)
        print(em)
        if(code):
            request.session['first']=em
            return redirect('/')
        else:
            return render(request,'login.html',{'msj':'wrong email or password'})
    return render(request,'login.html')   

def profile(request):
    sec=request.session.get('first')
    thrd=register1.objects.all().filter(email=sec)
    return render(request,'homepage.html',{'data1':thrd})

def logout(request):
    try:
        del request.session['first']
    except:
        pass    
    return render(request,'login.html')

def mobrecharge(request):
    if request.session.has_key('first'):
        data=recharge1.objects.all()
        return render(request,"mobrecharge.html",{'record':data})
    else:
        return redirect('/log')     
 
def recharge(request,id):
    record=recharge1.objects.filter(id=id)
    return render(request,"recharge.html",{'data':record})  
    
def register(request):
    if(request.method=='POST'):
        code=register1()
        code.name=request.POST['username']
        code.email=request.POST['Email']
        code.contect=request.POST['contects']
        code.password=request.POST['passwords']
        pass2=request.POST['pass2']
        code.img=request.POST['image']
        code5=register1.objects.filter(email=request.POST['Email'])
        if (code.password==pass2):
            if(code5):
                return render(request,'registration.html',{'msj':'already exist'})
            else:

                code.save()
                subject='registration success'
                message=f'hi{code.name},you have register succesfully'
                email_from='yashpanday1205@gmail.com'
                rec_list=[code.email]
                send_mail( subject,message,email_from,rec_list)
                return redirect('/log')
        else:
            return render(request,'registration.html',{'msj':'password is not same'})

    return render(request,'registration.html')

def cylender(request):
    if(request.method=='POST'):
        cyl=cylenderbook()
        cyl.gas=request.POST['gase']
        cyl.name=request.POST['fullname']
        cyl.consumer_number=request.POST['con_num']
        cyl.amount=request.POST['ount']
        cyl.save()
        return render(request,"payment.html")
    if request.session.has_key('first'):
        return render(request,"cylender.html")         
    else:
        return redirect('/log')        
         
def payment(request):
    return render(request,"payment.html")   

def loandep(request):
    if(request.method=='POST'):
        lon=loan()
        lon.loan_type=request.POST['loan']
        lon.loan_holder=request.POST['person']
        lon.loan_number=request.POST['loan_num']
        lon.mob_number=request.POST['rnum']
        lon.ammount=request.POST['loan_amt']
        lon.save()
        return render(request,"payment.html")
    if request.session.has_key('first'):
        return render(request,"loan.html")        
    else:   
        return redirect('/log')   
     
def electri(request):
    if(request.method=='POST'):
        elec=electricity()
        elec.bill_holder=request.POST['holder']
        elec.bill_idr=request.POST['id']
        elec.number=request.POST['numb']
        elec.amount=request.POST['bill']
        elec.save()
        return render(request,"payment.html") 
    if request. session.has_key('first'):
        return render(request,"electricity.html")        
    else: 
        return redirect('/log') 

def credit(request):
    if(request.method=='POST'):
        card=creditcard()
        card.bank=request.POST['bank']
        card.card_number=request.POST['card']
        card.name=request.POST['full_name']
        card.ammount=request.POST['amt']
        card.save()
        return render(request,"payment.html") 
    if request. session.has_key('first'):
        return render(request,"creditcard.html")        
    else: 
        return redirect('/log')          
      
def rent(request):
    if(request.method=='POST'):
        ren=rentpay()
        ren.rent_about=request.POST['about']
        ren.account_holder=request.POST['hol']
        ren.aount_number=request.POST['bank_num']
        ren.mobile_number=request.POST['reg_num']
        ren.ammount=request.POST['mount']
        ren.save()
        return render(request,"payment.html") 
    if request. session.has_key('first'):
        return render(request,"rentpay.html")         
    else: 
        return redirect('/log')         
       
def education(request):
    if(request.method=='POST'):
        tion=educationfees()
        tion.country=request.POST['count']
        tion.state=request.POST['stat']
        tion.institution=request.POST['inst']
        tion.your_class=request.POST['section']
        tion.year=request.POST['sal']
        tion.amount=request.POST['moun']
        tion.save()
        return render(request,"payment.html") 
    if request. session.has_key('first'):    
        return render(request,'education.html')  
    else: 
        return redirect('/log')         
     
def broadbandcon(request):
    if(request.method=='POST'):
        band=broadband()
        band.company=request.POST['compn']
        band.holder_name=request.POST['nam']
        band.mobile_number=request.POST['num']
        band.ammunt=request.POST['pay']
        band.save()
        return render(request,"payment.html")
    if request. session.has_key('first'):
        return render(request,"broadband.html") 
    else: 
        return redirect('/log')     
     
def forget(request):
    return render(request,"forget.html") 

def confrom(request):
    return render(request,"conform.html")  

def update(request):
    kyc=request.session.get('first')
    thrd=register1.objects.all().filter(email=kyc)
    if request.method == 'POST':
        usr=request.POST['user']
        cont=request.POST['con']
        psw=request.POST['word']
        city=request.POST['city1']
        state=request.POST['state1']
        country=request.POST['country1']
        
        code9=register1.objects.filter(name=usr,contect=cont,password=psw)
        if code9:
            messages.success(request,'already save')
            return render(request,"update.html",{'data2':thrd})
        else:
            register1.objects.update(name=usr,contect=cont,password=psw,city=city,country=country,state=state)
            messages.success(request,'update succesfully')
            return render(request,"update.html",{'data2':thrd})
    return render(request,"update.html",{'data2':thrd})                
