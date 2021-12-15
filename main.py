from python.encryption import encrypt_pwd
from website import create_app
from sys import exit, argv


def test_env():
    pass


if __name__ == "__main__":
    if (int(argv[1])):
        test_env()
    else:
        app = create_app()
        app.run(debug=True)
    exit()
