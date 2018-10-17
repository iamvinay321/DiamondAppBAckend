from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.users.serializers import ProfileSerializer,UserSerializer
from app.users.models import UserProfile
from app.lib.common import RequestOverwrite,AccessUserObj
from app.lib.response import ApiResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from app.lib.permissions import IsAuthenticatedOrCreate

class UserApi(APIView):
    
    
    def post(self,request):
        """
           This api create user.'Email' and 'Password' field is required.
           url: user/create

        """
        try:
            user_info = UserSerializer(data = request.data)
            if not user_info.is_valid():
                return ApiResponse().error(user_info.errors,400)
            user = self.create_user(request)
            if not(user):
                return ApiResponse().error("This email is already exists", 400)
            RequestOverwrite().overWrite(request, {'user':user.id})
            user_data = ProfileSerializer(data=request.data)
            if not(user_data.is_valid()):
                return ApiResponse().error(user_data.errors, 400)
            user_data.save()
            return ApiResponse().success(user_data.data, 200)
        except Exception as err:
            print(err)
            return ApiResponse().error("There is a problem while creating user", 500)

    def create_user(self,request):
        try:
            user = User.objects.create_user(username=request.data.get('email'),
            email=request.data.get('email'),password=request.data.get('password'),is_staff=True,is_active=True)
            return user
        except Exception as err:
            print(err)
            return None

    permission_classes = (IsAuthenticatedOrCreate, )
    def put(self,request,user_id):
        try:
            """
            This api update user details 
            url: user/edit/user_id
            """
            if(request.data.get('email')):
                try:
                    user = User.objects.get(email=request.data.get('email'))
                    if int(user_id) != int(user.id):
                        return ApiResponse().error("This email is already exists", 400)
                except Exception as err:
                    print(err)
                get_data = UserProfile.objects.get(user=user_id)
                RequestOverwrite().overWrite(request, {'user':user_id})
                User.objects.filter(id = user_id).update(email = request.data.get('email'), username = request.data.get('email'))
                update_data = ProfileSerializer(get_data,data=request.data)
                if update_data.is_valid():
                    update_data.save()
                    return ApiResponse().success(update_data.data, 200)
                else:
                    return ApiResponse().error(update_data.errors, 400) 
        except Exception as err:
            print(err)
            return ApiResponse().error("Error", 500)

    permission_classes = (IsAuthenticatedOrCreate, )
    def delete(self,request,user_id):
        try:
            """
               This api make user disable
               url: user/disable/user_id 
            """
            email_val = User.objects.get(id=user_id).email
            User.objects.filter(id = user_id).update(is_active=False)
            UserProfile.objects.filter(user=user_id).update(is_deleted=True,deleted_val = email_val)
            return ApiResponse().success("User disabled", 200)
        except Exception as err:
            print(err)
            return ApiResponse().error("Please send valid id", 500)


class LoginApi(APIView):
    
    
    def post(self,request):
        """
           This api make user login.
           url: user/login
        """
        try:
            if request.data.get('email') and request.data.get('password'):
                user = UserSerializer(data = request.data)
                if not user.is_valid():
                    return ApiResponse().error(user.errors,400)
                try:
                    user_email = User.objects.get(email=request.data.get('email'))
                    auth_user = authenticate(username=user_email,password=request.data.get('password'))
                except Exception as err:
                    print(err)
                    return ApiResponse().error("Invalid username or password", 400)     
                if not auth_user:
                    return ApiResponse().error("invalid username or password", 400) 
                token,create = Token.objects.get_or_create(user_id=auth_user.id)    
                if(auth_user):
                    try:
                        userprofile = UserProfile.objects.get(user_id=auth_user.id, is_deleted=False)
                        user_data = ProfileSerializer(userprofile)
                    except Exception as err:
                        print(err)  
                        return ApiResponse().error("invalid email or password", 400)

                token_value = {
                    'token':token.key,
                    }
                user_response = user_data.data
                user_response.update(token_value)
                return ApiResponse().success(user_response, 200)
            return ApiResponse().error("Please send correct email and password", 400)
        except Exception as err:
            print(err)
            return ApiResponse().error("Error while login", 500)



class ChangePassword(APIView):

    permission_classes = (IsAuthenticatedOrCreate, )
    def post(self,request):
        try:
            """
                User can change password."old_password","new_password","confirm_new_password" field is required.
                url: user/changepassword

            """
            user = AccessUserObj().fromToken(request).user
            if not request.data.get("old_password"):
                return ApiResponse().error("Please enter current password.",400)
            if UserProfile.objects.filter(is_deleted=True, user=user):
                return ApiResponse().success("User does not exist",400) 
            if request.data.get("old_password") is not None:
                if authenticate(username = user, password = request.data.get("old_password")) is None:
                    return ApiResponse().error("Invalid current password entered.",400)
            password = request.data.get("new_password")
            confirm_new_password = request.data.get("confirm_new_password")
            if password != '' and confirm_new_password !='':
                
                if password != confirm_new_password:
                    return ApiResponse().error("New Password and Confirm Password does not match",400)
                user.set_password(request.data.get("new_password"))
                user.save()
                return ApiResponse().success("password changed successfully", 200)
                
            return ApiResponse().error("Password empty", 400)   
        except Exception as err:
            print(err)
            return ApiResponse().error("Error while change password", 500)


class ForGotPassword(APIView):
    
    def post(self,request):
        """
            Users can send a forgot password email and recover account
            url:user/forgotpassword

        """
        try:
            user = User.objects.get(email = request.data.get("email"))
        except Exception as err:
            return ApiResponse().error("This email is not registered", 400)
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save()
        frm = 'XYZ'
        body = "Hi there. \n You have requested a new password for your account.\nYour temporary password is "+password+""
        if Email.sendMail("Forgot password",body,frm,user.email) is True:
            return ApiResponse().success("New password have to sent to your email",200)    
        return ApiResponse().error("Error while sending the email",500) 
        