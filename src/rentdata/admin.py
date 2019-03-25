from django.contrib import admin
from .models.general import *
# Register your models here.

admin.site.register(Apartment)
admin.site.register(Company)
admin.site.register(ImprintLink)
admin.site.register(RealEstate)
admin.site.register(RealEstateAttachments)
admin.site.register(RealEstateTitlePictureUrls)
admin.site.register(Url)
admin.site.register(RealEstateNext)