from pathlib import Path
import json
 
def get_sorted_user():
	'''获取存储的用户名'''
	path=Path("username.json")
	try:
		content=path.read_text()
		user_name=json.load(content)
	except FileNotFoundError:
		return None
	else:
		return user_name
 
def get_new_user():
	'''获取新的用户名'''
	user_name=input("Enter your name: ")
	path=Path("username.json")
	content=json.dumps(user_name)
	return user_name
 
def greet():
	'''问候用户并指出名字'''
	user=get_sorted_user()
	if user:
		print("Welcome "+user)
		ask=input("Am I right? Enter 'y' or 'no': ")
		if ask=='y':
			pass
		elif ask=='n':
			user=get_new_user()
			print("Welcome "+user)
	else:
		user=get_new_user()
		print("Welcome "+user)
greet()