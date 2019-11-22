session = dict()

# The below code gives KeyError, as the dict
# does not have the key `logged_in`
# if session["logged_in"]:
#     print("Found It")

# Checking the existence using the in key word does not
# cause keyerror
if "logged_in" in session:
    print("Found It")

session["logged_in"] = True

# Checking using in still works
if "logged_in" in session:
    print("Found It")

# checking using if also works.
if session["logged_in"]:
    print("Found It")
