all:
	@cd org && emacsclient -s serverN --eval "(progn (find-file \"presentation.org\") (org-beamer-export-to-pdf) (kill-buffer))" > /dev/null
	cd org && scp presentation.pdf eab@microkairos:~/share/writehere

