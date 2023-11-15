from .models import Visitor


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.log_visitor(request, response)
        return response

    def log_visitor(self, request, response):
        session_key = request.session.session_key
        referer = request.META.get('HTTP_REFERER', '')
        status_code = response.status_code
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        page_path = request.path_info

        Visitor.objects.create(
            ip_address=ip_address,
            session_key=session_key,
            referer=referer,
            status_code=status_code,
            user_agent=user_agent,
            page_path=page_path
        )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
