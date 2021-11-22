def encode(sequence):
    count = 1
    result = []
    for x,item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1
    result.append((sequence[len(sequence) - 1], count))
    return result
    


def decode(sequence):
    result = []
    for item in sequence:
        result.append(item[0] * item[1])
    return "".join(result)

def formatOutput(sequence):
    result = []
    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])
    return "".join(result)

def main():
  
    h = int(input("Press 1 and Enter to start decompressing your files.\n"))

    if h == 1:
        file = input("Enter the filename:")
        with open(file, 'r') as f:
            string = f.read()
            
    else:
        print("You entered invalid input")
    encoded = encode(string) 
    decoded = decode(encoded)
    
    OutputFile2=open('Decompressed.csv','w')
    OutputFile2.write(decoded)
    print("File succesfully decompressed.")
if __name__ == "__main__":
    main()

