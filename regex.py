import re

"""
Exercise 1: Matching Email Addresses
- Create a regular expression that matches valid email addresses.
Remember that email addresses typically have the format `username@domain.extension`. 
Your regex should check for basic email format validation.
"""

regex = re.compile('(^\w+@[a-zA-z]+?\.[a-zA-Z]{2,3})$')
# The input should be in this format "username@domain.extension" space and not comma(,) to differenciate each email_address
# Example udoka@gmail.com glory@yahoo.com jo19.co.yahoo.co
address = input("Enter email address: ")
# we convert the input(address) to a list using split() function
email_address = address.split()
print(email_address) # expected output ['udoka@gmail.com', 'glory@yahoo.com', 'jo19.co.yahoo.co']
for email in email_address:
    if regex.match(email):
        print("Valid email")
    else:
        print("Invalid email")

"""
Exercise 2: Extracting Phone Numbers
- Given a text that contains multiple phone numbers, 
write a regular expression to extract all the phone numbers from the text. 
Phone numbers can have different formats, such as `+ 000 (123) 456-7890` or `+000-123-456-7890`.
"""
# Using regex to extract phone number from a text in a particular format
# The regular expression for extracting this number format ('+000-123-456-7890') is this (r'\+\d{3}-\d{3}-\d{3}-\d{4}')
numbers = "find the number + 000 (123) 456-7890"
pattern = r'\+ \d{1,4}\s?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'

phone_number = re.findall(pattern, numbers)
print(phone_number)


"""
Exercise 3: Validating URLs
- Create a regular expression to validate URLs. 
URLs can have different components, including the protocol 
(e.g., `http://` or `https://`), domain name, path, and query parameters. 
Your regex should be able to identify valid URLs.

"""

# Identifying a  valid URL
url_regex = re.compile("((http|https)://)(www.)?" +
            "[a-zA-Z0-9@:%._\\+~#?&//=]" +
            "{2,256}\\.[a-z]" +
            "{2,6}\\b([-a-zA-Z0-9@:%" +
            "._\\+~#?&//=]*)")

# You can enter as many   URLS as you want in your input, include a one wrong url from the format above
url = input("Enter a URL: ")
url_details = url.split()
for detail in url_details:
    if url_regex.fullmatch(detail):
        print("The URL is a valid URL")
    else:
        print("The URL you entered is not valid")

"""
Exercise 4: Extracting Dates
- Given a text that contains dates in different formats, 
write a regular expression to extract all the dates. 
Dates can be represented in various formats like `dd/mm/yyyy`, 
`mm/dd/yyyy`, or `yyyy-mm-dd`.
"""

# regex for extracting dates in this format "dd/mm/yyyy"  is "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
date_regex = re.compile("\d{4}[.-]\d{2}[.-]\d{2}$") # regex for extracting date in the format 'yyyy-mm-dd'
date_str = "Today is a beautiful day and the date is 2023-11-14"

date_output = date_regex.findall(date_str)
print(date_output)

"""
Exercise 5: Matching HTML Tags
- Write a regular expression to match HTML tags from a given HTML document.
 HTML tags are enclosed within angle brackets, such as `<p>`, `<div>`, 
 or `<a href="...">`.
"""

# Regular expression to match all the angle brackets <>
html_pattern = r"<[^>]*>"
file = ("<!DOCTYPE html>\n"
	"<html>\n"
	"    <head>\n"
	"        <title>\n"
	"            My Biography\n"
	"        </title>\n"
	"        <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n"
	"    </head>\n"
	"    <body>\n"
	"        <img src=\"img/glow.JPG\" alt=\"gloria's image\"/>\n"
	"        <h3>Hi, I'm Gloria Durugo</h3>\n"
	"        <p>I am a graduate of Computer Science,\n"
	"            currently improving on my backend programming skills.</p>\n"
	"        <div class=\"content\"><a href=\"hobbies.html\">Hobbies</a></div>\n"
	"        <div class=\"footer\"><a href=\"goal.html\">Goal</a></div>\n"
	"        <a href=\"home.html\">Return back</a>\n"
	"    </body>\n"
	"</html>")

main = re.findall(html_pattern, file)
print(main)

"""
Exercise 6:
- Create a regular expression to find all words that start with a capital letter in a sentence.
"""

# regex to find all words that starts with a capital letter
words_regex = r"[A-Z][A-Za-z]+"
text = "The sentence is Supposed to Ignore the Words at the beginning of the Sentence."

capital_words = re.findall(words_regex, text)
print(capital_words)

"""
Exercise 7:
- Write a regular expression to validate a password with the following criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (e.g., !@#$%^&*)

"""

# regex expression to validate a password with the above criteria
password_regex = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

password = input("Enter password here: ")

if re.match(password_regex, password):
    print("Valid Password")
else:
    print("invalid password")


"""
Exercise 8:
- Write a regular expression to extract all the hashtags (#) from a tweet.

"""
# regex to extract all the hashtags from a tweet
hash_regex = r"#(\w+)"

tweet = "I love #stackoverflow because #people are very #helpful!"

hash_words = re.findall(hash_regex, tweet)
print(hash_words)



"""
Exercise 9:
- Create a regular expression to match a date in the format "MM/DD/YYYY".

"""
# regex to match a date in the format "MM/DD/YYYY"
new_date = re.compile("\d{1,2}/\d{1,2}/\d{2,4}$")
main_date = '12/22/2014'
if new_date.fullmatch(main_date):
    print("The regex format matches the date format 'MM/DD/YYYY'")
else:
    print("Invalid date formate")