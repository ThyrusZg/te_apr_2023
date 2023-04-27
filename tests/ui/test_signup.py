from src.user import User


def test_signup_initial():
    user = dict(name="non_existing_user")
    assert user["name"] == "non_existing_user"
    user = None


def test_signup(user_fixture):
    assert user_fixture.get('name') == User.username


def test_signup_negative(user_fixture):
    assert user_fixture.get('name') == "user"
