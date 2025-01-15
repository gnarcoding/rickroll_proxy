from mitmproxy import http

# Rickroll URL
RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Domains and patterns to exclude
EXCLUDED_DOMAINS = [
    "googlevideo.com",           # Video streams
    "ytimg.com",                 # Thumbnails
    "gstatic.com",               # Static resources
    "google.com",                # Google APIs
    "googlesyndication.com",     # Ads and tracking
    "youtube.com/api",           # YouTube API endpoints
    "youtube.com/sw.js",         # Service workers
    "youtube.com/generate_204",  # Keep-alive check
    "mozilla.cloudflare-dns.com",  # DNS over HTTPS
    "detectportal.firefox.com"   # Firefox network detection
]

# Keep track of Rickrolled domains
rickrolled_domains = set()

def request(flow: http.HTTPFlow) -> None:
    global rickrolled_domains

    # Extract the domain from the URL
    domain = flow.request.host

    # Skip excluded domains
    for excluded_domain in EXCLUDED_DOMAINS:
        if excluded_domain in flow.request.pretty_url:
            return

    # Skip redirection for Rickroll URL itself
    if flow.request.pretty_url.startswith(RICKROLL_URL):
        return

    # Skip if the domain has already been Rickrolled
    if domain in rickrolled_domains:
        return

    # Redirect only navigational HTML requests
    if flow.request.method == "GET" and "html" in flow.request.headers.get("accept", ""):
        print(f"Rickrolling: {flow.request.pretty_url}")
        # Mark the domain as Rickrolled
        rickrolled_domains.add(domain)
        flow.response = http.HTTPResponse.make(
            302,  # HTTP redirect
            b"",  # Empty body
            {"Location": RICKROLL_URL}
        )
