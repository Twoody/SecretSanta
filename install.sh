
# TODO: Actually test this and see if it works
# TODO: Check PWD...

# If file DNE, setup for user
if [ -f .env ] ; then
	echo "Creating .env file"
	cp .env.example .env
else
	echo "Skipping .env rewrite"

# If file DNE, setup for user
if [ -f .players ] ; then
	echo "Creating players.py file"
	cp players-example.py players.py
else
	echo "Skipping players.py rewrite"



