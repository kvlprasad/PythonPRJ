import pyspark
from pyspark.sql import SparkSession
import os

os.environ["JAVA_HOME"] = "/var/run/host/usr/lib/jvm/java-8-openjdk-amd64";

spark= SparkSession.builder.master("local[*]").appName("WIndowing").getOrCreate();

simpledata=(("James", "Sales", 3000),
           ("Michael", "Sales", 4600),
           ("Robert", "Sales", 4100),
           ("Maria", "Finance", 3000),
           ("James", "Sales", 3000),
           ("Scott", "Finance", 3300),
           ("Jen", "Finance", 3900),
           ("Jeff", "Marketing", 3000),
           ("Kumar", "Marketing", 2000),
           ("Saif", "Sales", 4100)
           );
columns=("ename","dept","salary");

df=spark.createDataFrame(simpledata,schema=columns);

df.printSchema();
df.show(10,False);



