Manifesto
=========

In no particular order:

* *Standard interface*: Interfacing with current embedded software toolchains is non-standard to say the least. The closest we can get to 
some sort of universal interface is the combination of Makefiles for building and GDB/MI for debugging. 
The BlockWorks Build environment is an attempt to expose those interfaces to the developer in an easy to use, encapsulated way.

* *Do similar things in a similar way*:
Having a standard way of Building & Testing on multiple platforms should allowhigh quality tools to be buit on top of it. 

* *Automation*: The build environment shoud lend itself to build & test automation. If you repeat it, automate it.

* *Open Source*: All BlockWorks code is open. All the toolchains wrapped up in BlockWorks are open.

* *Multi-Platform*: Maintaining code that is Buildable/Runnable/Debuggable across multiple architectures speeds initial development and aids
debugging as different platforms expose different issues (Timing, RAM restriction, etc). Taking account of these differences leads to higher
quality code that is genuinely abtracted away from the platform.

* *Command-Line is not a naughty word*: BlockWorks is definitely aimed at the more expert-end of the spectrum, Proficiency with shells,
Makefiles & gdb is assumed. We are attempting (in the first case) to unify many disparate architecures into a common toolset to allow
better things to be built on top. Initally, that interface is command-line based.

* *Simple*: This can manifest itself in non-obvious ways, sometimes well-encapsualted complexity promotes simplicity e.g. encapsulating a 
build environment inside a VM could be seen as complex, but it promotes a simpler way of working.

* *Libraries, not frameworks*: Small, composable, non-prescriptive modules/classes/tools is what BlockWorks are about, not rigid, long-learning-curve
frameworks that fit no-one very well. This ideal promotes *true* reusability, not theoretical.

* *Everyone works in different ways*: We create blocks to build with... we dont specify what you should build with them or how
you should lay them. For example, editors&IDEs are specifically *not* in our domain, they are very specific to a persons way of working.
Having said that, neither do we think that should be allowed to harm interoperability and portabiity. Separate the editor & debugger from the toolchain.

* *Lightweight*: Flexible, small, single purpose tools > monolithic, rigid, kitchen-sink tools.


In summary, much of this has been said before in the [Unix Philosophy](http://en.wikipedia.org/wiki/Unix_philosophy#Mike_Gancarz:_The_UNIX_Philosophy) but
it bears repeating (as often as necesary).

