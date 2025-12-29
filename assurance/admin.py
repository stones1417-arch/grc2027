from django.contrib import admin
from .models import (
    Risk,
    ComplianceRequirement,
    Audit,
    AuditFinding
)


@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('title', 'inherent_level', 'residual_level', 'owner')
    list_filter = ('inherent_level', 'residual_level')
    search_fields = ('title',)
    filter_horizontal = ('controls',)


@admin.register(ComplianceRequirement)
class ComplianceRequirementAdmin(admin.ModelAdmin):
    list_display = ('source',)
    search_fields = ('source',)
    filter_horizontal = ('controls',)


class AuditFindingInline(admin.TabularInline):
    model = AuditFinding
    extra = 1


@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('title', 'auditor', 'start_date', 'end_date')
    inlines = [AuditFindingInline]
    search_fields = ('title',)


@admin.register(AuditFinding)
class AuditFindingAdmin(admin.ModelAdmin):
    list_display = ('audit', 'is_closed')
    list_filter = ('is_closed',)
