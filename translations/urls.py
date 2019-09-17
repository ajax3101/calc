from django.urls import path

from translations.views import TranslateView

app_name = 'translations'

urlpatterns = [
    path('', TranslateView.as_view(), name='index'),
]
