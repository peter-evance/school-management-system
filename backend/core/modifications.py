"""
curl -H "Authorization: Token 861ed9885fac5bc25d0a98e4b8e9ff925ff56237" http://127.0.0.1:8000/core/subjects/

curl -X POST -H "Content-Type: application/json" -d '{"title": "English", "code": "ENG"}' http://127.0.0.1:8000/core/subjects/


"id": 1,
    "title": "SENIOR SECONDARY SCHOOL 3",
    "code": "JSS 1",
    "capacity": 100,
    "stream": "C"

i noticed the classroom code should be generated based on the title to avoid errors as shown above

"""