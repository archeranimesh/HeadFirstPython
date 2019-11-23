session = dict()

# The below code gives KeyError, as the dict
# does not have the key `logged_in`
if session["logged_in"]:
    print("Found It")
