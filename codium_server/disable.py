# CSRF protection disabling. It is not needed as the json web token authorization is used


class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
