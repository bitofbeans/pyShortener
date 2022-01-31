# Import modules
import pyshorteners
import pprint as pp

# Create instance of shortener
s = pyshorteners.Shortener()

# User input for which action
print("Would you like to shorten or expand a URL?")
arg = input("'short', 'expand': ")

# Define services and print them to user
services = ['chilpit','clckru','dagd','gitio','isgd','osdb','owly','qpsru','tinyurl']
pp.pprint(services)

# Get user input for which service
service = input("Choose a service to use...: ")

# If not a valid service, exit
if not service in services:
    raise SystemExit("Not a valid service")

# Get input URL
url = input("Enter URL to modify: ")

# Define function map
 # Avoids using switch/if then statements
 # and instead runs a function 
 # according to the input.
s_func = {'chilpit':s.chilpit,'clckru':s.clckru,'dagd':s.dagd,'gitio':s.gitio,'isgd':s.isgd,'osdb':s.osdb,'owly':s.owly,'qpsru':s.qpsru,'tinyurl':s.tinyurl}

# Do function
if arg == 'short':
    # Shorten url
     # Get the corresponding function
     # according to the input
    output = s_func[service].short(str(url)) 
elif arg == 'expand':
    # Expand url
    output = s_func[service].expand(str(url))

# Show result to user
print() # new line
print(f"New URL >> {output}") 

# Ask to copy to clipboard
if input("Copy to clipboard? [Y]: ") in ["y", "Y"]:
    # If input is 'Y' or 'y' (upper or lowercase y)
    import clipboard
    clipboard.copy(output) # copy to clipboard
print("Success!")