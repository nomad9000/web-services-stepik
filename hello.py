def wsgi_application(environ, start_response):
    query = environ.get('QUERY_STRING')
    if query:
        body = query.replace('&', '\n')
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return [ body ]