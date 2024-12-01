import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.dataclasses.user_dataclass import User
from core.services.jwt_service import ActivateToken, JWTService, RecoverToken

from apps.all_users.users.models import UserModel

from configs.celery import app


class EmailService:
    @staticmethod
    @app.task
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
        cls.__send_email.delay(
            user.email,
            'Register EMAIL',
            {'name': user.profile.name, 'url': url},
            'register.html'
        )

    @classmethod
    def recovery_password(cls, user: User):
        token = JWTService.create_token(user, RecoverToken)
        url = f'http://localhost:3000/recovery/{token}'
        cls.__send_email.delay(
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
        cls.__send_email.delay(
            user.email,
            'checking ad',
            {
                'name': user.profile.name,

            },
            'checking_ad.html',
        )

    @classmethod
    def notify_admin_error_brand(cls, user: User):
        cls.__send_email.delay(
            user.email,
            'error brand',
            {'name': user.profile.name},
            'brand_not.html',
        )

    @staticmethod
    @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService.__send_email(user.email, 'Spam', {},'spam.html')

