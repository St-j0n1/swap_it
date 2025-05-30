import shortuuid
from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings


def send_verification_code(email):
    su = shortuuid.ShortUUID()
    code = su.random(length=6)


    print(f"[DEBUG] Generated code for {email}: {code}")
    cache.set(f'verify:{email.lower()}', code, timeout=60 * 60)

    send_mail(
        subject="Your Verification Code",
        message=f"Your verification code in Barter.ge is: {code}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )