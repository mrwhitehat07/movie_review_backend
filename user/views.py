from django.http import Http404
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.core.mail.message import EmailMultiAlternatives
from rest_framework import generics
from django.http.response import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
)
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from user.models import Profile, UserProfile
from moviereviews.decorators import check_token
from .utils import generate_access_token
from user.serializers import (
    ProfileSeriL,
    ProfileSerializer,
    UserSer,
    UserSerializer,
)
from django.core.mail import send_mail
from moviereviews import settings
import jwt
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from jwt import exceptions as e

def decypher(token):
    data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    return data["user"]

def encrypt(payload):
    token = jwt.encode(payload, settings.SECRET_KEY)
    return token

def smtp(payload, email):
    token = encrypt({"user": payload})
    subject = "Welcome to MovieReview"
    message = (
        "Hello, "
        + " Please click on this link to activate your account: "
        + "http://127.0.0.1:8000/user/activate/?token="
        + str(token)
    )
    recepient = email
    msg=EmailMultiAlternatives(subject,message,settings.EMAIL_HOST_USER,[recepient])
    msg.send()


def token_validity(request):
    token = request.headers.get("token")
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return HttpResponse("Valid")
    except e.ExpiredSignatureError:
        return HttpResponseBadRequest("Token Expired, Please refetch access token")
    except e.InvalidSignatureError:
        return HttpResponseForbidden("Token Invalid")
    except e.DecodeError:
        return HttpResponseForbidden("Token Invalid")


@csrf_exempt
def activation(request):

    try:
        token_get = request.GET.get("token")
        decrypt = decypher(bytes(token_get, "utf-8"))
        user = UserProfile.objects.get(id=decrypt)
        if user:
            user.is_active = True
            user.save()
    except:
        return JsonResponse(status=400)
    return JsonResponse({"message": "Congrats, Your account is activaed."})


class Login(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        response = Response()

        if (email is None) or (password is None):
            raise exceptions.AuthenticationFailed("email and password required")

        user = UserProfile.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed("user not found")
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("wrong password")

        serialized_user = UserSerializer(user).data
        access_token = generate_access_token(user)

        response.set_cookie(key="refreshtoken", httponly=True)
        response.data = {
            "message": "success",
            "access_token": access_token,
        }

        return response


class Register(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        data = request.data
        email=request.data.get("email")
        username=request.data.get("username")
    
        if email:
            userp = UserProfile.objects.filter(email=email).first()
            data["user"] = {
                "email": email,
                "password": data["password"],
            }
        elif username:
            userp = UserProfile.objects.filter(username=username).first()
            data["user"] = {
                "username": username,
                "password": data["password"],
            }
        else:
            userp=None
        
        if userp != None :
            raise exceptions.NotAcceptable("Phone or Email already in use.")
        
        serializer2 = ProfileSerializer(data=data)
        if serializer2.is_valid(raise_exception=True):

            serializer2.save()
            # if email:
            #     user = UserProfile.objects.get(email=email)
            # if username:
            #     user = UserProfile.objects.get(username=username)


            # smtp(user.pk, email)

            return Response({"User successfully created"})
        else:
            raise exceptions.ValidationError("User validation Error")


@method_decorator(check_token, name='dispatch')
class UpdateProfile(generics.UpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(id=self.kwargs["user"].id)

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

@method_decorator(check_token, name='dispatch')
class ChangePassword(APIView):
    def post(self, request, *args, **kwargs):
        currentPassword = request.data.get("currentPassword")
        newPw1 = request.data.get("newPassword")
        newPw2 = request.data.get("validatePassword")
        print(self.kwargs['user'].id)
        print(request.data)
        if newPw1 == newPw2:
            user_obj = UserProfile.objects.get(id=kwargs["user"].id)

            if user_obj.check_password(currentPassword):
                user_obj.set_password(newPw1)
                user_obj.save()
                return HttpResponse("Password Changed Successfully.")
            else:
                return HttpResponse("Password Error, Please check again.")
        else:
            raise HttpResponse("Password Doesn't match.")


@method_decorator(check_token, name="dispatch")
class GetUser(APIView):
    def get(self, request, *args, **kwargs):
        response = Response()
        print(self.kwargs["user"])
        profile = Profile.objects.get(user=self.kwargs['user'])
        if profile:
            response.data = {
                "profile": ProfileSeriL(Profile.objects.get(user=self.kwargs["user"])).data,
                "user": UserSer(self.kwargs["user"]).data,
            }
            return response
        else:
            return Http404
