import nflgame as nfl

class Team(object):
	def __init__(self, name):
		self.name = name
	
	def get_name(self):
		return self.name
		

teams = nfl.teams
data = []
for team in teams:
	tmp = Team(team[0])
	data.append(tmp)

for i in range(len(data)):
	print data[i].get_name()
