import re

with open('input.txt') as f:
    lines = f.read().splitlines()

with open("output.txt", "w") as k:
    with open("outputMI.txt", 'w') as p:
        for line in lines:
            line = line.upper()
            num = re.findall(r'\d+', line)[-1]
            letter = line[:line.rfind(num)]
            print(letter)
            line = line[(line.rfind(num)+len(num))+1:]
            output = list(line[1:18])
            for i in range(len(output)):
                if output[i] == 'C':
                    output[i] = 'G'
                elif output[i] == 'G':
                    output[i] = 'C'
                elif output[i] == 'T':
                    output[i] = 'A'
                else:
                    output[i] = 'T'
            output.reverse()
            output = ''.join(output)
            output = line + output
            if output[0] == "G":
                D = output +  "A"
            else:
                D = output + "C"
            F1 = "AAGG" + D

            R1 = list(D)
            for i in range(len(R1)):
                if R1[i] == 'C':
                    R1[i] = 'G'
                elif R1[i] == 'G':
                    R1[i] = 'C'
                elif R1[i] == 'T':
                    R1[i] = 'A'
                else:
                    R1[i] = 'T'
            R1.reverse()
            R1 = ''.join(R1)
            R1 = "AAGA" + R1

            mi1 = "CTTGGGAATGGCAAGG" + D + "TCTTGCTATACCCAGA"
            mi1 = list(mi1)
            for i in range(len(mi1)):
                if mi1[i] == "T":
                    mi1[i] = "U"

            mi1 = ''.join(mi1)

            k.write(letter + str(num) + "-F"  + " " + F1)
            k.write('\n')
            k.write(letter + str(num) + "-R"  + " " + R1 + '\n')
            k.write('\n')
            p.write(letter + str(num) + "-MI"  + " " + mi1)
            p.write('\n')

f.close
k.close
p.close