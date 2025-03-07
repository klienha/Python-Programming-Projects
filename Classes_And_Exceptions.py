class Criminal:
    def __init__(self, name, num_fraud, num_assault, num_murder, victims):
        if num_fraud + num_assault + num_murder != len(victims):
            raise InfoError("No. of crimes and no. of victims must match!")
		
        self.name = name
        self.num_fraud = num_fraud
        self.num_assault = num_assault
        self.num_murder = num_murder
        self.victims = victims
	
    def add_crimes(self, crimes):
        if type(crimes) != dict:
            raise InfoError("Crime information must be in a dictionary.")

        for crime in crimes:
            for victim in crimes[crime]:
                if victim not in self.victims:
                    if crime == "murder":
                        self.num_murder += 1
				
                    elif crime == "fraud":
                        self.num_fraud += 1

                    else:
                        self.num_assault += 1

                    self.victims.append(victim)

    def exonerate(self, crimes):
        if type(crimes) != dict:
            raise InfoError("Crime information must be in a dictionary.")
	    
        for crime in crimes:
            for victim in crimes[crime]:
                if victim in self.victims:
                    if crime == "murder":
                        self.num_murder -= 1

                    elif crime == "fraud":
                        self.num_fraud -= 1
				
                    else:
                        self.num_assault -= 1

                    self.victims.remove(victim)
	
    def __str__(self):
        return f"Criminal {self.name}: fraud {self.num_fraud}, assault {self.num_assault}, murder {self.num_murder}."
		

class InfoError(Exception):
    def __init__(self, msg):
        self.msg = msg
	
    def __str__(self):
        return self.msg