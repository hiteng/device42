





def helloSolarSystem(original_function):
    def new_function():
        original_function()
        print("Hello, solar system!")
    return new_function

def helloGalaxy(original_function):
    def new_function():
        original_function()
        print("Hello, galaxy!")
    return new_function



@helloGalaxy
@helloSolarSystem
def hello():
    print ("Hello, world!")


if __name__ == '__main__':


    hello()