Platform/Block
============

What is it?
-----------

A set of simple, open, platform-independent libraries to be used as building blocks for
your embedded system.
Together, they form both a Board Support Package (BSP) and a well-tested foundation for the
rest of your application. 
Some of these are written by ourselves, others are collected from external sources and
presented as a cohesive whole for you to pick from.


Get it.
-------

* "git clone BlockWorks.co/Platform.git".

* TBD.


Why do it?
----------

* *Testability*. Specifically at the beginning of lifecycle, but also throughout the life of 
the software, abstracting away from your platform brings many benefits.

* *Switchability*. Switching platforms may initially seem an unlikely thing to happen, but if you dont
allow for it in the initial stages then it will never become an option. Later in the lifecycle, 
platform switching can provide cost benefits

* *Debugability*. Imagine if you could use all the debugging tool available on a desktop sytem
on your target. Having multiple targets to test can give an extra angle on those difficult to solve
bugs.

* *Pre-tested*. All the code you can take from Rocket/Blocks is code you're not writing, debugging,
testing and documenting.

* You benefit from all other projects contributing features & bug fixes in parallel to you.


Demo
----

* DemoOne; Hello world functionality. Shows project organisation & toolchain usage.

* DemoTwo; SimpleConsole over a UART. Demonstrates UART, SimpleConsole, interrupt handling.

