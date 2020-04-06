def app(environ, start_response):
    query = environ['QUERY_STRING'].split('?')[1]
    data = query.replace('&','\n')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]