from django.contrib import admin

from apps.task2.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    class Meta:
        model = Vacancy
        fields = "__all__"
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
