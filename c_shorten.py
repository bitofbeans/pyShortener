# Import modules
import sys

# Try to import pyshorteners
try:
    import pyshorteners
except:
    print("Missing module - 'pyshorteners'")
    sys.exit()

# Print correct formatting function
def printHelp():
    print()
    print('Error: Incorrect Syntax')
    print(' -e       = Expand URL instead of shorten')
    print(' -nocopy  = Do not copy output to clipboard')
    print("Available services:", '"chilpit"','"clckru"','"dagd"','"gitio"','"isgd"','"osdb"','"owly"','"qpsru"','"tinyurl"')
    print('... {-e} {-nocopy} [Service] [URL Input]')

# Get args (except for script name)
arguments = sys.argv[1:]

# Default options 
copy = True
expand = False

# Change options according to commands
if "-e" in arguments:
    expand = True
    arguments.pop(arguments.index("-e"))
if "-nocopy" in arguments:
    copy = False
    arguments.pop(arguments.index("-nocopy"))
    
# Create instance of shortener
s = pyshorteners.Shortener()

# Try to load arguments from args
try:
    service = arguments[0]
    url = arguments[1]
except:
    printHelp()
    print("    Specific Error: ")
    print('--- Arguments Missing ---')
    sys.exit()
    
# Service options
services = ['chilpit','clckru','dagd','gitio','isgd','osdb','owly','qpsru','tinyurl']
# If service is wrong, exit
if not service in services:
    printHelp()
    print("    Specific Error: ")
    print("--- Service does not Exist ---")
    sys.exit()

# Define function map
 # Avoids using switch/if-then statements
 # and instead runs a function 
 # according to the input.
s_func = {'chilpit':s.chilpit,'clckru':s.clckru,'dagd':s.dagd,'gitio':s.gitio,'isgd':s.isgd,'osdb':s.osdb,'owly':s.owly,'qpsru':s.qpsru,'tinyurl':s.tinyurl}

# Do function
try:
    if expand == False:
        # Shorten url
        output = s_func[service].short(str(url)) 
    elif expand == True:
        # Expand url
        output = s_func[service].expand(str(url))
except:
    printHelp()
    print("    Specific Error: ")
    print('--- Invalid URL ---')
    sys.exit()

print()
print(output)

if copy == True:
    # If input is 'Y' or 'y' (upper or lowercase y)
    try:
        import clipboard
        clipboard.copy(output) # copy to clipboard
        print("Copied to clipboard!")
    except:
        print("Couldn't copy to clipboard.")
        print("Missing module - 'clipboard'")
else:
    
    print("Finished!")
print()
