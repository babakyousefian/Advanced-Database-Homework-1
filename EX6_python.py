from math import sqrt;

def calculateN(n:(int)=0):
    if not isinstance(n,int):
        raise TypeError("\n\n invalid inputs...!!!");
    else:
        l = [];
        maximum = 0;
        average = 0.00;
        sum = 0.00;

        for i in range(0, n, 1):
            l.append(int(input("\nEnter number " + str(i + 1) + ": ")));

        minimum = l[0];

        for i in l:
            if i > maximum:
                maximum = i;
            elif i < minimum:
                minimum = i;

        for i in l:
            sum += i;
        average = sum / len(l);

        N = len(l);
        mu = float(average);
        variance_sum = 0;

        # Variance = (Σ(xi - μ)^2) / N
        for i in l:
            variance_sum += ((i - mu) ** 2);

        variance = variance_sum / N;
        standard_deviation = sqrt(variance);

        print("\n\n Maximum is: ", maximum);
        print("\n\n Minimum is: ", minimum);
        print("\n\n Average is: ", average);
        print("\n\n Standard Deviation is: ", standard_deviation);


n = int(input("\n\n Enter the n: "));
calculateN(n);
