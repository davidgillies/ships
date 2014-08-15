from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)


class Builder(Company):
    nationality = models.CharField(max_length=20)    


class Owner(Company):
    business = models.CharField(max_length=100, blank=True)


class Link(models.Model):
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)

class OtherName(models.Model):
    name = models.CharField(max_length=50)


class Ship(models.Model):
    SHIP_TYPE_CHOICES = {
        ('pass', 'Passenger'),
        ('cargo', 'Cargo'),
        ('tanker', 'Tanker'),
        ('pass/carg', 'Passenger/Cargo'),
        ('navy', 'Navy'),
    }
    DRIVE_TYPE_CHOICES = {
        ('ps', 'Paddle Steamer'),
        ('st', 'Steam Turbine'),
        ('sa', 'Sail')
    }


    
    name = models.CharField(max_length=40)
    ship_type= models.CharField(max_length=10, choices=SHIP_TYPE_CHOICES, blank=True)
    drive_type = models.CharField(max_length=2, choices=DRIVE_TYPE_CHOICES, blank=True)
    yard_no = models.CharField(max_length=6, blank=True)
    build_year = models.CharField(max_length=4, blank=True)
    built_for = models.CharField(max_length=100, blank=True)
    length_in_feet = models.IntegerField(blank=True, default=0)
    breadth_in_feet = models.IntegerField(blank=True, default=0)
    draft_in_feet = models.IntegerField(blank=True, default=0)
    status = models.CharField(max_length=100, blank=True)
    previous_owners = models.ForeignKey(Owner, blank=True, null=True)
    history = models.TextField(blank=True)
    links = models.ForeignKey(Link, blank=True, null=True)
    other_names=models.ForeignKey(OtherName, blank=True, null=True)

    def is_active():
        pass

    def is_wreck():
        pass 

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
