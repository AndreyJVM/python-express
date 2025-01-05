"A string in double quotes can contain 'single quote' characters."

'A string in single quotes can contain "double quote" characters.'

'''\tA string which starts with a tab; ends with a newline character.\n'''

"""This is a triple double quoted string, the only kind that can
contain real newlines."""


x = "live and    let \t    \tlive"

x.split() # ['live', 'and', 'let', 'live']

x.replace("let \t   \tlive", "enjoy life") # 'live and enjoy life'



import re

regexpr = re.compile(r"[\t ]+")
regexpr.sub(" ", x) # 'live and let live'