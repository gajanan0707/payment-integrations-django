from accounts.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from accounts.utils import check_email, check_password, check_username


# Create your views here.
@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        if check_username(request.POST.get("username")):
            return JsonResponse({"error": "Username should be unique"}, status=400)
        if check_email(request.POST.get("email")):
            return JsonResponse({"error": "Email Already Exits."}, status=401)
        if check_password(request.POST["password"], "length"):
            return JsonResponse(
                {"error": "Password should be at least 6 characters long."}, status=400
            )
        if not check_password(request.POST["password"], "pattern"):
            return JsonResponse(
                {
                    "error": "Password should have at least: one lower case letter, one upper case letter, one number and one special character !#$@%&."
                },
                status=400,
            )
        user = User.objects.create_user(
            email=request.POST.get("email"),
            password=request.POST.get("password"),
            user_name=request.POST.get("username"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            phone=request.POST.get("phone"),
        )
        if user:
            return JsonResponse({"success": "Successfully signup"}, status=200)
    return render(request, "authentications/signup.html")


@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        if not check_email(request.POST.get("email")):
            return JsonResponse(
                {"error": str(request.POST["email"]) + " is not registered with us"},
                status=400,
            )
        user = authenticate(
            request, username=request.POST["email"], password=request.POST["password"]
        )
        if user is not None:
            auth_login(request, user)
            return JsonResponse({"success": "Successfully User Login."}, status=200)
        else:
            return JsonResponse({"error": "password is incorrect"}, status=401)

    return render(request, "authentications/login.html")


@csrf_exempt
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    else:
        return redirect("login")
