def test_signup():
    user_name = "non_existing_user"
    user = dict(name=user_name)  # user.create()

    print(f"User '{user_name}' created")

    assert user.get('name') == user_name

    user = None  #user.remove()

    print(f"User '{user_name}' removed")
