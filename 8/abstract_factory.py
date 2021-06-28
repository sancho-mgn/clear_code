from __future__ import annotations
from abc import ABC, abstractmethod

class SportsFactory(ABC):
    @abstractmethod
    def create_sportsmen(self):
        pass

    @abstractmethod
    def create_teams(self):
        pass

class SportsmenFactory(SportsFactory):
    def create_teams(self) -> Team:
        return WrestlingTeam()

    def create_sportsmen(self) ->Sportsmen:
        return WrestlingSportsmen()


class TeamFactory(SportsFactory):
    def create_sportsmen(self) ->Sportsmen:
        return WrestlingSportsmen()

    def create_teams(self) -> Team:
        return WrestlingTeam()

class Sportsmen(ABC):
    @abstractmethod
    def __init__(self, number=0, name="E", surname="D", country="F", weidth=100, types="G"):
        self.number = number
        self.name = name
        self.surname = surname
        self.country = country
        self.weidth = weidth
        self.types = types

class FieldEventSportsmen(Sportsmen):
    def set_number(self, new_number):
        self.number = new_number

    def get_number(self):
        return self.number

class WrestlingSportsmen(Sportsmen):
    def set_number(self, new_number):
        self.number = new_number

    def get_number(self):
        return self.number

class Team(ABC):
    @abstractmethod
    def __init__(self, name="E", country="F", types="G"):
        self.name = name
        self.country = country
        self.types = types

class FieldEventTeam(Team):
    def set_name(self, new_number):
        self.number = new_number

    def get_name(self):
        return self.number

class WrestlingTeam(Team):
    def set_name(self, new_number):
        self.number = new_number

    def get_name(self):
        return self.number

def create_judoka(factory: SportsFactory):
    judoka = factory.create_sportsmen()
    judoka_team = factory.create_teams()

if __name__ == '__main__':
    print('Factory Fabric create sportsmen')
    create_judoka(WrestlingSportsmen)
    print()
    create_judoka(WrestlingTeam)