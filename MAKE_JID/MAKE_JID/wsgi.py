import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MAKE_JID.MAKE_JID.settings')

application = get_wsgi_application()
