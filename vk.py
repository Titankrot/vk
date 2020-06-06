import vk


V=5.107

def auth():
	session = vk.AuthSession(app_id='5340228', user_login=input("Login: "), user_password=input("Password: "))
	return vk.API(session)

def get_id():
	user = input("User_id: ")
	if user == "exit":
		return
	user_info = api.users.get(user_ids=user, v=V)[0]
	return user_info['id']

def get_friends():
	return api.friends.get(user_id=id, v=V)["items"]

def get_names(ids):
	return api.users.get(user_ids=ids, v=V)

if __name__ == "__main__":
	api = auth()
	while True:
		id = get_id()
		if id is None:
			break
		for i in get_names(get_friends()):
			print("Id: {0}, Name: {1} {2}".format(i["id"], i["first_name"], i["last_name"]))

		