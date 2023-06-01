# Demos

This folder contains some demos for both tkinter and pygame.
They are functionally the exact same; it's just a matter of preference.

tkinter comes pre-installed with most versions of Python.
For pygame, you may need to run:
`pip install pygame`

## Use cases

* tkinter tends to be easier for making standard GUI apps;
e.g. it makes buttons very easy, whereas they are hard in pygame.

* pygame tends to be easier for making games;
e.g. it makes setting FPS very easy, whereas synchronizing events is hard in tkinter.

## Hurdles

* One hurdle of tkinter is that essentially all objects need to be kept track of,
or else they disappear. You have to get used to storing references in a global app object.

* One hurdle of pygame is that essentially everything needs to happen within the main loop.
You have to get used to the idea that you don't do things outside the loop, you only
change variables that affect how the loop behaves.

## General notes

* For both of these platforms, I prefer to use a global app object to store variables.
This is because when passing around data between functions, the scope of access can often
be lost. Using an app object allows us to avoid this problem. It's not the cleanest solution,
but it's by far the simplest and the one I recommend for ICS3U until you learn OOP in the future.

* GUI apps do not automatically end until you *either* manually quit it using the X button,
or trash the terminal in VSCode. If you run a program and nothing happens, first make sure
you've actually ended the previous instance.

* There are comments to help you understand. Watch the console as well as the graphic interface.
However, these files are *not* full tutorials, just demos that can be plundered and imitated as needed.
There are many tutorials that will walk you through this step-by-step online.

* These files do not demonstrate importing. Each file is self-contained. In practice, some of the functions
would be much better in their own files, where they could be imported and reused by multiple programs.
(Hey, there's an idea for your own work...)

## TODO

* sounds / music
* collision detection
* app layout and scaling with resolution
