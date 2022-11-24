""" adapter.py """

from math import sqrt

# Also known as wrapper

### Intent
#   ------
# Adapter is a structural design pattern
# that allows objects with incompatible
# interfaces to collaborate.
#
### Problem
#   -------
# Imagine that you’re creating a stock
# market monitoring app. The app downloads
# the stock data from multiple sources in
# XML format and then displays nice-looking
# charts and diagrams for the user.
#
# At some point, you decide to improve the
# app by integrating a smart 3rd-party
# analytics library. But there’s a catch:
# the analytics library only works with data
# in JSON format.
#
# You could change the library to work with XML.
# However, this might break some existing code
# that relies on the library. And worse, you
# might not have access to the library’s source
# code in the first place, making this approach
# impossible.
#
### Solution
#   --------
# You can create an adapter. This is a special
# object that converts the interface of one
# object so that another object can understand
# it.
#
# An adapter wraps one of the objects to hide
# the complexity of conversion happening behind
# the scenes. The wrapped object isn’t even aware
# of the adapter. For example, you can wrap an
# object that operates in meters and kilometers
# with an adapter that converts all of the data
# to imperial units such as feet and miles.
#
# Adapters can not only convert data into various
# formats but can also help objects with different
# interfaces collaborate. Here’s how it works:
# 1. The adapter gets an interface, compatible
# with one of the existing objects.
# 2. Using this interface, the existing object can
# safely call the adapter’s methods.
# 3. Upon receiving a call, the adapter passes the
# request to the second object, but in a format and
# order that the second object expects.
#
# Sometimes it’s even possible to create a two-way
# adapter that can convert the calls in both directions.
#
# Let’s get back to our stock market app. To solve
# the dilemma of incompatible formats, you can create
# XML-to-JSON adapters for every class of the analytics
# library that your code works with directly. Then you
# adjust your code to communicate with the library only
# via these adapters. When an adapter receives a call,
# it translates the incoming XML data into a JSON
# structure and passes the call to the appropriate
# methods of a wrapped analytics object.
#
### Application
#   -----------
# 1. Use the Adapter class when you want to use some
# existing class, but its interface isn’t compatible
# with the rest of your code.
#
# The Adapter pattern lets you create a middle-layer
# class that serves as a translator between your code
# and a legacy class, a 3rd-party class or any other
# class with a weird interface.
#
# 2. Use the pattern when you want to reuse several
# existing subclasses that lack some common functionality
# that can’t be added to the superclass.
#
# You could extend each subclass and put the missing
# functionality into new child classes. However, you’ll
# need to duplicate the code across all of these new
# classes, which smells really bad.
#
# The much more elegant solution would be to put the
# missing functionality into an adapter class.
# Then you would wrap objects with missing features
# inside the adapter, gaining needed features dynamically.
# For this to work, the target classes must have a common
# interface, and the adapter’s field should follow that
# interface. This approach looks very similar to the
# Decorator pattern.
#
### How to Implement
#   ----------------
# 1. Make sure that you have at least two classes with
# incompatible interfaces:
# a. A useful service class, which you can’t change
# (often 3rd-party, legacy or with lots of existing dependencies).
# b. One or several client classes that would benefit
# from using the service class.
# 2. Declare the client interface and describe how
# clients communicate with the service.
# 3. Create the adapter class and make it follow
# the client interface. Leave all the methods empty for now.
# 4. Add a field to the adapter class to store a reference
# to the service object. The common practice is to
# initialize this field via the constructor, but
# sometimes it’s more convenient to pass it to the
# adapter when calling its methods.
# 5. One by one, implement all methods of the client
# interface in the adapter class. The adapter should
# delegate most of the real work to the service object,
# handling only the interface or data format conversion.
# 6. Clients should use the adapter via the client interface.
# This will let you change or extend the adapters without
# affecting the client code.
#
### Pros and Cons
#   -------------
# 1. Pros
# a.  Single Responsibility Principle. You can separate
# the interface or data conversion code from the primary
# business logic of the program.
# b.  Open/Closed Principle. You can introduce new types
# of adapters into the program without breaking the
# existing client code, as long as they work with the
# adapters through the client interface.
# 2. Cons
# a. The overall complexity of the code increases because
# you need to introduce a set of new interfaces and classes.
# Sometimes it’s simpler just to change the service class
# so that it matches the rest of your code.
#
### Realtion to other patterns
#   --------------------------
# 1. Bridge is usually designed up-front, letting you
# develop parts of an application independently of each other.
# On the other hand, Adapter is commonly used with an
# existing app to make some otherwise-incompatible classes
# work together nicely.
# 2. Adapter changes the interface of an existing object,
# while Decorator enhances an object without changing its interface.
# In addition, Decorator supports recursive composition,
# which isn’t possible when you use Adapter.
# 3. Adapter provides a different interface to the wrapped
# object, Proxy provides it with the same interface, and
# Decorator provides it with an enhanced interface.
# 4. Facade defines a new interface for existing objects,
# whereas Adapter tries to make the existing interface usable.
# Adapter usually wraps just one object, while Facade works
# with an entire subsystem of objects.
# 5. Bridge, State, Strategy (and to some degree Adapter)
# have very similar structures. Indeed, all of these patterns
# are based on composition, which is delegating work to other
# objects. However, they all solve different problems.
# A pattern isn’t just a recipe for structuring your code
# in a specific way. It can also communicate to other
# developers the problem the pattern solves.


class RoundPeg:
    """ Defines a round peg """
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def get_radius(self) -> float:
        """ returns the radius of a peg """
        return self.radius

class RoundHole:
    """ Defines a hole """
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def get_radius(self) -> float:
        """ returns the radius of the hole """
        return self.radius

    def fits(self, peg: RoundPeg) -> bool:
        """ determines if a peg can go through a hole """
        return self.get_radius() >= peg.get_radius()

class SquarePeg:
    """ Defines a square peg """

    def __init__(self, width: float) -> None:
        self.width: float = width

    def get_width(self) -> float:
        """ returns the width of the Peg """
        return self.width

class SquarePegAdapter(SquarePeg):
    """ Defines a square Peg """
    def __init__(self, peg: SquarePeg) -> None:
        super(SquarePeg, self).__init__()
        self.peg: SquarePeg = peg

    def get_radius(self) -> float:
        """ returns the width of the peg """
        return self.peg.get_width() * sqrt(2) / 2


if __name__ == "__main__":

    hole = RoundHole(5)
    rpeg = RoundPeg(5)
    print(hole.fits(rpeg)) # true

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    # print(hole.fits(small_sqpeg)) # this won't compile (incompatible types)

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
    print(hole.fits(small_sqpeg_adapter)) # true
    print(hole.fits(large_sqpeg_adapter)) # false
