import sys

prev_show          = " "                #initialize previous show to blank string

is_abc             = 0 #indicate shows on abc
viewer_total         = 0 #sum viewers

line_cnt           = 0  #count input lines
curr_show          = " "
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

   
    if curr_show != prev_show:

        if line_cnt>1 and is_abc==1:
	    print('{0} {1}'.format(prev_show,viewer_total))
            
	is_abc = 0
        viewer_total = 0
        prev_show = curr_show  #set up previous show for the next set of input lines

	
    if value_in == 'ABC': 
        
        is_abc = 1

    else:

        viewer_total += int(value_in)
print('{0} {1}'.format(curr_show,viewer_total))
