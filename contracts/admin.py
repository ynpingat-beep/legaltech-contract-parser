from django.contrib import admin
from .models import Contract, ExtractedClause, RiskFlag

admin.site.register(Contract)
admin.site.register(ExtractedClause)
admin.site.register(RiskFlag)