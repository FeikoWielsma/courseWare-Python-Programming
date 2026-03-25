#!/usr/bin/env python
"""
findgtk.py - Find the pyGTK libraries, wherever they are.
"""
import os
import sys
sys.path.append("/usr/local/lib/python2.3/site-packages/")

def try_import():
    import sys
    """tries to import gtk and if successful, returns 1"""
    #print "Attempting to load gtk...Path=%s"%sys.path
    # To require 2.0
    try:
        import pygtk
        pygtk.require("2.0")
    except:
        print "pyGTK not found. You need GTK 2 to run this."
        print "Did you \"export PYTHONPATH=/usr/local/lib/python2.2/site-packages/\" first?"
        print "Perhaps you have GTK2 but not pyGTK, so I will continue to try loading."
        
        
    try:
        import gtk,gtk.glade
        import atk,pango #for py2exe
        import gobject
    except:
        import traceback,sys
        traceback.print_exc(file=sys.stdout)
        print "I'm sorry, you apparently do not have GTK2 installed - I tried"
        print "to import gtk, gtk.glade, and gobject, and I failed."
     
        return 0
    return 1

if not try_import():
    site_packages=0
    #for k in sys.path:
    #    if k.count("site-packages"):
    #        print "existing site-packages path %s found\n"%k
    #        site_packages=1
    if site_packages == 0:
        from stat import *
        #print "no site-packages path set, checking.\n"
        check_lib = [ "/usr/lib/python2.2/site-packages/",
                        "/usr/local/lib/python2.2/site-packages/",
                        "/usr/local/lib/python2.3/site-packages/" ]
        for k in check_lib:
            try:
                path=os.path.join(k,"pygtk.py")
                #print "Path=%s"%path
                if open(path)!=None:
                    #print "appending", k
                    sys.path=[k]+sys.path
                    if try_import():
                        break
            except:
                pass
    if not try_import():
        sys.exit(0)
