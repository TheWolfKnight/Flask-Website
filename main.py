from website import create_app
from sys import exit

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    exit()
