s = "Python is ironcically not a snake trying to kill you, so relax and enjoy that it actually tells you errors"

# this is your string - just type in the sentence or text you would like the most frequent letters of 
#-------------------------------------------------------------------------

# d is an empty list
# b is any one element
# when b in s, amount of value of element in d + 1
# -> d: List with frequency

d = {}

for b in s:

    if b not in d:
     d[b]= 1

    else:
        d[b] = d[b] + 1

# Key ' ', which is the element ' ' of a spacebar, 
# to be deleted and not shown in the print

del d[' ']

# d, through iteration d.items(), since its a dictionary, typecasting into list,
# so sorting can begin 

d_list = list(d.items())

# after "Bubble-Sort"-Idol: https://www.toptal.com/developers/sorting-algorithms ; 24-05-22)
# if successor of element is of a higher frequency (value), 
# succesor is moved higher 
#Loop-Idol after https://stackoverflow.com/questions/52551033/bubble-sorting-in-dictionary-in-python

for mx in range(len(d_list)-1, -1, -1):
    swapped = False
    for i in range(mx):
        if d_list[i][1] < d_list[i+1][1]:
            d_list[i], d_list[i+1] = d_list[i+1], d_list[i]
            swapped = True
    if not swapped:
        break

#Versuch 4 
#casts the list back to a dictionary for better display(only key etc.)
#and then adds keys 

dict_d = dict(d_list)
keys_str = ""
for key in dict_d.keys():
    keys_str = keys_str + key

print("The three most frequent symbols are {}, {} and {}.".format(keys_str[0], keys_str[1], keys_str[2]))
