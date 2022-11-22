""" abstract_factory.py """

from abc import ABC, abstractmethod

### Intent
#   ------
# Abstract Factory is a creational design pattern that lets
# you produce families of related objects without specifying
# their concrete classes.

### Problem
#   -------
# Imagine that you're creating a furniture shop simulator.
# Your code consists of classes that represent:
# 1. A family of related products, say: Chair + Sofa + CoffeeTable.
# 2. Several variants of this family.
#   For example, products Chair + Sofa + CoffeeTable are
#   available in these variants: Modern, Victorian, ArtDeco.
#
# You need a way to create individual furniture objects
# so that they match other objects of the same family.
# Customers get quite mad when they receive non-matching furniture.
#
# Also, you don’t want to change existing code when adding new products
# or families of products to the program. Furniture vendors update their
# catalogs very often, and you wouldn’t want to change the core code
# each time it happens.

### Solution
#   --------
#
# The first thing the Abstract Factory pattern suggests is to explicitly
# declare interfaces for each distinct product of the product family
# (e.g., chair, sofa or coffee table). Then you can make all variants
# of products follow those interfaces. For example, all chair variants
# can implement the Chair interface; all coffee table variants can
# implement the CoffeeTable interface, and so on.
#
# The next move is to declare the Abstract Factory—an interface with a
# list of creation methods for all products that are part of the product
# family (for example, createChair, createSofa and createCoffeeTable).
# These methods must return abstract product types represented by the
# interfaces we extracted previously: Chair, Sofa, CoffeeTable and so on.
#
# Now, how about the product variants? For each variant of a product family,
# we create a separate factory class based on the AbstractFactory interface.
# A factory is a class that returns products of a particular kind. For example,
# the ModernFurnitureFactory can only create ModernChair, ModernSofa and
# ModernCoffeeTable objects.
#
# The client code has to work with both factories and products via their
# respective abstract interfaces. This lets you change the type of a factory
# that you pass to the client code, as well as the product variant that the
# client code receives, without breaking the actual client code.

### Application
#   -----------
# 1.  Use the Abstract Factory when your code needs to work with various
#     families of related products, but you don’t want it to depend on the
#     concrete classes of those products—they might be unknown beforehand
#     or you simply want to allow for future extensibility.
#
#     The Abstract Factory provides you with an interface for creating objects
#     from each class of the product family. As long as your code creates objects
#     via this interface, you don’t have to worry about creating the wrong variant
#     of a product which doesn’t match the products already created by your app.
#
#     a. Consider implementing the Abstract Factory when you have a class with a
#           set of Factory Methods that blur its primary responsibility.
#
#     b. In a well-designed program each class is responsible only for one thing.
#           When a class deals with multiple product types, it may be worth extracting
#           its factory methods into a stand-alone factory class or a full-blown
#           Abstract Factory implementation.

### How to Implement
#   ----------------
# 1. Map out a matrix of distinct product types versus variants of these products.
# 2. Declare abstract product interfaces for all product types. Then make all
#       concrete product classes implement these interfaces.
# 3. Declare the abstract factory interface with a set of creation methods
#       for all abstract products.
# 4. Implement a set of concrete factory classes, one for each product variant.
# 5. Create factory initialization code somewhere in the app.
#       It should instantiate one of the concrete factory classes,
#       depending on the application configuration or the current environment.
#       Pass this factory object to all classes that construct products.
# 6. Scan through the code and find all direct calls to product constructors.
#       Replace them with calls to the appropriate creation method on the factory
#       object.

### Pros and Cons
#   -------------
# 1. Pros
#   a. You can be sure that the products you’re getting from a factory are compatible
#       with each other.
#   b. You avoid tight coupling between concrete products and client code.
#   c.  Single Responsibility Principle. You can extract the product creation code
#       into one place, making the code easier to support.
#   d. Open/Closed Principle. You can introduce new variants of products without
#       breaking existing client code.
# 2. Cons
#   a. The code may become more complicated than it should be, since a lot of new
#       interfaces and classes are introduced along with the pattern.

### Relation with Other Patterns
#   ----------------------------
# 1. Many designs start by using Factory Method
#      (less complicated and more customizable via subclasses) and evolve toward
#   Abstract Factory, Prototype, or Builder (more flexible, but more complicated).
# 2. Builder focuses on constructing complex objects step by step.
#   Abstract Factory specializes in creating families of related objects.
#   Abstract Factory returns the product immediately, whereas Builder lets you run
#   some additional construction steps before fetching the product.
# 3. Abstract Factory classes are often based on a set of Factory Methods,
#   but you can also use Prototype to compose the methods on these classes.
# 4. Abstract Factory can serve as an alternative to Facade when you only want to
#   hide the way the subsystem objects are created from the client code.
# 5. You can use Abstract Factory along with Bridge. This pairing is useful when
#   some abstractions defined by Bridge can only work with specific implementations.
#   In this case, Abstract Factory can encapsulate these relations and hide the
#   complexity from the client code.
# 6. Abstract Factories, Builders and Prototypes can all be implemented as Singletons.


class Chair(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def sit_on(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def can_purchase(self) -> bool:
        raise NotImplementedError


class CoffeeTable(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def sit_on(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def can_purchase(self) -> bool:
        raise NotImplementedError


class Sofa(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def sit_on(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def can_purchase(self) -> bool:
        raise NotImplementedError


class ModernChair(Chair):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return True

    def can_purchase(self) -> bool:
        return True


class VictorianChair(Chair):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return True

    def can_purchase(self) -> bool:
        return True


class ArtDecoChair(Chair):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return True

    def can_purchase() -> bool:
        return False


class ModernSofa(Sofa):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return True

    def can_purchase(self) -> bool:
        return True


class VictorianSofa(Sofa):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return True

    def can_purchase(self) -> bool:
        return True


class ArtDecoSofa(Sofa):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return True

    def can_purchase(self) -> bool:
        return False


class ModernCoffeeTable(CoffeeTable):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return False

    def can_purchase(self) -> bool:
        return True


class VictorianCoffeeTable(CoffeeTable):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return False

    def can_purchase(self) -> bool:
        return True


class ArtDecoTable(CoffeeTable):
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> bool:
        return False

    def can_purchase(self) -> bool:
        return False


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        raise NotImplementedError
    
    @abstractmethod
    def create_sofa(self) -> Sofa:
        raise NotImplementedError
    
    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        raise NotImplementedError


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()
    
    def create_sofa(self) -> ModernSofa:
        return ModernSofa()
    
    def create_coffee_table() -> ModernCoffeeTable:
        return ModernCoffeeTable()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()
    
    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()
    
    def create_coffee_table() -> VictorianCoffeeTable:
        return VictorianCoffeeTable()


class ArtDecoFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ArtDecoChair:
        return ArtDecoChair()
    
    def create_sofa(self) -> ArtDecoSofa:
        return ArtDecoSofa()
    
    def create_coffee_table() -> ArtDecoCoffeeTable:
        return ArtDecoCoffeeTable()