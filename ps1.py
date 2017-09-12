###### this is the first .py file ###########
#!/usr/bin/python

message = []                                                        #list for message bit
p_message = []                                                      # list for message bit along with the parity bit 
num = input('enter total no of bits in a message \n')                   # Taking the no of bits in message
                                                                         # taking input for message bits
for count in range (0, num , +1):                                         
	value = input("enter the one binary value of mesaage and enter")	
	message.append(value);
	                                                                  # finish acknowledgment for finishing message
print ("finish")  
bit = message[0];                                            #new variable bit for parity calculation purpose
p_message.append(bit);                                        # taking first element into the list of message bit along with parity
print '1st bit is', bit                                       
                                                              #logic for the parity calculation
for count in range (1, num , +1):                              
	par = bit ^ message[count]
	bit = par
	element = message[count]
	p_message.append(element)

parity =par ^(not par)
 
                                                        #printing the only parity bit
print 'parity bit is:', parity
                                                  
p_message.append(parity)                          # Adding the parity bit to the list
message.append(parity) 
                                                       #printing the message bits along with parity
print ("message with parity bit is as follows \n")
for count in range (0, num+1 , +1):
	print p_message[count],

new = num+1                                                          # logic for the Bit Orientation                   	
for count in range(0, new, +1):
	if (count <= (num-2) ):
		if (message[count] == 0 and message[count+1] == 1 and message[count+2] == 0):
			p_message.insert(count+3, '0');

     

                                                      #logic for checking the last two bits
print ("message with bit orientation is as follows \n")
if ((message[new-2] == 0) and (message[new-1] == 1)):
	p_message.append('0')                                  #appending the  0 based on the condition


                                                                 #appending the flag for end of the frame
p_message.append('0')
p_message.append('1')
p_message.append('0')
p_message.append('1')

length = len(p_message)                                       #Calculating the new frame size

print ("finale")                                              #Printing the final frame of mesage along with the bit orientation
for count in range (0, length , +1):
	print p_message[count],

####### write your code here ##########
