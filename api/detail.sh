# Get the detail of a specific user

user_id='24da0cae-2d93-48e5-bd4e-e45d0b2449d9'
host='http://localhost:5000'

curl -si -X GET \
"${host}/${user_id}"

