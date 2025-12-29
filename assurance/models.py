from django.db import models
from django.contrib.auth.models import User
from governance.models import Control


class Risk(models.Model):
    """
    سجل المخاطر
    """
    LEVEL_CHOICES = [
        ('low', 'منخفض'),
        ('medium', 'متوسط'),
        ('high', 'مرتفع'),
        ('critical', 'حرج'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    inherent_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    residual_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    controls = models.ManyToManyField(Control, blank=True)

    def __str__(self):
        return self.title


class ComplianceRequirement(models.Model):
    """
    متطلبات الامتثال
    """
    source = models.CharField(max_length=255)  # لائحة / جهة تنظيمية
    description = models.TextField()
    controls = models.ManyToManyField(Control, blank=True)

    def __str__(self):
        return self.source


class Audit(models.Model):
    """
    التدقيق الداخلي
    """
    title = models.CharField(max_length=255)
    auditor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='audits'
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class AuditFinding(models.Model):
    """
    ملاحظات التدقيق
    """
    audit = models.ForeignKey(
        Audit,
        on_delete=models.CASCADE,
        related_name='findings'
    )
    description = models.TextField()
    risk = models.ForeignKey(
        Risk,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"Finding - {self.audit.title}"
