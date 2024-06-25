from app import app, db
from models import User, Burger

def create_users():
    user1 = User(username='ruhptura', wallet=100.00, version=0)
    user1.set_password('123')
    user2 = User(username='js0n', wallet=100.00, version=0)
    user2.set_password('123')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Usuários criados com sucesso.")

def create_burgers():
    burger1 = Burger(name='Hambúrguer de Siri', price=20.00, image='https://i.ibb.co/XZVKyrh/siri.png')
    burger2 = Burger(name='Hambúrguer Grisalho', price=1337.00, image='https://i.ibb.co/34zjrGh/grisalho.png')

    db.session.add(burger1)
    db.session.add(burger2)
    db.session.commit()
    print("Hambúrgueres criados com sucesso.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_users()
        create_burgers()