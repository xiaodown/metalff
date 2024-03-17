from datetime import datetime
import psycopg2
import settings
import shortuuid
from typing import Optional

def pg_client():
    return psycopg2.connect(
        dbname=settings.PG_DATABASE or 'metalff',
        user=settings.PG_USER or 'postgres',
        password=settings.PG_PASSWORD,
        host=settings.PG_HOST or 'localhost',
        port=settings.PG_PORT or 5432
    )

# Sucks, obviously completely bullshit

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

# Ok, this is more like it, but I have no idea how the sql returns actually will look
# Dear god, I think this is actually going to force me to use an ORM.  
# Is this a django thing?  SqlAlchemy?  Man......

class musician:
    def __init__(self, name, instrument, band_id):
        self.name = name
        self.instrument = instrument
        self.band_id = band_id

    
    def create(self, name: str, instrument: str, band_id: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    INSERT INTO musicians (id, name, instrument, band_id)
                    VALUES (%s, %s, %s, %s)
                ''', (shortuuid.uuid(), name, instrument, band_id))

    def get_by_name(self, name: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    SELECT * FROM musicians WHERE name = %s
                ''', (name,))
                return sql.fetchone()
            
    def get_by_band_id(self, band_id: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    SELECT * FROM musicians WHERE band_id = %s
                ''', (band_id,))
                return sql.fetchall()
    
    def get_by_instrument(self, instrument: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    SELECT * FROM musicians WHERE instrument = %s
                ''', (instrument,))
                return sql.fetchall()

    def get(self, id: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    SELECT * FROM musicians WHERE id = %s
                ''', (id,))
                return sql.fetchone()
    
    def delete(self, id: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    DELETE FROM musicians WHERE id = %s
                ''', (id,))
    
    def get_name(self, id: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    SELECT name FROM musicians WHERE id = %s
                ''', (id,))
                return sql.fetchone()
    
    def get_instrument(self, id: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    SELECT instrument FROM musicians WHERE id = %s
                ''', (id,))
                return sql.fetchone()
    
    def get_band_id(self, id: str):
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    SELECT band_id FROM musicians WHERE id = %s
                ''', (id,))
                return sql.fetchone()
    
    def update(self, id: str, name: Optional[str], instrument: Optional[str], band_id: Optional[str]):
        if not name:
            name = self.get_name(id)
        if not instrument: 
            instrument = self.get_instrument(id)
        if not band_id:
            band_id = self.get_band_id(id)
        with pg_client() as conn:
            with conn.cursor() as sql:
                sql.execute('''
                    UPDATE musicians SET name = %s, instrument = %s, band_id = %s WHERE id = %s
                ''', (name, instrument, band_id, id))