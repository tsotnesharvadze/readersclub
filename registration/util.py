

def get_code(user_id):
	code=(user_id*2+10)**2
	return code


def get_id(code):
	user_id=int((code**0.5-10)/2)

	return user_id


