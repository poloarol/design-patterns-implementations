""" bridge.py """

from typing import Dict, Final

### Intent
#   ------
# Bridge is a structural design pattern that
# lets you split a large class or a set of
# closely related classes into two separate
# hierarchies—abstraction and implementation—which
# can be developed independently of each other
#
### Problem
#   -------
# Abstraction? Implementation? Sound scary?
# Stay calm and let’s consider a simple example.
#
# Say you have a geometric Shape class with
# a pair of subclasses: Circle and Square.
# You want to extend this class hierarchy to
# incorporate colors, so you plan to create Red
# and Blue shape subclasses. However, since you
# already have two subclasses, you’ll need to create
# four class combinations such as BlueCircle and RedSquare.
#
# Adding new shape types and colors to the hierarchy
# will grow it exponentially. For example, to add a
# triangle shape you’d need to introduce two subclasses,
# one for each color. And after that, adding a new color
# would require creating three subclasses, one for each
# shape type. The further we go, the worse it becomes.
#
### Solution
#   --------
# This problem occurs because we’re trying to
# extend the shape classes in two independent dimensions:
# by form and by color. That’s a very common issue with
# class inheritance.
#
# The Bridge pattern attempts to solve this problem
# by switching from inheritance to the object composition.
# What this means is that you extract one of the dimensions
# into a separate class hierarchy, so that the original
# classes will reference an object of the new hierarchy,
# instead of having all of its state and behaviors within
# one class.
#
# Following this approach, we can extract the color-related
# code into its own class with two subclasses: Red and Blue.
# The Shape class then gets a reference field pointing to one
# of the color objects. Now the shape can delegate any
# color-related work to the linked color object. That reference
# will act as a bridge between the Shape and Color classes.
# From now on, adding new colors won’t require changing the
# shape hierarchy, and vice versa.
#
### Abstraction and Implementation
#   ------------------------------
# Abstraction (also called interface) is a high-level
# control layer for some entity. This layer isn’t supposed
# to do any real work on its own. It should delegate the work
# to the implementation layer (also called platform).
#
# Note that we’re not talking about interfaces or abstract
# classes from your programming language. These aren’t the
# same things.
#
# When talking about real applications, the abstraction can
# be represented by a graphical user interface (GUI), and
# the implementation could be the underlying operating
# system code (API) which the GUI layer calls in response
# to user interactions.
#
# Generally speaking, you can extend such an app in two
# independent directions:
#
# 1. Have several different GUIs
# (for instance, tailored for regular customers or admins).
# 2. Support several different APIs
# (for example, to be able to launch the app under Windows, Linux, and macOS).
#
# In a worst-case scenario, this app might look like
# a giant spaghetti bowl, where hundreds of conditionals
# connect different types of GUI with various APIs all
# over the code.
#
# You can bring order to this chaos by extracting the
# code related to specific interface-platform combinations
# into separate classes. However, soon you’ll discover that
# there are lots of these classes. The class hierarchy will
# grow exponentially because adding a new GUI or supporting
# a different API would require creating more and more classes.
#
# Let’s try to solve this issue with the Bridge pattern.
# It suggests that we divide the classes into two hierarchies:
#
# 1. Abstraction: the GUI layer of the app.
# 2. Implementation: the operating systems’ APIs.
#
# The abstraction object controls the appearance of the app,
# delegating the actual work to the linked implementation object.
# Different implementations are interchangeable as long as they
# follow a common interface, enabling the same GUI to work
# under Windows and Linux.
#
# As a result, you can change the GUI classes without touching
# the API-related classes. Moreover, adding support for another
# operating system only requires creating a subclass in the
# implementation hierarchy.
#
### Applicability
#   ------------
# 1. Use the Bridge pattern when you want to divide and
# organize a monolithic class that has several variants
# of some functionality (for example, if the class can
# work with various database servers).
#
# The bigger a class becomes, the harder it is to figure
# out how it works, and the longer it takes to make a change.
# The changes made to one of the variations of functionality
# may require making changes across the whole class, which
# often results in making errors or not addressing some
# critical side effects.
#
# The Bridge pattern lets you split the monolithic class
# into several class hierarchies. After this, you can change
# the classes in each hierarchy independently of the classes
# in the others. This approach simplifies code maintenance
# and minimizes the risk of breaking existing code.
#
# 2. Use the pattern when you need to extend a class
# in several orthogonal (independent) dimensions.
#
#  The Bridge suggests that you extract a separate
# class hierarchy for each of the dimensions. The original
# class delegates the related work to the objects belonging
# to those hierarchies instead of doing everything on its own.
#
# The Bridge pattern lets you split the monolithic class
# into several class hierarchies. After this, you can
# change the classes in each hierarchy independently
# of the classes in the others. This approach simplifies
# code maintenance and minimizes the risk of breaking
# existing code.
#
# 3. Use the Bridge if you need to be able to switch
# implementations at runtime.
#
# Although it’s optional, the Bridge pattern lets you
# replace the implementation object inside the abstraction.
# It’s as easy as assigning a new value to a field.
#
# By the way, this last item is the main reason why
# so many people confuse the Bridge with the Strategy
# pattern. Remember that a pattern is more than just a
# certain way to structure your classes. It may also
# communicate intent and a problem being addressed.
#
# Identify the orthogonal dimensions in your classes.
# These independent concepts could be: abstraction/platform,
# domain/infrastructure, front-end/back-end, or interface/implementation.
#
# See what operations the client needs and define them
# in the base abstraction class.
#
# Determine the operations available on all platforms.
# Declare the ones that the abstraction needs in the
# general implementation interface.
#
# For all platforms in your domain create concrete
# implementation classes, but make sure they all follow
# the implementation interface.
#
# Inside the abstraction class, add a reference field
# for the implementation type. The abstraction delegates
# most of the work to the implementation object that’s
# referenced in that field.
#
# If you have several variants of high-level logic,
# create refined abstractions for each variant by
# extending the base abstraction class.
#
# The client code should pass an implementation object
# to the abstraction’s constructor to associate one
# with the other. After that, the client can forget
# about the implementation and work only with the
# abstraction object.
#
### Pros and Cons
#   -------------
# 1. Pros
# a. You can create platform-independent classes and apps.
# b. The client code works with high-level abstractions.
# It isn’t exposed to the platform details.
# c. Open/Closed Principle. You can introduce new
# abstractions and implementations independently from
# each other.
# d. Single Responsibility Principle. You can focus on
# high-level logic in the abstraction and on platform
# details in the implementation.
# 2. Cons
# You might make the code more complicated by applying
# the pattern to a highly cohesive class.
#
### Relation with Other Platforms
#   -----------------------------
# 1. Bridge is usually designed up-front, letting you
# develop parts of an application independently of
# each other. On the other hand, Adapter is commonly
# used with an existing app to make some
# otherwise-incompatible classes work together nicely.
#
# 2. Bridge, State, Strategy (and to some degree Adapter)
# have very similar structures. Indeed, all of these
# patterns are based on composition, which is delegating
# work to other objects. However, they all solve
# different problems. A pattern isn’t just a recipe
# for structuring your code in a specific way.
# It can also communicate to other developers the
# problem the pattern solves.
#
# 3. You can use Abstract Factory along with Bridge.
# This pairing is useful when some abstractions defined
# by Bridge can only work with specific implementations.
# In this case, Abstract Factory can encapsulate
# these relations and hide the complexity from the
# client code.
#
# You can combine Builder with Bridge: the director
# class plays the role of the abstraction, while
# different builders act as implementations.

