from helper import validate_exec
import os,sys
from datetime import datetime;
no_of_days=20;
calicutaion_to_units=24;


for i in range(10):
    print (i);

for i in range(1,10):
    if(i%2 != 0):
        pass;
    else:
        print("Even Number ",i);


file = open("/home/kapur/Downloads/Kubernetes/Test-py.txt");
wordCnt=0;

for line in file.readlines():
    tokens=line.split(" ");
    wordCnt +=len(tokens);
    #print(len(tokens));
file.close();


def caliculate_area(base,height):
    return 1/2*base*height;

if __name__== "__main__":
    print("Area of the Triangle is :",caliculate_area(2,5));

print("Total cunts are : "+ str(wordCnt));


with open("/home/kapur/Downloads/Kubernetes/readTest.txt") as f:
    print(f.read(),end='');



file12 = open("/home/kapur/Downloads/Kubernetes/Test-py.txt");
wordCnt=0;
print(file12.readlines()[2]);
file12.close();
"""
for line in file:
    print(line);
file.close();

file = open("/home/kapur/Downloads/Kubernetes/Test-py.txt","a");
file.write("\n My Test File 576...!!!!");
file.close()

"""


input_Days="";

print(os.name);
"""
while (input_Days !="exit"):
    input_Days=input("Pl Enter no of Days :");
    for day in set(input_Days.split(",")):
        print(day);
        validate_exec(day);
"""

print(datetime.now())

dtm =input("Pl ente Date weather is it valid : ");
dtm=datetime.strptime(dtm,"%m-%d-%Y")
print(dtm);
currendtm = datetime.today();

print(f"Dead Line is in :  {(dtm-currendtm).days} Days");










