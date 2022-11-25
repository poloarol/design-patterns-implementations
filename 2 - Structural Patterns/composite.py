""" composite.py """

from typing import List
from abc import ABC, abstractmethod

### Intent
#   ------
# Composite is a structural design pattern
# that lets you compose objects into tree
# structures and then work with these structures
# as if they were individual objects.
#
### Problem
#   -------
# Using the Composite pattern makes sense
# only when the core model of your app can
# be represented as a tree.
#
# For example, imagine that you have two
# types of objects: Products and Boxes.
# A Box can contain several Products as
# well as a number of smaller Boxes.
# These little Boxes can also hold some
# Products or even smaller Boxes, and so on.
#
# Say you decide to create an ordering
# system that uses these classes.
# Orders could contain simple products without
# any wrapping, as well as boxes stuffed
# with products...and other boxes.
# How would you determine the total price of
# such an order?
#
# You could try the direct approach: unwrap
# all the boxes, go over all the products and
# then calculate the total. That would be
# doable in the real world; but in a program,
# it’s not as simple as running a loop.
# You have to know the classes of Products
# and Boxes you’re going through, the nesting
# level of the boxes and other nasty details
# beforehand. All of this makes the direct
# approach either too awkward or even impossible.
#
### Solution
#   --------
# The Composite pattern suggests that you
# work with Products and Boxes through a
# common interface which declares a method
# for calculating the total price.
#
# How would this method work? For a product,
# it’d simply return the product’s price.
# For a box, it’d go over each item the
# box contains, ask its price and then return
# a total for this box. If one of these items
# were a smaller box, that box would also start
# going over its contents and so on, until the
# prices of all inner components were calculated.
# A box could even add some extra cost to the
# final price, such as packaging cost.
#
# The greatest benefit of this approach is
# that you don’t need to care about the concrete
# classes of objects that compose the tree.
# You don’t need to know whether an object is
# a simple product or a sophisticated box.
# You can treat them all the same via the
# common interface. When you call a method,
# the objects themselves pass the request
# down the tree.
#
### Applicability
#   -------------
# 1. Use the Composite pattern when you have
# to implement a tree-like object structure.
#
# The Composite pattern provides you with
# two basic element types that share a common
# interface: simple leaves and complex containers.
# A container can be composed of both leaves and
# other containers. This lets you construct a
# nested recursive object structure that resembles
# a tree.
#
# 2. Use the pattern when you want the client
# code to treat both simple and complex elements
# uniformly.
#
# All elements defined by the Composite pattern
# share a common interface. Using this interface,
# the client doesn’t have to worry about the
# concrete class of the objects it works with.
#
### How to Implement
#   ----------------
# 1. Make sure that the core model of your
# app can be represented as a tree structure.
# Try to break it down into simple elements
# and containers. Remember that containers
# must be able to contain both simple elements
# and other containers.
#
# 2. Declare the component interface with a list
# of methods that make sense for both simple
# and complex components.
#
# 3. Create a leaf class to represent simple
# elements. A program may have multiple different
# leaf classes.
#
# 4. Create a container class to represent complex
# elements. In this class, provide an array field
# for storing references to sub-elements. The array
# must be able to store both leaves and containers,
# so make sure it’s declared with the component
# interface type.
#
# 5. While implementing the methods of the component
# interface, remember that a container is supposed
# to be delegating most of the work to sub-elements.
#
# 6. Finally, define the methods for adding and
# removal of child elements in the container.
#
# 7. Keep in mind that these operations can be declared
# in the component interface. This would violate the
# Interface Segregation Principle because the methods
# will be empty in the leaf class. However, the client
# will be able to treat all the elements equally, even
# when composing the tree.
#
### Pros and Cons
#   -------------
# 1. Pros
# a. You can work with complex tree structures more
# conveniently: use polymorphism and recursion to
# your advantage.
# b. Open/Closed Principle. You can introduce new
# element types into the app without breaking the
# existing code, which now works with the object tree.
# Cons
# a. It might be difficult to provide a common
# interface for classes whose functionality differs
# too much. In certain scenarios, you’d need to
# overgeneralize the component interface, making it
# harder to comprehend.
#
### Relation to Other Patterns
#   --------------------------
# 1. You can use Builder when creating complex
# Composite trees because you can program its
# construction steps to work recursively.
# 2. Chain of Responsibility is often used in
# conjunction with Composite. In this case,
# when a leaf component gets a request,
# it may pass it through the chain of all of
# the parent components down to the root of
# the object tree.
#
# 3. You can use Iterators to traverse Composite
# trees.
#
# 4. You can use Visitor to execute an operation
# over an entire Composite tree.
#
# 5. You can implement shared leaf nodes of the
# Composite tree as Flyweights to save some RAM.
#
# 6. Composite and Decorator have similar structure
# diagrams since both rely on recursive composition
# to organize an open-ended number of objects.
#
# 7. A Decorator is like a Composite but only has
# one child component. There’s another significant difference:
# Decorator adds additional responsibilities to
# the wrapped object, while Composite just
# “sums up” its children’s results.
#
# 8. However, the patterns can also cooperate:
# you can use Decorator to extend the behavior
# of a specific object in the Composite tree.
#
# 9. Designs that make heavy use of Composite and
# Decorator can often benefit from using Prototype.
# Applying the pattern lets you clone complex structures
# instead of re-constructing them from scratch.
#
# A good example would be the folder/directory system.
# Added a much simplified version

class File: # leaf
    """ Defines a file """

    def __init__(self, name: str, content: str|bytes) -> None:
        self.name: str = name
        self.content: str|bytes = content

    def operation(self):
        """ tells it is a leaf """
        return "Leaf"


class Component(ABC):
    """ Defines a component """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._parent: Component

    @property
    def parent(self) -> "Component":
        """ defines a parent """
        return self._parent

    @parent.setter
    def parent(self, parent: "Component") -> None:
        self._parent = parent

    def add_folder(self, folder: "Component") -> None:
        """ Add a folder """

    def add_file(self, file: File) -> None:
        """ Add a file """

    def remove_folder(self, folder: "Component") -> None:
        """ remove a folder """

    def remove_file(self, file: File) -> None:
        """ remove a file """

    @abstractmethod
    def operation(self) -> str:
        """ Operation to be performed """
        raise NotImplementedError

class Folder(Component):
    """ Decribes a Folder """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._list_children: List[Component|File] = []

    def add_file(self, file: File) -> None:
        self._list_children.append(file)

    def add_folder(self, folder: "Component") -> None:
        self._list_children.append(folder)

    def remove_file(self, file: File) -> None:
        pass

    def remove_folder(self, folder: "Component") -> None:
        pass

    def operation(self) -> str:
        """ finds all leaves """
        results = []
        for child in self._list_children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"
