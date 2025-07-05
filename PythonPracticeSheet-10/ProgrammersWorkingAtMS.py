class Programmer:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def show_details(self):
        print(self.name, self.emp_id)

Divyansh = Programmer("Divyansh", 1007)
Gojo = Programmer("Gojo", 1008)
Aizen = Programmer("Aizen", 1009)
Ichigo = Programmer("Ichigo", 1010)

Divyansh.show_details()
Gojo.show_details()
Aizen.show_details()
Ichigo.show_details()