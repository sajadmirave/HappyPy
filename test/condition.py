# class Condition:
#     def __init__(self) -> None:
#         pass

#     def create(self,cond,code):
#         if cond == True:
#             return code
        
#     def echo(self,value):
#         print(value)

# condition = Condition()
# condition.create(
#     cond=False,
#     code=condition.echo("mew")
# )
class Condition:
    def __init__(self) -> None:
        ...

    def create(self, cond, code):
        if cond:
            return code

    def echo(self, value):
        print(value)

condition = Condition()
result = condition.create(cond=True, code="mew")
condition.echo(result)
