# This is a simple bash script to run the game.

# Make commands run verbose.
set -x

# This is the path to the game's executable.
GAME_PATH="./game.py"

# Run the game.
python $GAME_PATH

# Make commands run silent again.
set +x

# Exit with success.
exit 0