t = input("Enter the multiplication table you want: ")
t = int(t)
for i in range(11):
    if(i > 0):
        print(t,"X",i,"=",t*i)