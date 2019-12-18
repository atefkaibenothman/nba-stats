# Holds all Player info
class Player:
    def __init__(self, id, full_name, first_name, last_name, is_active):
        self.id = id
        self.full_name = full_name
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.game_log = dict()

    def get_id(self):
        return self.id

    def get_full_name(self):
        return self.full_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_is_active(self):
        return is_active

    def get_player_stats(self):
        for game_id, stats in self.game_log.items():
            print(f'matchup: {stats["matchup"]}')
            print(f'game_date: {stats["game_date"]}')
            print(f"game_id: {game_id}")
            print("-------------------")
            print(f'won/lose: {stats["win_lose"]}')
            print(f'min_played: {stats["min_played"]}')
            print(f'points: {stats["pts"]}')
            print(f'assists: {stats["ast"]}')
            print(f'steals: {stats["stl"]}')
            print(f'blocks: {stats["blk"]}')
            print()

    def add_game_log_entry(self, player_game_log):
        for game in player_game_log:
            game_id = game["Game_ID"]
            self.game_log[game_id] = dict()
            self.game_log[game_id]["season_id"] = game["SEASON_ID"] # season ID
            self.game_log[game_id]["game_date"] = game["GAME_DATE"] # game date
            self.game_log[game_id]["matchup"] = game["MATCHUP"] # team vs. team
            self.game_log[game_id]["win_lose"] = game["WL"] # win/lose
            self.game_log[game_id]["min_played"] = game["MIN"]  # minutes played
            self.game_log[game_id]["fgm"] = game["FGM"] # field goals made
            self.game_log[game_id]["fga"] = game["FGA"] # field goals attempted
            self.game_log[game_id]["fg_pct"] = game["FG_PCT"] # field goal percentage
            self.game_log[game_id]["fg3m"] = game["FG3M"] # 3point field goals made
            self.game_log[game_id]["fg3a"] = game["FG3A"] # 3point field goals attempted
            self.game_log[game_id]["fg3_pct"] = game["FG3_PCT"] # 3point field goal percentage
            self.game_log[game_id]["ftm"] = game["FTM"] # free throws made
            self.game_log[game_id]["fta"] = game["FTA"] # free throws attempted
            self.game_log[game_id]["ft_pct"] = game["FT_PCT"] # free throw percentage
            self.game_log[game_id]["oreb"] = game["OREB"] # offensive rebounds
            self.game_log[game_id]["dreb"] = game["DREB"] # defensive rebounds
            self.game_log[game_id]["tot_reb"] = game["REB"] # total rebounds
            self.game_log[game_id]["ast"] = game["AST"] # assists
            self.game_log[game_id]["stl"] = game["STL"] # steals
            self.game_log[game_id]["blk"] = game["BLK"] # blocks
            self.game_log[game_id]["tov"] = game["TOV"] # turnovers
            self.game_log[game_id]["pf"] = game["PF"] # personal fouls
            self.game_log[game_id]["pts"] = game["PTS"] # points
            self.game_log[game_id]["plus_minus"] = game["PLUS_MINUS"] # plus/minus