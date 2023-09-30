
class userclass:
    def __init__(self, name, age, nationality, adult):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.adult = adult
        

        data_processing = open("user_data.txt", "w")
        data_processing.write(self.name)
        data_processing.write("\n")
        data_processing.write(str(self.age))
        data_processing.write("\n")
        data_processing.write(self.nationality)
        if self.adult <=18:
             data_processing.write("\nNon Adult")
        if self.adult >=18:
             data_processing.write("\nAdult")
        data_processing.write("\n")
        data_processing.close()

    
        
