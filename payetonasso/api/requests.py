PORTS = {
    '80': 'http',
    '443': 'https',
}


def get_host_uri(request):
    return request.build_absolute_uri().split(request.get_host())[0] + request.get_host()


def build_uri(request, url):
    return get_host_uri(request) + url
