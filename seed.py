from models import session, User, CalculationHistory

def seed_data():
    user1 = User(name="John Doe", email="john@example.com")
    user2 = User(name="Jane Smith", email="jane@example.com")
    session.add_all([user1, user2])
    session.commit()

    history1 = CalculationHistory(user_id=1, operation="add", input_data="2, 3", result=5.0)
    history2 = CalculationHistory(user_id=2, operation="divide", input_data="10, 2", result=5.0)
    session.add_all([history1, history2])
    session.commit()

if __name__ == "__main__":
    seed_data()
