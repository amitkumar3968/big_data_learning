def reverse(string):
	new_string = ""
	for item in range(len(string)-1, -1, -1):
		new_string = new_string + string[item]
	return new_string


reverse("Zubair AHMED")
