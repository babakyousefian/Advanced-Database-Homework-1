
def print_All_4_Digits():
    l = list();
    p1=0;
    p2=0;
    print("\n\n your output is : ");
    for i in range(1000 , 9999+1 , 1):
        l = list(str(i));
        p1= int(int(l[len(str(i))-1]) + int(l[len(str(i))-2]));
        p2= int(int(l[0]) * int(l[1]));
        if p1 == p2:
            print(str(i) , sep=" " , end=" ");
        else:
            continue;

print_All_4_Digits();