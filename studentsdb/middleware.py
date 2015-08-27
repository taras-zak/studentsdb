from datetime import datetime
from django.http import HttpResponse
from studentsdb.settings import DEBUG
from bs4 import BeautifulSoup


class RequestTimeMiddleware(object):
    """Display request time on a page"""

    def process_request(self, request):
        if DEBUG == True:
            request.start_time = datetime.now()
        return None

    def process_response(self, request, response):
        # if our process_request was canceled someone within
        # middleware stack, we can not calculate request time
        if not hasattr(request, 'start_time'):
            return response

        # calculate request execution time
        request.end_time = datetime.now()

        if 'text/html' in response.get('Content-Type', ''):
            response.soup = BeautifulSoup(response.content)
            response.original_tag = response.soup.body
            response.new_tag = response.soup.new_tag("div")
            response.new_tag.string = 'Request took: %s' % str(request.end_time - request.start_time)
            response.original_tag.append(response.new_tag)
            #response.content = response.soup
            #soup.body.append('Request took: %s' % str(request.end_time - request.start_time))
        print(response.content)
        
        
        #if 'text/html' in response.get('Content-Type', ''):
        #    response.write('<br/>Request took: %s' % str(request.end_time - request.start_time))
        #print type(response.content)
        #print request
        return response

    def process_view(self, request, view, args, kwargs):
        return None

    def process_template_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        return HttpResponse('Exception found: %s' % exception)
