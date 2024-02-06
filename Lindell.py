from user_functions import register_user, edit_user

user = ' '
user email ' '

while True:

	user_input = input('''
1.) show user
2.) create user 
3.) clear user
4.) edit user
0.) exit

what do you think to do?: ''')

   if user_input == '1':

   	if user != '':
   		print(f'\n{user} - {user_email}')
   	else:
   	    print('\nNo user found')	

   elif user_input == '2':

       new_user = register_user()
       user = new_user['user_name']
       user_email = new_user['email']
     
       print(f'\nNew User Created| Welcome { new_user ["user_name "]}')

    elif user_input == '3':

   	user = ' '
   	user_ email = ' '

    elif user_input == '4':

       edited_user = edit_user(user) 
 
       user = edited_user = edit_user['user_name']

       user = editted_user ['user_name']
       user_email = editted_user ['email']

   else:
   	   break 


