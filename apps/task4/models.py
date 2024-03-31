from django.db import models
from django.db.models import CASCADE, DO_NOTHING

from apps.shared.models import AbstractModel
from apps.task1.models import User


class Country(AbstractModel):
    name = models.CharField(max_length=128)
    flag = models.ImageField(upload_to="flags/%Y/%m/%d")

    def __str__(self):
        return self.name


class Federation(AbstractModel):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(
        Country, on_delete=DO_NOTHING, related_name="federations"
    )
    logo = models.ImageField(
        upload_to="federation/%Y/%m/%d", default="logo federation.jpg"
    )

    def __str__(self):
        return self.name


class League(AbstractModel):
    name = models.CharField(max_length=128)
    federation = models.ForeignKey(Federation, CASCADE, related_name="leagues")
    logo = models.ImageField(upload_to="league/", default="logo league.jpg")

    def __str__(self):
        return self.name


class Stadium(AbstractModel):
    name = models.CharField(max_length=128)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Teams(AbstractModel):
    name = models.CharField(max_length=128)
    league = models.ForeignKey(League, CASCADE, related_name="clubs")
    logo = models.ImageField(upload_to="teams/", default="logo teams.jpg")
    stadium = models.ForeignKey(Stadium, CASCADE, related_name="clubs")
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    goals_due = models.IntegerField(default=0)

    @property
    def games_count(self):
        return self.home_games.count() + self.away_games.count()

    @property
    def goal_count(self):
        return self.goals.count()

    def __str__(self):
        return f"{self.name} - {self.league}"


class Positions(AbstractModel):
    name = models.CharField(max_length=128)


class Players(AbstractModel):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=DO_NOTHING, related_name="players")
    age = models.IntegerField()
    position = models.ForeignKey(Positions, DO_NOTHING, related_name="players")
    market_value = models.IntegerField()
    Contract_expires = models.DateField()
    team = models.ForeignKey(Teams, DO_NOTHING, related_name="players")
    avatar = models.ImageField(
        upload_to="players/%country/%federation/%team/", default="player.jpg"
    )
    games = models.IntegerField(default=0)

    @property
    def goal_count(self):
        return self.goals.count()

    @property
    def assist_count(self):
        return self.assists.count()

    @property
    def redcards_count(self):
        return self.red_cards.count()

    @property
    def yellow_cards_count(self):
        return self.yellow_cards.count()

    def __str__(self):
        return f"{self.name} - {self.team}-{self.games}/{self.goals}"


class News(AbstractModel):
    title = models.CharField(max_length=128)
    content = models.TextField()
    team = models.ForeignKey(
        Teams, DO_NOTHING, related_name="news", null=True, blank=True
    )
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=DO_NOTHING, related_name="news")

    def __str__(self):
        return f"{self.title}"


class NewsFederartion(AbstractModel):
    news = models.ManyToManyField(News)
    federation = models.ManyToManyField(Federation, related_name="news")


class Referee(AbstractModel):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=DO_NOTHING, related_name="referees")

    @property
    def games_count(self):
        return self.games.count()

    def __str__(self):
        return f"{self.name}"


class Games(AbstractModel):
    date = models.DateField()
    finished = models.BooleanField(default=False)
    home_team = models.ForeignKey(
        Teams, on_delete=DO_NOTHING, related_name="home_games"
    )
    away_team = models.ForeignKey(
        Teams, on_delete=DO_NOTHING, related_name="away_games"
    )
    stadium = models.ForeignKey(Stadium, on_delete=CASCADE)
    league = models.ForeignKey(League, on_delete=CASCADE)
    referee = models.ForeignKey(Referee, on_delete=CASCADE, related_name="games")

    def __str__(self):
        return f"{self.home_team} - {self.away_team} - {self.date}"


class Goal(AbstractModel):
    player = models.ForeignKey(Players, on_delete=DO_NOTHING, related_name="goals")
    minut = models.TimeField()
    team = models.ForeignKey(Teams, on_delete=DO_NOTHING, related_name="goals")
    game = models.ForeignKey("Games", on_delete=DO_NOTHING, related_name="goals")

    def __str__(self):
        return f"{self.player} - {self.game} - {self.team}"


class Assistant(AbstractModel):
    player = models.ForeignKey(Players, on_delete=CASCADE, related_name="assists")
    team = models.ForeignKey(Teams, on_delete=DO_NOTHING)
    game = models.ForeignKey(Games, on_delete=CASCADE)
    goal = models.ForeignKey(Goal, on_delete=CASCADE)

    def __str__(self):
        return f"{self.player} - {self.game} - {self.team}"


class Comment(AbstractModel):
    author = models.ForeignKey(User, on_delete=DO_NOTHING)
    text = models.TextField()
    game = models.ForeignKey(Games, on_delete=DO_NOTHING, related_name="comments")

    def __str__(self):
        return f"{self.author} - {self.game}"


class YellowCard(AbstractModel):
    player = models.ForeignKey(Players, on_delete=CASCADE, related_name="yellow_cards")
    game = models.ForeignKey(Games, on_delete=DO_NOTHING, related_name="yellow_cards")
    minut = models.TimeField()

    def __str__(self):
        return f"{self.player} - {self.game} - {self.minut}"


class RedCard(AbstractModel):
    player = models.ForeignKey(Players, on_delete=DO_NOTHING, related_name="red_cards")
    game = models.ForeignKey(Games, on_delete=DO_NOTHING, related_name="red_cards")
    minut = models.TimeField()

    def __str__(self):
        return f"{self.player} - {self.game} - {self.minut}"
