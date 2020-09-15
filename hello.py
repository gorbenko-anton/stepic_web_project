from django.http import HttpResponse

def return_params(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    print([bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), 'ascii')])
    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), 'ascii')]
    
