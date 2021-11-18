# Update a register in the database

user_id='24da0cae-2d93-48e5-bd4e-e45d0b2449d9'

curl -si -X PUT \
'http://localhost:5000/${user_id}' \
-H 'Content-Type: application/json' \
--data-binary @- << EOF
    {
        "email": "jhon.doe+00@example.com",
        "phone": "1231231232",
        "username": "jhon.doe.00"
    }
EOF

