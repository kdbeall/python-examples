def foo():
    global me
    me = "locally defined"

foo()
print(me)
