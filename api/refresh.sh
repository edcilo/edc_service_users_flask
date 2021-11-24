# Refresh autorization token

host='http://localhost:5000'
token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImYyZGYyYWMyLTUzNWYtNDM0ZS1iZjVlLTMzZmVmZjhiOTg3NCIsImV4cCI6MTYzNzc3Njg4Mn0.bqRA8coU6KBNHE7g9XckwTczSBei4I34aQbFSt5VJKc'

curl -si -X POST \
"${host}/refresh" \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer ${token}"
