"""было"""
import random

class Gamer:
    
    def __init__(self, id, name, surname, national, team, types, status, age, speed, cnt_games, cnt_seasons, cnt_goals, cnt_pass_boals):
        self.player_id = id # уникальный идентификатор игрока (счётчик)
        self.first_name = name # Имя игрока
        self.second_name = surname # Фамилия игрока
        self.national = national # Национальность игрока
        self.team = team # Команда игрока
        self.types = types # Нападающий, защитник, полузащитник, полунападающий, вратарь
        self.status = status # текущий статус футболиста
        self.age = age # Возраст
        self.speed = speed # скорость футболиста
        self.cnt_games = cnt_games # Количество сыигранных игр
        self.cnt_seasons = cnt_seasons # Количество сыигранных сезонов
        self.cnt_goals = cnt_goals # Количество забитых мячей
        self.cnt_pass_boals = cnt_pass_boals # Количество пропущенных мечей (для вратарей)
    
    def Run(self, new_speed):
        self.speed = new_speed
    
    def Stop(self):
        self.speed = 0
    
    def Status(self, new_status): # статус футболиста например выдана красная карточка или желтая тогда футболист обнуляет скорость и меняет статус на скамейка
        self.status = new_status
        if new_status == "Red":
            self.Stop()
        elif new_status == "Yellow":
            i += 1
            if i >= 2:
                self.Stop()
        else:
            self.Run(10)
    
    def Goals(self, new_goal):
        self.cnt_goals += new_goal
        
    def Games(self, new_game):
        self.cnt_games += new_game
    
    def Seasons(self, new_season):
        self.cnt_seasons += new_season
    
    def Passed_boal(self, new_pas_boal):
        self.cnt_pass_boals += new_pas_boal

ronaldo = Gamer(1, "Ronaldo", "Ricaro", "Brasil", "Динамо", "Нападающий", "Green", 23, 10, 10, 10, 100, 0)
ronaldo.Status("Red")
ronaldo.Status("Green")
ronaldo.Goals(200)
ronaldo.Games(10)
ronaldo.Seasons(5)




class Teams:

    def __init__(self, id, name, city, status, season, cnt_seasons, games, cnt_win, cnt_win_seasons, cnt_boals):
        self.id_team = id
        self.name = name # наименование команды
        self.city = city # город команды
        self.status = status # статус команды не Pass значит команда в сезоне, если pass сезон анлируется и команда дисквалифицирована
        self.season = season # Текущий сезон
        self.cnt_seasons = cnt_seasons # Количество сыигрианных сезонов
        self.games = games # Количество игр
        self.cnt_win = cnt_win # Количество выигранных игр
        self.cnt_win_seasons = cnt_win_seasons # Количество выигранных сезонов
        self.cnt_boals = cnt_boals # Общее количество забитых мечей командой
    
    def sum_season(self, season):
        self.cnt_seasons += season
    
    def sum_games(self, game):
        self.games += game
    
    def sum_win(self, win):
        self.cnt_win += win
    
    def sum_win_seasons(self, win_season):
        self.cnt_win_seasons += win_season
    
    def status_team(self, status):
        self.status = status
        if status == "Pass":
            self.cnt_seasons -= 1
        else:
            self.cnt_seasons += 1

dinamo = Teams(1, "Динамо", "Москва", "Active", 2020, 130, 872, 766, 98, 3333)
dinamo.status_team("Pass")
dinamo.status_team("Active")
dinamo.sum_season(10)
dinamo.sum_games(100)
dinamo.sum_win(90)
dinamo.sum_win_seasons(8)
"""стало"""
class Player:
    
    def __init__(self, id, name, surname, national, team, types, status, age, speed, cnt_games, cnt_seasons, cnt_goals, cnt_pass_boals):
        self.player_id = id # уникальный идентификатор игрока (счётчик)
        self.first_name = name # Имя игрока
        self.second_name = surname # Фамилия игрока
        self.national = national # Национальность игрока
        self.team = team # Команда игрока
        self.types = types # Нападающий, защитник, полузащитник, полунападающий, вратарь
        self.status_player = status # текущий статус футболиста
        self.age = age # Возраст
        self.current_speed_player = speed # скорость футболиста
        self.games_sum = cnt_games # Количество сыигранных игр
        self.cnt_seasons = cnt_seasons # Количество сыигранных сезонов
        self.goals_sum = cnt_goals # Количество забитых мячей
        self.pass_boals_sum = cnt_pass_boals # Количество пропущенных мечей (для вратарей)
    
    def set_run_player(self, new_speed):
        self.current_speed_player = new_speed
    
    def set_stop_player(self):
        self.current_speed_player = 0
    
    def set_status_player(self, new_status): # статус футболиста например выдана красная карточка или желтая тогда футболист обнуляет скорость и меняет статус на скамейка
        self.status_player = new_status
        if new_status == "Red":
            self.set_stop_player()
        elif new_status == "Yellow":
            i += 1
            if i >= 2:
                self.set_stop_player()
        else:
            self.set_run_player(10)
    
    def set_goals(self, new_goal):
        self.goals_sum += new_goal
        
    def set_game(self, new_game):
        self.games_sum += new_game
    
    def set_season(self, new_season):
        self.cnt_seasons += new_season
    
    def set_passed_boal(self, new_pas_boal):
        self.pass_boals_sum += new_pas_boal

ronaldo = Player(1, "Ronaldo", "Ricaro", "Brasil", "Динамо", "Нападающий", "Green", 23, 10, 10, 10, 100, 0)
ronaldo.set_status_player("Red")
ronaldo.set_status_player("Green")
ronaldo.set_goals(200)
ronaldo.set_game(10)
ronaldo.set_season(5)




class Team:

    def __init__(self, id, name, city, status, season, cnt_seasons, games, cnt_win, cnt_win_seasons, cnt_boals):
        self.id_team = id
        self.name = name # наименование команды
        self.city = city # город команды
        self.set_status = status # статус команды не Pass значит команда в сезоне, если pass сезон анлируется и команда дисквалифицирована
        self.season = season # Текущий сезон
        self.seasons_cnt = cnt_seasons # Количество сыигрианных сезонов
        self.games_sum = games # Количество игр
        self.win_sum = cnt_win # Количество выигранных игр
        self.win_seasons_sum = cnt_win_seasons # Количество выигранных сезонов
        self.cnt_boals = cnt_boals # Общее количество забитых мечей командой
    
    def set_season(self, season):
        self.seasons_cnt += season
    
    def set_games(self, game):
        self.games_sum += game
    
    def set_win(self, win):
        self.win_sum += win
    
    def set_win_seasons(self, win_season):
        self.win_seasons_sum += win_season
    
    def set_status_team(self, status):
        self.set_status = status
        if status == "Pass":
            self.seasons_cnt -= 1
        else:
            self.seasons_cnt += 1

dinamo = Team(1, "Динамо", "Москва", "Active", 2020, 130, 872, 766, 98, 3333)
dinamo.set_status_team("Pass")
dinamo.set_status_team("Active")
dinamo.set_season(10)
dinamo.set_games(100)
dinamo.set_win(90)
dinamo.set_win_seasons(8)