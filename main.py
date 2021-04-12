from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from benaxfrwork.core import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
}


def secret_controller(request):
    # пример Front Controller
    request['check'] = 'checked'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)
with make_server('', 8000, application) as httpd:
    print('Server started at port: 8000')
    httpd.serve_forever()

