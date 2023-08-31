from lib import CONN, CURSOR
from lib.classes.player import Player

class Game:

    # MAGIC METHODS #
    def __init__(self, name, hours_played, player_id, id=None):
        self.name = name
        self.hours_played = hours_played
        self.player_id = player_id
        self.id = id
    
    def __repr__(self):
        return f"Game(id={self.id} name={self.name}, hours_played={self.hours_played}, player_id={self.player_id})"

    # CLASS METHODS #
    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        name TEXT,
        hours_played INTEGER,
        player_id INTEGER
        )
        """
        CURSOR.execute(sql)
    
    @classmethod
    def query_all(cls):
        sql="SELECT * FROM games"
        rows = CURSOR.execute(sql).fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def query_by_id(cls, id):
        sql="SELECT * FROM games WHERE id = ?"
        row = CURSOR.execute(sql, [id]).fetchone()
        return Game(row[1], row[2], row[3], row[0])
    
    @classmethod
    def favorite_game(self):
        #using subquery here to get the whole row of the highest hours_played
        sql="SELECT * FROM games WHERE hours_played = (SELECT max(hours_played) FROM games)"
        row = CURSOR.execute(sql).fetchone()
        return Game(row[1], row[2], row[3], row[0])
    
    @classmethod
    def average_playtime(self):
        sql="SELECT avg(hours_played) FROM games"
        return f"{CURSOR.execute(sql).fetchone()[0]} hours"

    # PROPERTIES #
    @property
    def hours_played(self):
        return self._hours_played
    
    @hours_played.setter
    def hours_played(self, value):
        if (type(value) == int) and value > 0:
            self._hours_played = value
        else:
            raise ValueError("you haven't been playing long enough")
        
    @property
    def player(self):
        sql="SELECT * FROM players WHERE id = ?"
        row = CURSOR.execute(sql, [self.player_id]).fetchone()

        if row:
            return Player(row[1], row[0])
        else:
            None  
    
    @player.setter
    def player(self, value):
        if isinstance(value, Player):
            self.player_id = value

    # INSTANCE METHODS #
    def create(self):
        sql="""INSERT INTO games (name, hours_played, player_id)
        VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.name, self.hours_played, self.player_id])
        CONN.commit()

        self.id = CURSOR.lastrowid

    def delete(self):
        sql="DELETE FROM games WHERE id = ?"
        CURSOR.execute(sql, [self.id])
        CONN.commit()
        self.id=None
    
    def update(self):
        sql="""UPDATE games
        SET name = ?, hours_played = ?, player_id = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.hours_played, self.player_id, self.id])
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()