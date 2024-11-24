import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import get_template

from core.dataclasses.user_dataclass import User
from core.services.jwt_service import ActivateToken, JWTService, RecoverToken

from configs import settings

UserModel: User = get_user_model()


class EmailService:
    @staticmethod
    def __send_email(to: str, subject: str, context: dict, template_name: str) -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get("EMAIL_HOST_USER"), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def send_test_email(cls):
        cls.__send_email('grigoriyvorobiov1@gmail.com', 'TEST EMAIL', {}, 'test.html')

    @classmethod
    def register(cls, user: User):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email(
            user.email,
            'Register EMAIL',
            {'name': user.profile.name, 'url': url},
            'register.html'
        )

    @classmethod
    def recovery_password(cls, user: User):
        token = JWTService.create_token(user, RecoverToken)
        url = f'http://localhost:3000/recovery/{token}'
        cls.__send_email(
            user.email,
            'Recovery PASSWORD',
            {
                'name': user.profile.name,
                'url': url
            },
            'recovery_password.html',
        )

    @classmethod
    def notify_manager(cls, user: User):
        cls.__send_email(
            user.email,
            'checking ad',
            {
                'name': user.profile.name,

            },
            'checking_ad.html',
        )