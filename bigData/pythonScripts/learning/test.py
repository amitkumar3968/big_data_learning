Lloyd = {
    "name":"Lloyd",
    "homework": [90,97,75,92],
    "quizzes": [ 88,40,94],
    "tests": [ 75,90]
    }
Alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }
Tyler = {
    "name":"Tyler",
    "homework": [0,87,75,22],
    "quizzes": [0,75,78],
    "tests": [100,100]
    }
    
def average(list):
	total = sum(list)
	average = total / len(list)
	return average
	
def getAverage(dict):
	avg_home = 0
	avg_quiz = 0
	avg_test = 0
	total_avg = 0
	avg_home = average(dict["homework"]) * 0.10
	avg_quiz = average(dict["quizzes"]) * 0.30
	avg_test = average(dict["tests"]) * 0.60
	print avg_home
	print avg_quiz
	print avg_test
	print "======="
	total_avg = avg_home + avg_quiz + avg_test
	print total_avg


getAverage(Lloyd)

