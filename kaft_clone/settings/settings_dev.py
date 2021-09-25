from .settings_base import BASE_DIR, INSTALLED_APPS
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

if os.environ.get('DJANGO_DEBUG') == 'True':
    # Hocanın ayarlarında olacak bu ayar ama if koşulu koyduğumuz için her projeye bu if koşulunu koyabiliriz :)
    INSTALLED_APPS += [
        'django_extensions',
    ]