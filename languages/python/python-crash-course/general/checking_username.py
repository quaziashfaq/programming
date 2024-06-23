#!/usr/bin/env python3


current_users = ['aynan', 'ayat', 'afsana', 'alima', 'admin']
new_users = ['sanvi', 'haniah', 'daniya', 'aaya', 'jazmin', 'alima', 'ayat']

for new_user in new_users:
    if new_user in current_users:
        print(f'This username {new_user} is already taken! Enter a new username')
    else:
        print(f'Username {new_user} is available!')
