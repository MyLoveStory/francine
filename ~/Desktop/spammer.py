import random
import string
import sys
import mechanize

def fill(control):

	""" Fills up radio, checkbox and select control with a random option """
	print control
	print dir(control)
	total = len(control.get_items())
	value_to_set = str(control.get_items()[random.randint(1,total - 1)])
	control.value = [value_to_set]

def random_text(control, length):

	""" Fills up a text control with a random string of length "length" """

	control.value = ''.join(random.choice(string.ascii_uppercase + string.digits)
					for _ in range(length))

def new_browser():

	""" Returns a new mechanize browser instance """

	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.set_handle_refresh(False)

	return browser

def fill_form(form):

	""" Fills up the form with random bs """

	for control in form.controls:
		fill(control)

def spam_form(url, times = 1):

	""" Spams a google form at url "times" number of times """

	browser = new_browser()
	total = times
	while times:

		""" Open form """
		browser.open(url)

		""" The form has no name by default, but luckily for
			us only one form on the page so simply select the
			first one.
		"""
		browser.form = list(browser.forms())[0]

		""" Mess it up and submit"""
		fill_form(browser.form)
		browser.submit()

		times -= 1

		print "%d. Filled form" % (total - times)


if __name__ == "__main__":

	if len(sys.argv) < 3:
		print "run script as\n'python %s 'url' (in quotes) number_of_times_you_want_to_spam'\n" %(__file__)
		exit()

	url = sys.argv[1]
	times = int(sys.argv[2])
	spam_form(url, times)
