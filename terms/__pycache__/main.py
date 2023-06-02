from opening_text import open_text
from gameplay import gameplay
from close_page import death
playing = True
open_text()
while playing:
    gameplay()
    death()
exit()
