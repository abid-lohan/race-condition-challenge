from app import app, db
from models import User, Burger

def create_users():
    user1 = User(username='ruhptura', wallet=100.00)
    user1.set_password('123')
    user2 = User(username='js0n', wallet=100.00)
    user2.set_password('123')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Usuários criados com sucesso.")

def create_burgers():
    burger1 = Burger(name='Hanbúrguer de Siri', price=20.00, image='https://media.discordapp.net/attachments/888101596796452937/1253732999909085264/siri.png?ex=6676ed58&is=66759bd8&hm=57a74a8b02e38c1c684872866a7d32379d1c28bf9d9b48bd149c95b187555c3a&=&format=webp&quality=lossless')
    burger2 = Burger(name='Hambúrguer Grisalho', price=1337.00, image='https://media.discordapp.net/attachments/888101596796452937/1253732999669878874/grisalho.png?ex=6676ed58&is=66759bd8&hm=b395d2f360496a472bc4ab6052b52c63e82ab9faf58bd6f65e73577bcb6dae2a&=&format=webp&quality=lossless')

    db.session.add(burger1)
    db.session.add(burger2)
    db.session.commit()
    print("Hambúrgueres criados com sucesso.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_users()
        create_burgers()