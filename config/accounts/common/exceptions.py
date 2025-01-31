from rest_framework.exceptions import APIException
from rest_framework import status







class InvalidUserTypeException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = ('Invalid user type for this endpoint!')
    default_code = 'invalid_user_type'
    
    


class UserRegisterException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST  
    default_detail = "An error occurred while registering the teacher."
    default_code = "user_register_error"