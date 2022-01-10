import datetime
import jwt
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import exceptions
from user.models import UserProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view

def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5, minutes=5),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256')
    return access_token
