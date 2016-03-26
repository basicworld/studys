#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
Use for deployment
depend on uWSGI
depend on linux
"""

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


# from django.core.handlers.wsgi import WSGIHandler
# application = WSGIHandler() is not useful
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
