import sae
from learn_models import wsgi
application = sae.create_wsgi_app(wsgi.application)