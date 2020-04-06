def app(environ, start_response):
    print(environ)
    query = environ['QUERY_STRING']
    data = query.replace('&','\n')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]