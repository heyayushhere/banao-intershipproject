from django.shortcuts import redirect
from django.urls import reverse

class RestrictNavigationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is logged out and the current path requires authentication
        if not request.user.is_authenticated and request.path != reverse('login'):
            return redirect('login')  # Redirect to the login page

        return response
