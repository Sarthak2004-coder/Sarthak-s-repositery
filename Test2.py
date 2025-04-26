n = 5
for i in range(1, n + 1):
    line = ""
    for j in range(1, n + 1):
        if j == n:
            line += str(i + 1)
        else:
            if j == 1:
                if i == 2:
                    line += '3'
                elif i == 4:
                    line += '5'
                else:
                    line += str(i)
            else:
                line += str(i)
    print(line)
