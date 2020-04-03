# -*- coding: utf-8 -*-
"""This module defines the ConstantTeambuilder class, which is a subclass of
ShowdownTeamBuilder that yields a constant team.
"""
from poke_env.teambuilder.teambuilder import Teambuilder


class ConstantTeambuilder(Teambuilder):
    def __init__(self, team):
        if "|" in team:
            self.converted_team = team
        else:
            self.converted_team = self.convert_showdown_to_packed(team)

    def yield_team(self):
        return self.converted_team
