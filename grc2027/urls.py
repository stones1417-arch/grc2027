from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ✅ الصفحة الرئيسية
    path('', include('core.urls')),

    # لوحة الإدارة
    path('admin/', admin.site.urls),

    # تطبيقات منصة GRC
    path('governance/', include('governance.urls')),
    path('assurance/', include('assurance.urls')),
]

# دعم الملفات المرفوعة أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
