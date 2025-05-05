import icontract

@icontract.require(lambda x: x > 3)
def f(x):
    pass

f(4) 
@icontract.require(lambda x,y: (x > 4) and (y>3))
@icontract.ensure(lambda result: result > 10)
def add_above_ten(x,y):
    print(x+y)
    return x+y

result = add_above_ten(5,4)
print(result)
