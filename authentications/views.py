from django.shortcuts import render


def home(request):
    return render(request, "auth/index.html")


def dashboard(request):
    print(f"request: {request.user}")
    return render(request, "auth/dashboard.html")
