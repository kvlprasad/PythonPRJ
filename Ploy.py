class Laptop:

    def code(self,ide):
        ide.execute();



class pyCharm:
    def execute(self):

        print(f"It Compiled");
        print(f"It Runs");

class Editor:
    def execute(self):
        print(f"It Spell check");
        print(f"It Formats");
        print(f"It Complies");
        print(f"It Runs");

ide=Editor();

lap=Laptop();
lap.code(ide);
