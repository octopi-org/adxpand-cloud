from django.contrib import admin
from .models import BenAdGroup, BenCampaign, BenMetrics, Account

# Register your models here.
admin.site.register(Account)
admin.site.register(BenMetrics)
admin.site.register(BenAdGroup)
admin.site.register(BenCampaign)