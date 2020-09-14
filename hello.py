from django.http import HttpResponse

def return_params(environ, start_response):
    print(environ['QUERY_STRING'])
    data = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    print(data)
    return data