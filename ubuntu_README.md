# (K)Ubuntu installation and configuration #

These are the install and configuration instruction to get pirateplay running locally. They have been made on a new install of Kubuntu 15.10, but probably work well for all debian based distributions.

## Installing dependecies

Check the version
```console
$ python -V
Python 2.7.10
```

Install the Python version manager
```console
$ sudo apt-get install python-pip
...
```

Install the dependencies
```console
$ pip install cherrypy
Downloading/unpacking cherrypy
  Downloading CherryPy-3.8.0.tar.gz (433kB): 433kB downloaded
  Running setup.py (path:/tmp/pip-build-OQFzMd/cherrypy/setup.py) egg_info for package cherrypy
    
Installing collected packages: cherrypy
  Running setup.py install for cherrypy
    changing mode of build/scripts-2.7/cherryd from 664 to 775
    
    changing mode of /home/user_name/.local/bin/cherryd to 775
Successfully installed cherrypy
Cleaning up...
```

```console
$ pip install setuptools
Downloading/unpacking setuptools
  Downloading setuptools-18.5-py2.py3-none-any.whl (462kB): 462kB downloaded
Installing collected packages: setuptools
Successfully installed setuptools
Cleaning up...
```

I got a warning when installing genshi, but things worked out anyway

```console
$ pip install genshi
Downloading/unpacking genshi
  Downloading Genshi-0.7.tar.gz (491kB): 491kB downloaded
  Running setup.py (path:/tmp/pip-build-TD_zPf/genshi/setup.py) egg_info for package genshi
    
    warning: no previously-included files matching '*' found under directory 'doc/logo.lineform'
    warning: no previously-included files found matching 'doc/2000ft.graffle'
    warning: no previously-included files matching '*.pyc' found anywhere in distribution
Installing collected packages: genshi
  Running setup.py install for genshi
    building 'genshi._speedups' extension
    x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fno-strict-aliasing -D_FORTIFY_SOURCE=2 -g -fstack-protector-strong -Wformat -Werror=format
-security -fPIC -I/usr/include/python2.7 -c genshi/_speedups.c -o build/temp.linux-x86_64-2.7/genshi/_speedups.o
    genshi/_speedups.c:14:20: fatal error: Python.h: No such file or directory
    compilation terminated.
    **********************************************************************
    WARNING:
    An optional C extension could not be compiled, speedups will not be
    available.
    **********************************************************************
    command 'x86_64-linux-gnu-gcc' failed with exit status 1
    
    warning: no previously-included files matching '*' found under directory 'doc/logo.lineform'
    warning: no previously-included files found matching 'doc/2000ft.graffle'
    warning: no previously-included files matching '*.pyc' found anywhere in distribution
Successfully installed genshi
Cleaning up...
```

There are several version of python packages. This one is the right one us.

```console
$ pip install python-twitter
Downloading/unpacking python-twitter
  Downloading python_twitter-2.2-py2-none-any.whl (60kB): 60kB downloaded
Downloading/unpacking requests (from python-twitter)
  Downloading requests-2.8.1-py2.py3-none-any.whl (497kB): 497kB downloaded
Downloading/unpacking requests-oauthlib (from python-twitter)
  Downloading requests_oauthlib-0.5.0-py2.py3-none-any.whl
Downloading/unpacking oauthlib>=0.6.2 (from requests-oauthlib->python-twitter)
  Downloading oauthlib-1.0.3.tar.gz (109kB): 109kB downloaded
  Running setup.py (path:/tmp/pip-build-NL8JQF/oauthlib/setup.py) egg_info for package oauthlib
    
Installing collected packages: python-twitter, requests, requests-oauthlib, oauthlib
  Running setup.py install for oauthlib
    
Successfully installed python-twitter requests requests-oauthlib oauthlib
Cleaning up...
```

We also need to create the configuration file. Copy the ```config.ini.example``` in the git root directory.
```console
$ cp config.examle config.ini
```

This file can be used without modification to run your server locally.

You can now start the server like this.
```console
$ python app.wsgi
PyAMF not found! Brightcove support dissabled!
PyAMF not found! Brightcove support dissabled!
[13/Dec/2015:22:57:11] ENGINE Listening for SIGHUP.
[13/Dec/2015:22:57:11] ENGINE Listening for SIGTERM.
[13/Dec/2015:22:57:11] ENGINE Listening for SIGUSR1.
[13/Dec/2015:22:57:11] ENGINE Bus STARTING
[13/Dec/2015:22:57:11] ENGINE Started monitor thread '_TimeoutMonitor'.
[13/Dec/2015:22:57:11] ENGINE Started monitor thread 'Autoreloader'.
[13/Dec/2015:22:57:11] ENGINE Serving on http://0.0.0.0:8082
[13/Dec/2015:22:57:11] ENGINE Bus STARTED
```

Note that although the config files states that ```server.socket_port = 80``` the server still binds this service to port ```8082```.

You can now start using your service by navigatin to [http://localhost:8082](http://localhost:8082)