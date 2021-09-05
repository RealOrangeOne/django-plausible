from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("simple", TemplateView.as_view(template_name="simple.html")),
    path("simple-wagtail", TemplateView.as_view(template_name="simple_wagtail.html")),
]
