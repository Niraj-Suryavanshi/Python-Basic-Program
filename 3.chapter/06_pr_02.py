letter='''Dear <|Name|>
you are selected
date: <|date|>'''

name=input("Enter your name:")
date=input("Enter a date:")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)