import re

pattern= r"[A-Z]ython"
text='''This endpoint provides live top and Dython breaking headlines for a  Aython country, specific category in a country, single source, or multiple sources. You can also search with keywords. Articles are sorted by the earliest date published first.
This endpoint is great for retrieving Python headlines for use with news tickers or similar.'''
matches= re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0] : match.span()[1] ])
