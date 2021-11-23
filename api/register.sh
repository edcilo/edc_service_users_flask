# Register a new user

host='http://localhost:5000'

curl -si -X POST \
"${host}/register" \
-H 'Content-Type: application/json' \
--data-binary @- << EOF
    {
        "email": "jhon.doe+09@example.com",
        "phone": "1231231239",
        "username": "jhon.doe.09",
        "password": "secret",
        "password_confirmation": "secret"
    }
EOF
