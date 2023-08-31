from lib import CONN, CURSOR

class Player:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Player(id={self.id}, name={self.name})"

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        """

        CURSOR.execute(sql)

    @classmethod
    def query_all(cls):
        rows = CURSOR.execute("SELECT * FROM players").fetchall()
        return [ Player(r[1], r[0]) for r in rows ]
    
    def favorite_game(self):
        #returns the game that a player has played the most (highest hours played)
        pass
