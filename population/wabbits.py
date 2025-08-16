def wabbits(user_input):
	s = user_input
	n_k = s.split(" ")

# n is the number of months
# k is the number of rabbit pairs in a litter
# a month will have the previous month's rabbits plus the new offspring
 
	rabbits = 1
	for i in range(1,int(n_k[0])+1):
		rabbits += i * int(n_k[1])
		
		print("Month:", i, end=" ")
		print("Rabbits:",rabbits)
	return rabbits

user_input = input("Enter n and k:\n")

print(wabbits(user_input))
