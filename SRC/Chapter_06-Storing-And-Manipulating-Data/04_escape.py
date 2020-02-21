from flask import escape

print(escape("This is a request"))
print(escape("This is a <request>"))
