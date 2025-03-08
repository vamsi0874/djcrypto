# from django.utils.deprecation import MiddlewareMixin
# from django.http import HttpResponse

# class CustomMiddleware(MiddlewareMixin):

#     def process_request(self, request):
#         print("🔹 Request Middleware: Before View Execution")
#         if request.path == "/blocked/":
#             return HttpResponse("🚫 This page is blocked by custom middleware.")

#     def process_response(self, request, response):
#         print("🔹 Response Middleware: After View Execution")
#         return response
