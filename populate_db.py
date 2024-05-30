from website import db, create_app
from website.models import HouseHelp

app = create_app()
app.app_context().push()

# Add sample data
househelps = [
    HouseHelp(name='Alice', age=30, services='Cleaning', rating=4.5),
    HouseHelp(name='Bob', age=25, services='Cooking', rating=4.7),
    HouseHelp(name='Charlie', age=28, services='Babysitting', rating=4.6)
]

for househelp in househelps:
    db.session.add(househelp)

db.session.commit()

print("Sample data added successfully.")

