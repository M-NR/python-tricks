# Extracted from accepted answer to question from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits?rq=1
  
def random_string(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
