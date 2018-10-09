#define a function
def flow_control(k):

	#deine a string based on the value k
	if(k==0):
		s = "Variable k = %d equals 0." % k
	elif(k==1):
		s = "Variable k = %d equals 1." % k
	else:
		s = "Variable k = %d does not equal 0 or 1." % k
	print(s) # print the variable
	
def main(): #define a main function
	i = 0 #declare an integer
	#try flow_control for 0, 1, 2
	flow_control(i)
	i = 1
	flow_control(i)
	i = 2
	flow_control(i)
	
if __name__ == "__main__":
	main()


	
	
		