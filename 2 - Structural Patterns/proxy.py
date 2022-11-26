""" proxy.py """

### Intent
#   ------
# Proxy is a structural design pattern that
# lets you provide a substitute or placeholder
# for another object. A proxy controls access
# to the original object, allowing you to perform
# something either before or after the request
# gets through to the original object.
#
### Problem
#   -------
# Why would you want to control access to an object?
# Here is an example: you have a massive object that
# consumes a vast amount of system resources.
# You need it from time to time, but not always.
#
# You could implement lazy initialization: create
# this object only when it’s actually needed.
# All of the object’s clients would need to execute
# some deferred initialization code. Unfortunately,
# this would probably cause a lot of code duplication.
#
# In an ideal world, we’d want to put this code directly
# into our object’s class, but that isn’t always possible.
# For instance, the class may be part of a closed
# 3rd-party library.
#
### Solution
#   --------
# The Proxy pattern suggests that you create a new
# proxy class with the same interface as an original
# service object. Then you update your app so that it
# passes the proxy object to all of the original
# object’s clients. Upon receiving a request from a
# client, the proxy creates a real service object
# and delegates all the work to it.
#
# But what’s the benefit? If you need to execute
# something either before or after the primary logic
# of the class, the proxy lets you do this without
# changing that class. Since the proxy implements the
# same interface as the original class, it can be
# passed to any client that expects a real service
# object.
#
### Applicability
#   -------------
# There are dozens of ways to utilize the Proxy pattern.
# Let’s go over the most popular uses.
#
# 1. Lazy initialization (virtual proxy). This is when
# you have a heavyweight service object that wastes
# system resources by being always up, even though you
# only need it from time to time.
#
# Instead of creating the object when the app launches,
# you can delay the object’s initialization to a time
# when it’s really needed.
#
# 2. Access control (protection proxy). This is when
# you want only specific clients to be able to use the
# service object; for instance, when your objects are
# crucial parts of an operating system and clients are
# various launched applications (including malicious ones).
#
# The proxy can pass the request to the service object only
# if the client’s credentials match some criteria.
#
# 3. Local execution of a remote service (remote proxy).
# This is when the service object is located on a remote server.
#
# In this case, the proxy passes the client request over
# the network, handling all of the nasty details of working
# with the network.
#
# 4. Logging requests (logging proxy). This is when you
# want to keep a history of requests to the service object.
#
# The proxy can log each request before passing it to the service.
#
# 5. Caching request results (caching proxy). This is when
# you need to cache results of client requests and manage
# the life cycle of this cache, especially if results are
# quite large.
#
# The proxy can implement caching for recurring requests
# that always yield the same results. The proxy may use the
# parameters of requests as the cache keys.
#
# 6. Smart reference. This is when you need to be able to
# dismiss a heavyweight object once there are no clients that
# use it.
#
# The proxy can keep track of clients that obtained a reference
# to the service object or its results. From time to time,
# the proxy may go over the clients and check whether they
# are still active. If the client list gets empty, the proxy
# might dismiss the service object and free the underlying
# system resources.
#
# The proxy can also track whether the client had modified
# the service object. Then the unchanged objects may be
# eused by other clients.
#
### How to Implement
#   ----------------
# 1. If there’s no pre-existing service interface, create
# one to make proxy and service objects interchangeable.
# Extracting the interface from the service class isn’t
# always possible, because you’d need to change all of the
# service’s clients to use that interface. Plan B is to
# make the proxy a subclass of the service class, and
# this way it’ll inherit the interface of the service.
#
# 2. Create the proxy class. It should have a field for
# storing a reference to the service. Usually, proxies
# create and manage the whole life cycle of their services.
# On rare occasions, a service is passed to the proxy via
# a constructor by the client.
#
# 3. Implement the proxy methods according to their purposes.
# In most cases, after doing some work, the proxy should
# delegate the work to the service object.
#
# 4. Consider introducing a creation method that decides
# whether the client gets a proxy or a real service.
# This can be a simple static method in the proxy class
# or a full-blown factory method.
#
# 5. Consider implementing lazy initialization for the
# service object
#
### Pros and Cons
#   -------------
# 1. Pros
#   a. You can control the service object without clients
# knowing about it.
#   b. You can manage the lifecycle of the service object
# when clients don’t care about it.
#   c. The proxy works even if the service object isn’t
# ready or is not available.
#   d. Open/Closed Principle. You can introduce new proxies
# without changing the service or clients.
# 2. Cons
#   a. The code may become more complicated since you
# need to introduce a lot of new classes.
#   b. The response from the service might get delayed.
#
### Relation with Other Patterns
#
# 1. Adapter provides a different interface to the wrapped
# object, Proxy provides it with the same interface, and
# Decorator provides it with an enhanced interface.
#
# 2. Facade is similar to Proxy in that both buffer a
# complex entity and initialize it on its own. Unlike Facade,
# Proxy has the same interface as its service object,
# which makes them interchangeable.
#
# 3. Decorator and Proxy have similar structures, but very
# different intents. Both patterns are built on the composition
# principle, where one object is supposed to delegate some of
# the work to another. The difference is that a Proxy usually
# manages the life cycle of its service object on its own,
# whereas the composition of Decorators is always controlled
# by the client.

from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
