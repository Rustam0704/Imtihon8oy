from django.urls import path

from apps.task2.views import VacancyListView

urlpatterns = [
    path("vacancy/", VacancyListView.as_view()),
]
