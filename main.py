from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from benafrwork.core import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
}


def secret_controller(request):
    # пример Front Controller
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)
with make_server('', 8000, application) as httpd:
    print(111)
    httpd.serve_forever()

