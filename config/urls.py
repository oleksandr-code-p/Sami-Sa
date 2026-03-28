from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('alphabet/', include('alphabet.urls')),
    path('lessons/', include('lessons.urls')),
    path("exercises/", include("exercises.urls")),
    path('theory/', TemplateView.as_view(template_name='theory/dashboard.html'), name='theory_dashboard'),

    path('theory/sentences/', TemplateView.as_view(template_name='theory/sentences.html'), name='sentences'),
    path('theory/present-simple/', TemplateView.as_view(template_name='theory/present_simple.html'), name='present_simple'),
    path('theory/present-continuous/', TemplateView.as_view(template_name='theory/present_continuous.html'), name='present_continuous'),
    path('theory/past-simple/', TemplateView.as_view(template_name='theory/past_simple.html'), name='past_simple'),
    path('theory/future/', TemplateView.as_view(template_name='theory/future.html'), name='future'),
    path('theory/questions/', TemplateView.as_view(template_name='theory/questions.html'), name='questions'),
    path('theory/negations/', TemplateView.as_view(template_name='theory/negations.html'), name='negations'),
    path('theory/articles/', TemplateView.as_view(template_name='theory/articles.html'), name='articles'),
    path('theory/prepositions/', TemplateView.as_view(template_name='theory/prepositions.html'), name='prepositions'),
]

