from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quarintine(models.Model):
    status = [
        ('Medical Leave', 'Medical Leave'),
        ('Full Duty', 'Full Duty'),
        ('Light Duty', 'Light Duty'),
        ('Military Leave', 'Military Leave'),
    ]
    rank = [
        ('EMT', 'EMT'),
        ('Medic', 'Medic'),
        ('Lt', 'Lt'),
        ('Capt', 'Capt')
    ]

    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    rank = models.CharField(max_length=6, choices=rank)
    shield = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=status)
    last_bhs = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    next_bhs = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    full_duty = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.last_name, self.first_name
    
class Profile(models.Model):
    status = [
        ('Medical Leave', 'Medical Leave'),
        ('Full Duty', 'Full Duty'),
        ('Light Duty', 'Light Duty'),
        ('Military Leave', 'Military Leave'),
    ]

    rank = [
        ('EMT', 'EMT'),
        ('Medic', 'Medic'),
        ('Lt', 'Lt'),
        ('Capt', 'Capt')
    ]

    tour = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]

    platoon = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),      
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),  
    ]

    unit = [
        ('33W', '33W'),
        ('33A', '33A'),
        ('43V', '43V'),
        ('43H', '43H'),
        ('33D', '33D'),
        ('43G', '43G'),
        ('33Z', '33Z'),
        ('43A', '43A'),
        ('33F', '33F'),
        ('43C', '43C'),
        ('33C', '33C'),
        ('43D', '43D'),
        ('C43', 'C43'),
        ('B43', 'B43'),
        ('VR', 'VR'),
    ]

    cert = [
        ('EMT', 'EMT'),
        ('Paramedic', 'Paramedic'),
    ]

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    rank = models.CharField(max_length=6, choices=rank)
    shield = models.IntegerField()
    tour = models.CharField(max_length=2, choices=tour)
    platoon = models.CharField(max_length=2, choices=platoon)
    unit = models.CharField(max_length=3, choices=unit)
    status = models.CharField(max_length=30, choices=status)
    oda = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    ted = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    lastfive = models.IntegerField(null=True, blank=True)
    statenumber = models.IntegerField(null=True, blank=True)
    stateexp = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    macexp = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    streetaddress = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    contact_name = models.CharField(max_length=50,null=True, blank=True)
    relationship = models.CharField(max_length=100, null=True, blank=True)
    contact_phone = models.CharField(max_length=15,null=True, blank=True)
    cert = models.CharField(max_length=20, choices=cert, null=True, blank=True)


    def __str__(self):
        return self.last_name