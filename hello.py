from django.http import HttpResponse

def return_params(environ, request):
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return HttpResponse(body)