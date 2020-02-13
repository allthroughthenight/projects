how to run
	python 3 __main__.py
tldr
	make an applet launcher for all these .py files
	or consolidate into one project, following proper python project structur
	import as needed with main menu and such
	gui?
papa programmer
	https://www.youtube.com/watch?v=y1Io0XgD1Ow
	https://www.youtube.com/watch?v=toe8wcSiuak
pyinstaller
	on linux via wine for windows
		brain dump of how to cross-compile python on linux for windows via pyinstaller and wine
		pyinstaller and wine
			https://www.sparkandshine.net/build-a-windows-executable-from-python-scripts-on-linux/
			https://www.andreafortuna.org/2017/12/27/how-to-cross-compile-a-python-script-into-a-windows-executable-on-linux/
		wine and ubuntu server
			https://linustechtips.com/main/topic/731012-how-can-i-install-wine-server-on-ubuntu-server-14/
			https://wiki.winehq.org/Ubuntu
			https://ubuntuforums.org/showthread.php?t=2367829
		tl;dr
			$ mkdir temp-dir; cd temp-dir
			$ sudo apt install -y wine-stable winetricks
			$ wget https://www.python.org/ftp/python/3.4.3/python-3.4.3.amd64.msi
			$ wine msiexec /i python-3.4.3.amd64.msi /qb
			$ cd ~/.wine/drive_c/Python34
			$ wine python.exe Scripts/pip3.exe install pyinstaller
			$ echo 'print("Hello World!")
			input() # to prevent CMD window from closing' > hello.py
			$ wine ~/.wine/drive_c/Python34/Scripts/pyinstaller.exe --onefile --distpath ./ hello.py
	previous process is janky since it is dependant on an old wine (v3) and old python (3.4)
		reasoning for the old wine is because the latest (5) isn't mainline for ubuntu or debian
		reasoning for the old python is because of probelms with running an exe installer, so the latest version that supports an msi install is python 34
		potential work around is 'extracting' the msi from the exe, or conver the exe to msi
		overall don't consider it viable in the long term
	see below for a pros vs cons list
		linux via wine
			pros
				foss and righteous
				plenty of wine and pyinstall info available for linux
			cons
				jankey set up and work arounds
				fragile for long term maintainability
				have to resolve dependancies for out of date or deprecated packages
		windows vm
			pros
				direcly on machine
				able to use what's available without modifying
				easier to keep up to date and maintain long term
			cons
				not foss or righteous
				provisioning and consistency of build env is unknown
	though not righteous, a windows vm is better for ease of maintainability (and less jank) in the long run
	quick search returned the following, so win10 vms might be easier that assumed
		https://dev.to/jeikabu/reusable-windows-vms-with-vagrant-2h5c
todo
	 car fuel cost calculator: mpg, mpg calc, gas tank size, week/month/year costs
