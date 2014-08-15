from django.contrib import admin
from ships.models import *

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)

class OtherNameAdmin(admin.ModelAdmin):
    pass

admin.site.register(OtherName, OtherNameAdmin)

class BuilderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Builder, BuilderAdmin)

class OwnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Owner, OwnerAdmin)

class ShipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ship, ShipAdmin)


class PeopleAdmin(admin.ModelAdmin):
    pass

admin.site.register(People, PeopleAdmin)
