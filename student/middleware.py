import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeMiddleware(MiddlewareMixin):

    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        else:
            start = time.time()
            response = func(request)
            costed = time.time() - start
            print('process view: {:.2f}'.format(costed))
            return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('process response: {:.2f}'.format(costed))
        return response

    def process_template_response(self, request, response):
        return response
