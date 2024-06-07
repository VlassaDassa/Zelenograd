# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/y/y90001hs/y90001hs.beget.tech/Zelenograd')
sys.path.insert(1, '/home/y/y90001hs/y90001hs.beget.tech/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()