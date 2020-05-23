from django.utils.deprecation import MiddlewareMixin
from .token_functionality import degenerate_token,authenticate,authenticate_token
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse,HttpResponse

class Auth_Middleware(MiddlewareMixin):


    def process_request(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        token=str(request.META.get('HTTP_AUTHORIZATION','')).replace('Bearer','').strip()

        if(token=='' and request.get_full_path() in ['/login/','/singup/','/jobseeker/','/business/']):
            print('Token',token)
        else:
            try:
                data=authenticate_token(token,ip)
                if request.get_full_path() == '/test/':

                    return JsonResponse({'status': 'Token Verified','token_data':data}, status=status.HTTP_200_OK)
            except Exception as e:
                pass
                # return HttpResponse({'error':'Token Authentication failed'},status=status.HTTP_400_BAD_REQUEST)
        if request.get_full_path()!='/login/':
            print('just test')

