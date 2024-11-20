# from django.contrib.auth import get_user_model
#
# from core.dataclasses.user_dataclass import User
# from core.services.jwt_service import ActivateToken, JWTService
#
# UserModel: User = get_user_model()
# class EmailService:
#     @classmethod
#     def register(cls, user:User):
#         token = JWTService.create_token(user,ActivateToken)
#         url = f'http://localhost:3000/activate/{token}'
#