import pyscreenshot as ImageGrab

def parse_input(body):
	return print_body(body)

def print_body(body):
	if (body):
		stripped = body[1:len(body)-3]
		question = "".join([s.content + " " for s in stripped[0:len(stripped)-3]])
		print(question)

		options = body[len(body)-6:len(body)-1]
		options = [o.content for o in options]	

		for choice, a in zip(['A','B','C'], options):
			print(choice + ". " + a)

		return question, options

def screenshot(id):
	im = ImageGrab.grab(bbox=(0,20,495,878))
	filename = "{}.png".format(id)
	im.save(filename)
	return filename

