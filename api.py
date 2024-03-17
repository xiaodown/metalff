from datetime import datetime
import psycopg2
import settings

# Sucks, obviously completely bullshit


def pg_client():
    return psycopg2.connect(
        dbname=settings.PG_DATABASE or 'metalff',
        user=settings.PG_USER or 'postgres',
        password=settings.PG_PASSWORD,
        host=settings.PG_HOST or 'localhost',
        port=settings.PG_PORT or 5432
    )


class User:
    def __init__(self, username, teams=None):
        self.created_at = datetime.now()
        self.username = username
        self.teams = teams if teams else []

    def add_team(self, team):
        self.teams.append(team)

    def remove_team(self, team):
        if team in self.teams:
            self.teams.remove(team)

    def get_teams(self):
        return self.teams

class Team:
    def __init__(self, name, guitar1, guitar2, bass, drummer, vocalist, season_id):
        self.name = name
        self.guitar1 = guitar1
        self.guitar2 = guitar2
        self.bass = bass
        self.drummer = drummer
        self.vocalist = vocalist
        self.founded_on = datetime.now()
        self.season_id = season_id

    def get(self):
        return {
            'name': self.name,
            'guitar1': self.guitar1,
            'guitar2': self.guitar2,
            'bass': self.bass,
            'drummer': self.drummer,
            'vocalist': self.vocalist,
            'founded_on': self.founded_on,
            'season_id': self.season_id
        }