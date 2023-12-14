"""
curl -H "Authorization: Token bb828cdbf41db326a78c8f51b275353f90e7c9e3" http://127.0.0.1:8000/core/subjects/

curl -X POST -H "Authorization: Token a8cfc8d88057fa5de033dd2a0c3b94b4bbf27c2b" -H "Content-Type: application/json" -d '{"title": "English", "code": "ENG"}' http://127.0.0.1:8000/core/subjects/



"id": 1,
    "title": "SENIOR SECONDARY SCHOOL 3",
    "code": "JSS 1",
    "capacity": 100,
    "stream": "C"

i noticed the classroom code should be generated based on the title to avoid errors as shown above

"""