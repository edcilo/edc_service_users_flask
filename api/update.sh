# Update a register in the database

host='http://localhost:5000'
user_id='46a62f85-60a6-400b-987c-c10929fdf987'

curl -si -X PUT \
"${host}/${user_id}" \
-H 'Content-Type: application/json' \
--data-binary @- << EOF
    {
        "email": "jhon.doe+00@example.com",
        "phone": "1231231233",
        "username": "jhon.doe.00"
    }
EOF

