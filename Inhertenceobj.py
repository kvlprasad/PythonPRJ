
class A:
    def __init__(self):
        print(f" I am in A");
    def feature1(self):
        print(f"Feature 1 working");
    def feature2(self):
        print(f"Feature 2 working");

class B:
    def __init__(self):

        print(f" I am in B");


    def feature3(self):
        print (f"Feature 3 working");
    def feature4(self):
        print(f"Feature 4 working");

class C(A,B):

    def __init__(self):
        super().__init__();
        print(f" I am in C");

    def feature5(self):
        print(f"Feature 5 working");

if __name__=="__main__":

    objc= C();
    #its calling constructor in Class A is called Method Resolution Order..
    objc.feature1();
    objc.feature4();
    objc.feature5();


    #print(objc.__dict__);