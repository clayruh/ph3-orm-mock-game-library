# Phase 3 ORM Mock Challenge - Game Library

For this mock challenge, we'll be working with a domain for a gaming library.

We have two models: `Game` which shows the games that belong to a `Player`.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Only one of the tables, `players` has been created so far. Additionally the `Player` class already has its required functionality and you won't have to
build additional methods for it.

Build out all of the methods listed in the deliverables for `Game`. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects. There are no formal tests to run with this code so be
sure to test it in the `debug.py` often.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

- `Game classmethod create_table()`
  - Creates a `games` table with these columns: id (INTEGER), name (TEXT),
  hours_played (INTEGER), player_id (INTEGER)
- `Game __init__(name, hours_played, player_id, id=None)`
  - `Game` is initialized with a name (string) and hours_played (integer)
  - When initialized a Game should have an id of None
  - Assume that Games will always be initialized with the proper data types
- `Game __repr__()`
  - Returns the Game instance in the format below:
  - `Game(id={id} name={name}, hours_played={hours_played}, player_id={player_id})`
- `Game property hours_played()`
  - Returns the `Game`'s hours_played
  - The hours_played must be an integer greater than 0

### SQL Methods

- `Game create()`
  - Creates a Game in the database with the instance's attributes
- `Game update()`
  - Updates a Game in the database based on the instance's attributes
- `Game save()`
  - Will either create or update the Game in the database depending on whether
  the Game has an id
- `Game delete()`
  - Deletes the Game from the database
  - No return value is necessary for this method
- `Game classmethod query_all()`
  - Returns a list of Game instances based on rows in the database
  - The return value ought to be a list of Game instances

### Association Propertiesc2

- `Game property player()`
  - Returns the Player that the Game is associated with as an instance
  - If the Game is not associated with a Player returns `None`
  - When setting the player, if the argument is a `Player` instance it
  associates the Game with the player
  - The database is already seeded with a pair of players for testing purposes
    - Player(id=1, name="Justin Muzzi")
    - Player(id=2, name="Brandon Collins")

### BONUS Methods

- `Game classmethod all_time_favorite()`
  - Returns the Game with the most hours_played as an instance
- `Player favorite_game()`
  - Returns the Game that a player has played the most (highest hours played)
  for that player
- `Game classmethod average_playtime()`
  - Returns the average hours_played across all games