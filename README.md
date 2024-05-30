# CrispCare
house care site

how to run this app:
 python3 main.py

how to posta request:
for eg when registering for househelp:

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Jane Doe",
    "age": 32,
    "services": "Cleaning, Babysitting",
    "rating": 4.8
}' http://localhost:5000/api/register_househelp


