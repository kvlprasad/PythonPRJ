import sys;
import os;
import logging;
import statistics;


from random import random,randint;

# Create and configure logger
logging.basicConfig(filename="resources/logger.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger= logging.getLogger();
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.WARN);

logger.warning("Its started Logging !!!!");


language="Python3";
print(language[0:3]);
print(language[::-1])
challenge="Its3456awonderfullLand";
print(challenge.isalnum());

#random, randonint
for i in range(randint(5,100)):
    print(i);
#sum of tuples
total=0;
def sumTuples(*nums):
    total=0;
    for num in nums:
        total += num;
    return total;

print("Sum of tuple is : "+ str(sumTuples(2,10,12)) );

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'];
upperNames=map(lambda name: name.upper(),names);

print(list(upperNames));


counter =0;

while counter < 5:
    print("Hello !!!!");
    counter +=1;

def getEnvs():
    osenv=os.getcwd()
    return str(osenv)+ " Wecome {} , I live {} ".format(sys.argv[1],sys.argv[2]);

if __name__=="__main__":


    print(getEnvs());
    print("Hello  ...!!!!");
    print(sys.path);
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
logger.warning("Logging Ended !!!!");

data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26];
print(data);


