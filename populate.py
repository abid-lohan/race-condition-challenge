from app import app, db
from models import User, Burger

def create_users():
    user1 = User(username='john_doe')
    user1.set_password('password123')
    user2 = User(username='jane_doe')
    user2.set_password('password123')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Users created successfully.")

def create_burgers():
    burger1 = Burger(name='Classic Burger', price=5.99)
    burger2 = Burger(name='Cheese Burger', price=6.99)
    burger3 = Burger(name='Bacon Burger', price=7.99)

    db.session.add(burger1)
    db.session.add(burger2)
    db.session.add(burger3)
    db.session.commit()
    print("Burgers created successfully.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_users()
        create_burgers()