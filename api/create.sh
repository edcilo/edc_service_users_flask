# Create a new user in the database

host='http://localhost:5000'

curl -si -X POST \
"${host}/" \
-H 'Content-Type: application/json' \
--data-binary @- << EOF
    {
        "email": "jhon.doe+01@example.com",
        "phone": "1231231231",
        "username": "jhon.doe.01",
        "password": "secret"
    }
EOF

