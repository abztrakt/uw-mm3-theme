# create /opt/mailman/web, fix permissions so you can write to it and copy
# this to that location

SERVE_FROM_DOMAIN = "example.com"
HYPERKITTY_API_KEY = "someapikey"
MAILMAN_ADMIN_USER = "mailman"
MAILMAN_ADMIN_EMAIL = "email@example.com"
SECRET_KEY="jshaflkjdhaslkjfhdlsjahfldjahfldkj"

INSTALLED_APPS = [
    'mmtheme',
    'hyperkitty',
    'postorius',
    'django_mailman3',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_gravatar',
    'compressor',
    'haystack',
    'django_extensions',
    'django_q',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_mailman3.lib.auth.fedora',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',
]
