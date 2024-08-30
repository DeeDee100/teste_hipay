from .database.database import SessionLocal
from .database.models import User, Claims, Roles, UserClaims

def create_data():
    session = SessionLocal()
    users = [
        User(name="Dee Dee", email="dee@mail.com", password="1234556", role_id=1),
        User(name="Alice", email="alice@mail.com", password="1234556", role_id=2),
        User(name="Bob", email="bob@mail.com", password="1234556", role_id=3)
    ]
    
    roles = [
        Roles(id=1, description='Admin'),
        Roles(id=2, description='User'),
        Roles(id=3, description='Guest')
    ]
    
    claims = [
        Claims(description="Read", active=True),
        Claims(description="Write", active=True),
        Claims(description="Delete", active=True),
        Claims(description="GODMODE", active=True)
    ]
    
    user_claims = [
        UserClaims(user_id=1, claim_id=4),
        UserClaims(user_id=2, claim_id=1),
        UserClaims(user_id=3, claim_id=2)
    ]
    
    try:
        session.bulk_save_objects(roles,)
        session.bulk_save_objects(users)
        session.bulk_save_objects(claims)
        session.bulk_save_objects(user_claims)
        session.commit()
    except:
        return

