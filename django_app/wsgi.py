from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root="static")
# application.add_files("/static/")
#  prefix="more-files/"