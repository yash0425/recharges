from django.db import models

# Create your models here.
class register1(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    contect=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    imgs=models.FileField(upload_to="images")
    def __str__(self):
        return self.email

class recharge1(models.Model):
    sim_name=models.CharField(max_length=200)
    amout=models.CharField(max_length=150)
    data=models.CharField(max_length=200)
    validity=models.CharField(max_length=200)
    def __str__(self):
        return self.sim_name

class broadband(models.Model):
    company=models.CharField(max_length=100)
    hoder_name=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=100)
    ammunt=models.IntegerField()
    def __str__(self):
        return self.hoder_name

class creditcard(models.Model):
    bank=models.CharField(max_length=100)
    card_number=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    ammount=models.IntegerField()
    def __str__(self):
        return self.name

class cylenderbook(models.Model):
    gas=models.CharField(max_length=100)
    consumer_number=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    amount=models.IntegerField() 
    def __str__(self):
        return self.name

class educationfees(models.Model):
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    institution=models.CharField(max_length=100)
    your_class=models.IntegerField()  
    year=models.CharField(max_length=100)
    amount=models.IntegerField() 
    def __str__(self):
        return self.institution

  
class electricity(models.Model):
    bill_holder=models.CharField(max_length=100)
    bill_id=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    amount=models.IntegerField() 
    def __str__(self):
        return self.bill_holder

class loan(models.Model):
    loan_type=models.CharField(max_length=100)
    loan_holder=models.CharField(max_length=100)
    loan_number=models.CharField(max_length=100)
    mob_number=models.CharField(max_length=100)
    ammount=models.IntegerField() 
    def __str__(self):
        return self.loan_holder

class rentpay(models.Model):
    rent_about=models.CharField(max_length=100)
    account_holder=models.CharField(max_length=100)
    aount_number=models.CharField(max_length=100)
    mob_number=models.CharField(max_length=100)
    ammount=models.IntegerField()
    def __str__(self):
        return self.account_holder    