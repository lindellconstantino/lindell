from user_functions import register_user, edit_user

user = None
user_email = None

while True:

    user_input = int(input('''
1.) Show user
2.) Create user
3.) Clear user
4.) Edit user
0.) Exit

What do you want to do?: '''))

    if user_input == 1:

        if user:

            print(f'\n{user} - {user_email}')
        else:
            print('\nNo user found')

    elif user_input == 2:

        new_user = register_user()
        user = new_user['user_name']

        user_email = new_user['email']
        print(f'\nNew User Created! Welcome {new_user["new_user"]}')

    elif user_input == 3:

        user = None
        user_email = None

    elif user_input == 4:

        if user:

            edited_user = edit_user(user)

            user = edited_user['user_name']
            user_email = edited_user['email']

            print(f'\nUser Updated! Welcome {edited_user["new_user"]}')
        else:
            print('\nNo user found')

    else:
        break
