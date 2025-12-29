from pathlib import Path
import os

# =========================
# المسارات الأساسية
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent  # => C:\Users\stone\grc2027


# =========================
# الأمان (Security)
# =========================
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-%x0z2t^^bl%t)@+fb^&rtbodikkco!o!cfszvwp^38j9=)6)j4"
)
# ⚠️ في الإنتاج: عرّف DJANGO_SECRET_KEY في متغيرات البيئة

DEBUG = True  # ❌ اجعلها False في الإنتاج

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]  # للتطوير فقط


# =========================
# التطبيقات
# =========================
INSTALLED_APPS = [
    # Django Core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # =========================
    # GRC Project Apps
    # =========================
    "core",        # الأساس: المستخدمين، الهيكل التنظيمي، الصلاحيات
    "governance",  # الحوكمة: السياسات، الإجراءات، الضوابط
    "assurance",   # المخاطر، الامتثال، التدقيق
]


# =========================
# الوسطاء (Middleware)
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.locale.LocaleMiddleware",  # 🌐 دعم العربية

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================
# الروابط
# =========================
ROOT_URLCONF = "grc2027.urls"


# =========================
# القوالب (Templates)
# =========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # ✅ هنا تعريف المسار العام للقوالب بعد نقلها
        "DIRS": [BASE_DIR / "templates"],  # C:\Users\stone\grc2027\templates

        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================
# WSGI
# =========================
WSGI_APPLICATION = "grc2027.wsgi.application"


# =========================
# قاعدة البيانات
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # للتطوير
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# ✔ في الإنتاج: PostgreSQL


# =========================
# التحقق من كلمات المرور
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# =========================
# اللغة والتوقيت 🌍
# =========================
LANGUAGE_CODE = "ar"

LANGUAGES = [
    ("ar", "العربية"),
    ("en", "English"),
]

TIME_ZONE = "Asia/Riyadh"

USE_I18N = True
USE_TZ = True


# =========================
# الملفات الثابتة (Static)
# =========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ مجلد static العام (إن وجد)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# =========================
# الملفات المرفوعة (Media)
# =========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# =========================
# الإعداد الافتراضي للمفاتيح
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================
# إعدادات أمان إضافية (عند الإنتاج)
# =========================
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
