from math import sqrt

print("x^2 + px + q = 0")
p=int(input("Skriv vad p i pq formeln ska vara: "))
q=int(input("Skriv vad q i pq formeln ska vara: "))

q1=(p/2)**2 -q
p1=p/-2

if q1<0:
    print("Ekvationen saknar reell losning")
elif q1==0:
    print("x ar",p1)
elif q1>0:
    x1=p1+sqrt(q1)
    x2=p1-sqrt(q1)
    print("x kan antingen vara", x1, "eller", x2)