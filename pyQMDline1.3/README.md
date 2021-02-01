## pyQMDline beta 1.3
***
### new features :
```text
> fun commands, like popup [message] and sl for people who misspell ls
> themes! all themes are *.pqtheme files, currently you can have one theme at the time
  with foreground, background colours and effects,
  the template can be found on ./system/DEFAULTS/DEFAULT-THEME.pqtheme

  * to apply the theme you just do "theme /path/to/my/theme.pqtheme"

> added an exception for KeyboardInterrupt in the main command field
  you have to use "exit" or "exit -f" to exit

> new syntax for WRITE, OVERWRITE and mv:
    * WRITE -F file.txt -C content
    * OVERWRITE -F file.txt -C content
    * mv -F file.txt -D some/place/
> new syntax for printf:
    * prinf [formatted message] instead of printf f'[formated message]'

> qfetch
  fetches information about your device
> netscan
  fetches information about your network
> diskscan
  fetches information about your disks
```

***

### fixes :
```text
> fixed some issues with PATH
    * changed PATH.path to PATH.py
    * fixed the paths
    * added the ROOT variable - it defines where the root of pyQMDline is located 
    * fixed the general sructure of it, defined the PATH in the file and imported
      all needed modules there

> fixed the issue when you go up more than 2 paths up commands that use
  paths don't work by adding the ROOT variable
> kinda fixed the py command

> made *.pyql files support spaces
```

***

### general upgrades, updates and optimizations :
```text
> tested all commands over a 100 times
   :: you can find the most recent test in ./dev/1.3-TESTS.txt ::

> optimised code and fixed some files like PATH.path >> PATH.py

> added a policy
> added requirements.txt

> new file: ./has_agreed_to_policy.bool
> cleaning up .idea and __pycache__ folders

> fclr >> clr; now can actually clear your python console unless you specify the -F flag
which will work amost the same as fclr 

> full support with paths with spaces for WRITE, OVERWRITE and mv
```
# this is not the complete list of everything that has been added
I forgot the rest

***
***
## ~ sidenote ~
### please report any issues with pyQMDline [here](https://github.com/B00bleaTea/pyQMDline/issues/)
### thank you in advance :)
#### - B00bleaTeA
##### ! sorry for any inconsistencies or inaccuracies !
***
***
###### (c) Apache software license 2.0