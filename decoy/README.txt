vanity repo to fake github commits for a full figured graph https://github.com/tickelton/ghdecoy

tl;dr
	1) do set up for tickelton/ghdecoy
	2) delete and remake 'decoy repo'
	3) run the command below
	$ python ghdecoy.py -s -u allthroughthenight -r decoy -l python -m 0 fill
		-s use ssh i.e. if you use pgp keys
		-u user name for someone other than unix user
		-r repo to push to
		-m fill in X amount of empty days with commits