channels: Dict = {0: "CBC", 1: "NBC"}

class Device:
    """
    Defines a device class
    """

    def __init__(self) -> None:
        self.volume_percent: float = 50.0
        self.channel: str = "CBC"
        self.enabled: bool = False
        self.MAX_VOLUME: Final[int] = 100
        self.MIN_VOLUME: Final[int] = 0

    def enable(self) -> None:
        """ Check if the device is enabled """
        self.enabled = True

    def is_enabled(self) -> bool:
        """ Check is the device is enabled """
        return self.enabled

    def disable(self) -> None:
        """ Disable the device """
        return self.disable

    def get_volume(self) -> float:
        """ Get the current device volume """
        return self.volume_percent

    def set_volume(self, percent: float) -> None:
        """ Set the volume """
        if self.get_volume() < percent < self.MAX_VOLUME:
            self.__increase_volume(percent)
            return None

        if self.MIN_VOLUME < percent < self.get_volume():
            self.__decrease_volume(percent)
        return None

    def __increase_volume(self, percent: float) -> None:
        self.volume_percent = percent

    def __decrease_volume(self, percent: float) -> None:
        self.volume_percent = percent

    def get_channel(self) -> str:
        """ Get the current channel """
        return self.channel

    def set_channel(self, new_channel: str) -> None:
        """ Change the channel """
        self.channel = new_channel

class Remote:
    """ Describes a remote """

    def __init__(self, device: Device) -> None:
        self.power: bool = False
        self.device: Device = device

    def __get_channel_list__(self) -> int:
        current_channel: str = self.device.get_channel()
        current_channel_index: int \
            = (i for i in channels.items() if channels[i] == current_channel)[0]
        return current_channel_index

    def toggle_power(self) -> None:
        """ Toggle device power """
        self.power = not self.power

    def volume_down(self) -> None:
        """ Decrease device volume """
        volume: float = self.device.get_volume() - 1
        self.device.set_volume(volume)

    def volume_up(self):
        """ Increase device volume """
        volume: float = self.device.get_volume() + 1
        self.device.set_volume(volume)

    def channel_down(self) -> None:
        """ Get to the previous channel numerically """
        channel_index = self.__get_channel_list__()
        previous_channel: str = channels.get(channel_index - 1)
        self.device.set_channel(previous_channel)

    def channel_up(self) -> None:
        """ Get to the previous channel numerically """
        channel_index = self.__get_channel_list__()
        next_channel: str = channels.get(channel_index + 1)
        self.device.set_channel(next_channel)

class AdvancedRemote(Remote):
    """ Creates an advanced remote """
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def mute(self):
        """ Set's volume to zero i.e. mutes device """
        self.device.set_volume(0.0)

# class TV(Device):
#     """ Defines a TV """
#     def __init__(self) -> None:
#         super().__init__()
#         self.has_screen: bool = True

# class Radio(Device):
#     """ Defines a radio """
#     pass