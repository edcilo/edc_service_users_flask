# Retrieve an autorization token

host='http://localhost:5000'

curl -si -X POST \
"${host}/login" \
-H 'Content-Type: application/json' \
--data-binary @- << EOF
    {
        "username": "jhon.doe.09",
        "password": "secret"
    }
EOF
