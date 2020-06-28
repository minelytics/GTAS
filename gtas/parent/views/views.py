from django.shortcuts import render
from django.views import View


class DashboardView(View):
    template_view = "parent/dashboard.html"

    def get(self, request):
        return render(request, "parent/dashboard.html")


class DashView(View):
    template_view = "parent/dash.html"

    def get(self, request):
        return render(request, "parent/dash.html")
