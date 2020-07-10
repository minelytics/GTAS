from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):
    template_name = "parent/dashboard.html"

    def get(self, request):
        return render(request, "parent/dashboard.html")
