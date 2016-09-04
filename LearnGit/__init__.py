class Driver(object):
    def __init__(self, name="", track="", finish=""):
        if not name:
            name = input("What is the driver's name? ")
        if not track:
            track = input("What is the driver's track? ")
        if not finish:
            finish = self.get_finish()
        self.name = name
        self.track = track
        self.finish = finish
    def get_finish(self):
        while True:
            finish = input("What is the driver's finish ? [K, 1-5]  ")
            if finish.lower() not in ['k', '1', '2', '3', '4', '5']:
                print("I'm sorry, but {} isn't valid.".format(finish))
            else:
                return finish

    def print_driver(self):
        print("Name: {}".format(self.name))
        print("Track {}".format(self.track))
        print("Finish {}".format(self.finish))

def print_roster(drivers):
    print("Drivers in the system:")
    for driver in drivers:
        print("*"*15)
        driver.print_driver()

def main():
    driver1 = Driver(name="Car 18", finish="3", track="Marshall")
    driver2 = Driver(name="Car 19", finish="2", track="Minnieville")
    driver3 = Driver(name="Car 20", finish="K", track="Woodbridge")
    drivers = [driver1, driver2, driver3]
    print_roster(drivers)

if __name__ == '__main__':
    main()

