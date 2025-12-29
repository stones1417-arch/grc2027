from django.db import models
from django.contrib.auth.models import User


class Framework(models.Model):
    """
    الأطر والمعايير (ISO – COSO – سياسات داخلية)
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Policy(models.Model):
    """
    السياسات
    """
    title = models.CharField(max_length=255)
    version = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Procedure(models.Model):
    """
    الإجراءات
    """
    title = models.CharField(max_length=255)
    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
        related_name='procedures'
    )

    def __str__(self):
        return self.title


class Control(models.Model):
    """
    الضوابط (قلب منصة GRC)
    """
    CONTROL_TYPE_CHOICES = [
        ('preventive', 'وقائي'),
        ('detective', 'كاشف'),
        ('corrective', 'تصحيحي'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    control_type = models.CharField(
        max_length=20,
        choices=CONTROL_TYPE_CHOICES
    )
    framework = models.ForeignKey(
        Framework,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
