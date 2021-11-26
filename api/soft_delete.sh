# Soft delete account

host='http://localhost:5000'
user_id='d3887fda-d884-4d32-9b8d-1d6db6e89c7e'

curl -si -X DELETE \
"${host}/${user_id}" \
-H 'Content-Type: application/json' \

