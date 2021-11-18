# Delete a user from the database

user_id='24da0cae-2d93-48e5-bd4e-e45d0b2449d9'

curl -si -X DELETE \
'http://localhost:5000/${user_id}'

