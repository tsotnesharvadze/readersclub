

def get_code(user_id):
	code=((user_id*2+10)**2)*(-1)
	return code


def get_id(code):
	try:
		user_id=int((((-1)*code)**0.5-10)/2)
	except:
		user_id=int(((-1)*code**0.5-10)/2)

	return user_id


