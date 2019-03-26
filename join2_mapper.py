import sys

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    
    if value_in == "ABC" or value_in.isdigit():           #if this entry equal 'ABC' or a digit
        print( '%s\t%s' % (key_in, value_in) )  #printing a string, tab, and string
