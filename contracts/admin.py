from django.contrib import admin
from .models import Contract, ExtractedClause, RiskFlag


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "uploaded_at"
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "uploaded_at",
    )

    ordering = (
        "-uploaded_at",
    )


@admin.register(ExtractedClause)
class ExtractedClauseAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "contract",
        "clause_type"
    )

    search_fields = (
        "clause_type",
        "clause_text",
        "contract__title"
    )

    list_filter = (
        "clause_type",
    )

    ordering = (
        "contract",
    )


@admin.register(RiskFlag)
class RiskFlagAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "contract",
        "risk_level"
    )

    search_fields = (
        "description",
        "contract__title"
    )

    list_filter = (
        "risk_level",
    )

    ordering = (
        "contract",
    )