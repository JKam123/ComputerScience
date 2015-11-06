import hashlib # Import the hashlib
Found = False #Initialize Found value
L = []#Array
Num = 0#Start Number
while not Found: # While loop until Found == True
    Num = Num+1#Add up each time loop runs
    n = hashlib.sha256("Very important message! PeterMeier "+str(Num)).hexdigest()#Generate hash
    L = n#String into Array Not needed ...
    if L[0] == "0" and L[1] == "0" and L[2] == "0" and L[3] == "0" and L[4] == "0" and L[5] == "0" and L[6] == "0":#Check for 0
        Found = True#We found it!
        print "Number has to be " + str(Num)#Print number
        print n # Print hash
