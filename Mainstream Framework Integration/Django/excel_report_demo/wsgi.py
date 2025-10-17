import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "excel_report_demo.settings")

application = get_wsgi_application()
