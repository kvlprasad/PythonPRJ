class Person():
    def __init__(self,name='Omkar',age=20,city='Pasadena',country='FRANCE'):
        self.name=name;
        self.age=age;
        self.city=city;
        self.country=country;
        self.skill=[];

    def personInfo(self):
        return  f'{self.name} is {self.age} old and he lives in the {self.city} {self.country}'
    def addSkill(self,skill):
        self.skill.append(skill);

class Student(Person):
            class Laptop:
                def boot(self):
                    return f" Its booing nOW, So pl take a seat !!!!";

print("This is my sentence of an Object \t"
      "Its hard what\"s going on this sentence \t"
      "whats upto you !!!!");


p1=Person("Ashley",22,"Sanjose","USA");
p2=Person("Geeta",32,"Pune","IN");

p1.addSkill('CSS');
p1.addSkill('HTML');
p1.addSkill('Java');
p1.addSkill('JavaScript');

print(Person.__dict__);
print(p2.skill);
print(p1.skill);

s1=Student("Omkar",21,"Orlando","FL");
s2=Student("Satheesh",20,"Houston","TX");

print(Student.Laptop.boot());
print(s2.personInfo());

