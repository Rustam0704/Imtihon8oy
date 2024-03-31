from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.generics import ListAPIView
from .models import Vacancy
from .serializers import VacancySerializer


class VacancyListView(ListAPIView):
    serializer_class = VacancySerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "salary_from",
                openapi.IN_QUERY,
                description="Minimum salary",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "salary_to",
                openapi.IN_QUERY,
                description="Maximum salary",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "salary",
                openapi.IN_QUERY,
                description="Exact salary",
                type=openapi.TYPE_NUMBER,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        salary_from = self.request.query_params.get("salary_from")
        salary_to = self.request.query_params.get("salary_to")
        salary = self.request.query_params.get("salary")

        if salary_from is not None:
            queryset = queryset.filter(salary__gte=salary_from)
        if salary_to is not None:
            queryset = queryset.filter(salary__lte=salary_to)
        if salary is not None:
            queryset = queryset.filter(salary=salary)

        return queryset


__all__ = ("VacancyListView",)
