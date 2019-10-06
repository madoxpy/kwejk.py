

from requests import *
import re
from pygame import *

page = get("http://www.kwejk.pl")


endprogram = False
while not endprogram:
	text = str(page.content)
	#print(text)
	urls = re.findall("https://i1.kwejk.pl/k/obrazki/[a-zA-Z0-9/]+.jpg",text)
	#print(urls)
	urls = list(set(urls))
	for url in urls:
		pagepic = get(url)
		#print(pagepic.content)
		with open('current.jpg', 'wb') as f:
			f.write(pagepic.content)
		f.close()

		pic = image.load("current.jpg")

		WIDTH = pic.get_width()
		HEIGHT = pic.get_height()
		init()
		clock = time.Clock()
		screen = display.set_mode((WIDTH,HEIGHT))
		screen.blit(pic,(0,0))
		#screen.destroy()

		end = False
		while not end:
			for z in event.get():
				if z.type == QUIT:
					endprogram = True
			if not endprogram:
				display.flip()
				clock.tick(25)
				keys=key.get_pressed()
				if keys[K_SPACE]:
					end = True
					quit()

			else:
				end = True
		if endprogram:
			break
	a = re.findall('<a href="https://kwejk.pl/strona/'+'[0-9]+'+'" class="btn btn-next',text)
	#rint(a)
	nexturl = re.findall("https://kwejk.pl/strona/[0-9]+",a[0])
	#print(nexturl)
	page = get(nexturl[0])