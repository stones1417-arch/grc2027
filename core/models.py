from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    """
    نموذج أساسي للتواريخ
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrganizationUnit(TimeStampedModel):
    """
    الهيكل التنظيمي (إدارة – قطاع – وحدة)
    """
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name


class Site(TimeStampedModel):
    """
    المواقع التشغيلية (الحرم المكي – الحرم النبوي – مرافق)
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Role(TimeStampedModel):
    """
    الأدوار الوظيفية داخل GRC
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserProfile(TimeStampedModel):
    """
    ربط المستخدم بالهيكل التنظيمي والدور
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_unit = models.ForeignKey(
        OrganizationUnit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username


class Attachment(TimeStampedModel):
    """
    المرفقات العامة (أدلة – ملفات – مستندات)
    """
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='attachments/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
