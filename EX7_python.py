import time;
from math import pow , sqrt;

def Max1(l:(list)=[]) -> int:
    if not isinstance(l,list):
        raise TypeError("\n\n an Error occur");
    else:
        maximum = 0;
        for i in l:
            if i>maximum:
                maximum = i;
            else:
                continue;
        return maximum;

def Min1(l:(list)=[]) -> int:
    if not isinstance(l,list):
        raise Exception("\n\n an ERROR occur...!!!");
    else:
        minimum=int(l[0]);
        for i in range(0, len(l) , 1):
            if int(l[i]) < minimum:
                minimum = int(l[i]);
            else:
                continue;
        return minimum;

def Ave1(l:(list)=[]):
    if not isinstance(l,list):
        raise TypeError("\n\n an ERROR occur...!!!");
    else:
        average = 0.00;
        sum = 0.00;
        length = len(l);
        for i in range(0, len(l),1):
            sum += int(l[i]);
        average = sum/length;
        print("\n\n Average is: ",average);

def STD1(l:(list)=[]):
    if isinstance(l,list)==False:
        raise Exception("\n\n An ERROR occur...!!!");
    else:
        mu=0;
        avg = 0.00;
        s = 0.00;
        size = len(l);
        for i in range(0, len(l), 1):
            s += int(l[i]);
        avg = s / size;

        mu = avg;
        sum_of_variance = 0;
        N = len(l);
        for i in range(0 , len(l) , 1):
            sum_of_variance += (pow((float(int(l[i]))-mu) , 2));

        variance = sum_of_variance/N;
        standard_deviation = sqrt(variance);
        print("\n\n Standard Deviation is: ",standard_deviation);

n = int(input("\n\n Enter the n: "));
l = list();
for i in range(0,n,1):
    l.append(int(input("\n\n Enter number"+str(i+1)+": ")));


max_number = Max1(l);

time.sleep(1);

print("\n\n Maximum is: ",max_number);

min_number = Min1(l);

time.sleep(1);

print("\n\n Minimum ia: ",min_number);

time.sleep(1);

Ave1(l);

time.sleep(1);

STD1(l);
