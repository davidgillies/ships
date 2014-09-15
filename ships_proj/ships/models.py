from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True)
    founded = models.CharField(max_length=10, blank=True)
    years_operating = models.CharField(max_length=15, blank=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Builder(Company):
    nationality = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=50, blank=True)

class Owner(Company):
    business = models.CharField(max_length=100, blank=True)


class Link(models.Model):
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class OtherName(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


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
    ship_type = models.CharField(max_length=10,
                                 choices=SHIP_TYPE_CHOICES, blank=True)
    drive_type = models.CharField(max_length=2,
                                  choices=DRIVE_TYPE_CHOICES, blank=True)
    yard_no = models.CharField(max_length=6, blank=True)
    build_year = models.CharField(max_length=4, blank=True)
    built_for = models.CharField(max_length=100, blank=True)
    length_in_feet = models.IntegerField(blank=True, default=0)
    breadth_in_feet = models.IntegerField(blank=True, default=0)
    draft_in_feet = models.IntegerField(blank=True, default=0)
    status = models.CharField(max_length=100, blank=True)
    builder = models.ForeignKey(Builder, blank=True, null=True)
    previous_owners = models.ManyToManyField(Owner, blank=True, null=True)
    history = models.TextField(blank=True)
    links = models.ManyToManyField(Link, blank=True, null=True)
    other_names = models.ManyToManyField(OtherName, blank=True, null=True)

    def is_active():
        pass

    def is_wreck():
        pass

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=100)
    biog = models.TextField(blank=True)
    birth_year = models.CharField(max_length=4, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    ships = models.ManyToManyField(Ship, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

