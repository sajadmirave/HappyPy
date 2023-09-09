class State:
    def __init__(self,value) -> None:
        self.value = value

    def update(self,newValue):
        self.value = newValue
    
    def echo(self):
        print(self.value)

mystate = State("sajad")
mystate.update("mmd")
mystate.echo()