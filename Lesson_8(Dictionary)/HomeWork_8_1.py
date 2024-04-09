#There is a system where there are lists of users.
#roles = { 'admin' : [...], 'maintainer' : [...], 'manager' : [...], 'developer': [...]} - names should be written in these lists users.
#When entering a name, it is necessary to check to which role this person belongs and display a message of the type: "Hello, <role>"
#If the name is not in the lists, output: "Hello, Guest"
roles = {'admin': [...], 'maintainer': [...], 'manager': [...], 'developer': [...]}
roles['Quentin'] = 'admin',
roles['Guillermo'] = 'maintainer',
roles['Martin'] = 'manager',
roles['Alfred'] = 'developer'
user_name = input("Введіть ваше ім'я: ")
if user_name in roles:
    print(f"Hello,{user_name} your role in project is {roles[user_name]}!")
else:
    print("Hello, Guest.")




