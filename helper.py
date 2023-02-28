name_of_unit="hour";

def validate_exec(input_Days):

    try:
        if(int(input_Days) >0):
            input_Days = int(input_Days);
            print(days_to_units(input_Days));
        else:
            print("Invalid Number");

    except:
        print("Its not a Digit");


def days_to_units(numDays):
    if (numDays > 20):
        print(type(numDays));
        espression= eval("numDays * calicutaion_to_units");
        return(f" {numDays} days are {espression} {name_of_unit}");
        print("All Good !");
    else:
        return("Not a valid value");