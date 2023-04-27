import pytest
from src.user import User


@pytest.fixture(scope='module')
def user_fixture():
    # create a user -> precondition
    user_name = User.username
    user = dict(name=user_name)  # user.create()

    print(f"User '{user_name}' created")

    # execute test -> test step
    yield user

    # remove user -> post condition
    user = None  # user.remove()

    print(f"User '{user_name}' removed")


def pytest_html_report_title(report):
    report.title = "TE Apr 2023"
