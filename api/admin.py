from django.contrib import admin
from .models import BenAdGroup, BenCampaign, BenMetrics, Hero, Account

# Register your models here.
admin.site.register(Hero)
admin.site.register(Account)
admin.site.register(BenMetrics)
admin.site.register(BenAdGroup)
admin.site.register(BenCampaign)