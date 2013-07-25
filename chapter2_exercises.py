# Exercises for chapter 2:

# Name:Patrick Byrnes (PMByrnes)

#Exercise 2.1: Starting with a 0 tells Python to treat the number as an octal
#Exercise 2.2: 
5
x = 5
x + 1
# "print x + 1" returns a value of 6 in the script mode, assuming that 5 was already assigned to variable x
# if we ask Python "print 'x + 5'" it will return "x + 5"
#Exercise 2.3:
	#1. 8       integer
	#2. 8.5     float
	#3. 4.0     float
	#4. 11      integer
	#5. '.....' string 

#Exercise 2.4:
# 1
r = 5
pi = 3.14159
radius = (4/3) * pi * r**3
print radius

# 2
book = 24.95
discount = .40
shipping = 3
additional = .75
wholesale = (book * (1-discount)) * (shipping + additional*59)
print wholesale

#3
s_hour = 6     #starting hour 
s_minute = 52  #starting minute 
e_minute = 8   #easy pace in minutes
e_second = 15  #easy pace in seconds
t_minute = 7   #tempo pace in minutes
t_second = 12  #tempo pace in seconds
s_seconds = (s_hour*60*60)+(s_minute*60)   #starting time in seconds
total_run_min = (e_minute*2)+(t_minute*3)  #total run in minutes
total_run_sec = (e_second*2)+(t_second*3)  #total additional seconds in run
run_time_in_sec = total_run_min*60 + total_run_sec  #total run seconds
bk_time_sec = run_time_in_sec + s_seconds   #time in seconds at end of run/start of breakfast
breakfast_hour = (bk_time_sec/60)/60    #hour of day for breakfast
breakfast_min = int((bk_time_sec/60.0)-(breakfast_hour*60)) #min of day for breakfast
breakfast_sec = bk_time_sec - breakfast_min*60 - breakfast_hour*60*60
print breakfast_hour,":",breakfast_min,":",breakfast_sec