from website import create_app
from python.encryption import encrypt_pwd
from sys import exit


def test_env():
    pass


if __name__ == "__main__":
    if (1):
        test_env()
    else:
        app = create_app()
        app.run(debug=True)
    exit()
