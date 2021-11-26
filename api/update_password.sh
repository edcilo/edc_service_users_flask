# Update password

host='http://localhost:5000'
user_id='46a62f85-60a6-400b-987c-c10929fdf987'

curl -si -X PUT \
"${host}/${user_id}/reset-password" \
-H 'Content-Type: application/json' \
--data-binary @- << EOF
    {
        "current_password": "secret",
        "password": "newsecret",
        "password_confirmation": "newsecret"
    }
EOF
