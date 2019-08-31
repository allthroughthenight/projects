## [ghdecoy](https://github.com/tickelton/ghdecoy)
##### vanity repo to fake github commits for a full figured graph
1. [set-up](https://github.com/tickelton/ghdecoy/blob/master/README.md)
2. delete and remake [repo](https://github.com/allthroughthenight/decoy)
3. `$ python ghdecoy.py -s -u allthroughthenight -r decoy -l python 19900101-19910101`
	- `-s`: ssh authentication
	- `-u`: user name for someone other than unix user
	- `-r`: repo to push to
	- `-l`: languge of commits
	- `YYYYMMDD`: date range of commits to fill in
