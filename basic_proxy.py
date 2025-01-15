from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    """
    This function is called whenever a client makes a request.
    Logs the requested URL to the console.
    """
    print(f"Request URL: {flow.request.pretty_url}")

def response(flow: http.HTTPFlow) -> None:
    """
    This function is called when the server sends a response.
    Logs the status code and content type of the response.
    """
    print(f"Response: {flow.response.status_code} {flow.response.headers.get('content-type', 'unknown')}")
