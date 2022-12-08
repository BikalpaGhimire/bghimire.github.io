from flask_frozen import Freezer
from main_website import myweb

freezer = Freezer(myweb)

if __name__ == '__main__':
    freezer.freeze()