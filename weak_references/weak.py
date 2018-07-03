import gc
import weakref


# Credit to https://github.com/k900
# this is just a hack to make lists weakref-able
class WeakList(list):

    pass

print('Test 1')
# create a list and a weakref to it
l = WeakList([1, 2, 3])
r = weakref.ref(l)
# refcount still = 1 because weakrefs don't count
print('Alive:', r())
# the name is deleted, refcount becomes 0, object is deallocated
del l
print('Dead:', r())

print('Test 2')
# create a list, then another reference to the same list, then a weakref
l = WeakList([1, 2, 3])
l2 = l
# refcount = 2 here
r = weakref.ref(l)
print('Alive:', r())
# remove one name, refcount = 1
del l
print('Still alive:', r())
# remove other name, refcount = 0, deallocated
del l2
print('Dead:', r())

print('Test 3')
# create a reference cycle
l1 = WeakList([1])
l2 = WeakList([2, l1])
l1.append(l2)
# refcount = 2 for both - 1 for name, 2 for inner reference (cycle)

# weakref both lists
r1 = weakref.ref(l1)
r2 = weakref.ref(l2)

# look ma, a cycle!
print('Both alive:', r1(), r2())

# delete both names
del l1
del l2
print('Still alive:', r1(), r2())

# force a gc sweep
gc.collect()

# and now they're gone
print('Dead:', r1(), r2())
