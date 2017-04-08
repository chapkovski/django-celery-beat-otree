from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
testing periodic task that starts when a player accesses the first page
"""


class Constants(BaseConstants):
    name_in_url = 'bigfive'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    ...
