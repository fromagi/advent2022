sum = 0
totals = []

with open('input.txt', 'r') as f:
	#lines = f.readlines()
    #lines = f.read().splitlines()
    for line in f:
        if line == '\n':
            totals.append(sum)
            sum = 0
        else:
            sum += int(line)
            
totals.sort(reverse = True)   

answer = totals[0] + totals[1] + totals[2]

print(f"Highest: { totals[0] }")
print(f"Highest Three: { answer }")