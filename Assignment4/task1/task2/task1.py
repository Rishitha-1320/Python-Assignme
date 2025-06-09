try:
    file1=open("my_file.txt",'r')
    print("Reading file content:")
    num=1
    for line in file1:
        print("Line",num,":",line.strip())
        num+=1
    file1.close()
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
