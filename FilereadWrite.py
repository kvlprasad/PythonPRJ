
file=open("/home/kapur/Downloads/kvlprasad/PaidRent.pdf","rb");
file1=open("resources/PaidRent.pdf","wb");

for data in file:
    file1.write(data);
