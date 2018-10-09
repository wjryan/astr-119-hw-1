#string
s = "I am a string."
print(type(s))  #will say string

#boolean
yes = True  #boolean true
print(type(yes))

no = False  #boolean false
print(type(no))

#list -- ordered and changeable

alpha_list = ["a", "b", "c"]    #list initializations
print(type(alpha_list))         #will say tuple
print(type(alpha_list[0]))      #will say string
alpha_list.append("d")          #will add "d" to the list end
print(alpha_list)               #will print list

#Tuple -- ordered and unchangeable

alpha_tuple = ("a", "b", "c")   #tuple intialization
print(type(alpha_tuple))        #will say Tuple

try:                            #attempt the following line
    alpha_tuple[2] = "d"        #won't work and will raise TypeError
except TypeError:               #when we get a type TypeError
    print("We can't add elements to a tuple!")  #print this message
print(alpha_tuple)              #will print tuple
