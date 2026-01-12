Install_Path ?= ~/foo
Data_Path ?= ~/.mood

install:
	cp -r main.py $(Install_Path)/mood
	mkdir -p $(Data_Path)

uninstall:
	rm -f $(Install_Path)/mood
	rm -rf $(Data_Path)

update:
	cp -r main.py $(Install_Path)/mood