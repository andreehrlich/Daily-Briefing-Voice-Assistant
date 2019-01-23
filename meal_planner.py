# Weekly meal plan

shopping_list = []

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

meals_of_day = ["Brkfst", "Lunch", "Snack1", "Dinner", "Snack2"]

meal_plan_dict = {x: {y: None for y in meals_of_day} for x in days_of_week}

# Iterate through days_of_week and meals_of_day to index meal_plan_dict

for day in days_of_week:
	print "{}:".format(day)
	for meal in meals_of_day:
		print "\t{}:\t{}".format(meal, meal_plan_dict[day][meal])

# Meal Plan = Recipe --> Shopping List

meals = {
	"breakfast" :  [
					"Toast w Peanut Butter",
					"10oz of Greek Yoghurt",
					"Three eggs w vegetables",
					"2 peices of fruit"
					],

	"lunch" : [
				"Spaghetti w vegis",
				"Cup of lentils",
				"Rice w vegis"
				],

	"dinner" : [],

	"snack" = []
	}

class Food:

	def __init__(self, name, amount=None):
		self.serving_size = amount
		self.name = name

	def get_nutrition(self):
		#api call
		pass
