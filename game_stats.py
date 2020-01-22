import re

file = 'high_score.txt'

class GameStats():

	def __init__(self, ai_settings):

		self.ai_settings = ai_settings
		self.reset_stats()

		self.game_active = False

		with open(file, 'r') as file_object:
			self.high_score = int(re.sub(',','', file_object.read()))

	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit

		self.score = 0
		self.level = 1