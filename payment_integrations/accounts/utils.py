import re
from accounts.models import User


def check_email(email):
    return User.objects.filter(email__exact=email).exists()


def check_username(username):
    return User.objects.filter(user_name__exact=username).exists()


def check_password(password, req_type):
    if req_type == "pattern":
        pattern = r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!#$@%&])[\w\d!#$@%&]{6,20}$"
        if re.match(pattern, password):
            return True
        return False
    if req_type == "length":
        if len(password) < 6:
            return True
        return False
