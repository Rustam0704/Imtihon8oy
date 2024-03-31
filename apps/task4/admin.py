from django.contrib import admin

from apps.task4.models import (
    Country,
    Players,
    Federation,
    Stadium,
    League,
    Games,
    News,
    Positions,
    Teams,
    Goal,
    RedCard,
    YellowCard,
)

admin.site.register([Country, Federation, Stadium, League])


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "country")
    search_fields = ("name", "country")
    list_filter = ("country",)

    class Meta:
        verbose_name_plural = "Players"
        verbose_name = "Player"


@admin.register(Positions)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        verbose_name_plural = "Positions"
        verbose_name = "Position"


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

    class Meta:
        verbose_name_plural = "News"
        verbose_name = "New"


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ("date",)

    class Meta:
        verbose_name_plural = "Games"
        verbose_name = "Game"


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ("name", "league")

    class Meta:
        verbose_name_plural = "Teams"
        verbose_name = "Team"


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("player", "minut")


@admin.register(RedCard)
class RedCardAdmin(admin.ModelAdmin):
    list_display = ("player", "game")


@admin.register(YellowCard)
class YellowCardAdmin(admin.ModelAdmin):
    list_display = ("player", "game")
