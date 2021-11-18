# Create a new user in the database


curl -si -X POST \
'http://localhost:5000/' \
-H 'Content-Type: application/json' \
--data-binary @- << EOF
    {
        "email": "jhon.doe+00@example.com",
        "phone": "1231231232",
        "username": "jhon.doe.00",
        "password": "secret"
    }
EOF

