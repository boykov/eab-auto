import os
import re
import sys
def set_paths(root="/home/$USER/projects/sage-4.3.3"):
    """
    Set paths necessary to import sage.
    root ... the path to your Sage installation
    """
    python_path = [
        root+"/local/lib/python",
        root+"/local/lib/python2.6/lib-dynload",
        root+"/local/lib/python2.6/site-packages",
            ]
    sys.path = python_path + sys.path
    paths = {
            "SAGE_ROOT": root,
            "SAGE_DOC": root +  "/devel/sage/doc",
            "SAGE_LOCAL": root+"/local",
            "DOT_SAGE": "~/.sage/",
            "SAGE_SERVER": "http://www.sagemath.org/",
            "PATH": root+"/local/bin:"+os.environ["PATH"],
            }
    os.environ.update(paths)
def import_sageall():
    """
    Imports sage by "import sage.all".
    If it fails, write a helpful message and exit. After executing this method,
    you can be sure that sage just works, e.g you can do
    from sage.all import something
    without worrying.
    """
    try:
        import sage.all
    except ImportError, e:
        if re.match("(.*).so: cannot open shared object file: No such file or directory", e.message):
            # all seems to be just a LD_LIBRARY_PATH problem in 99% of cases
            print """\
"import sage.all" failed when importing an .so library, this is most probably
an LD_LIBRARY_PATH problem, please set your LD_LIBRARY_PATH and try again, e.g. execute:
LD_LIBRARY_PATH=%s/local/lib python %s""" % (os.environ.get("SAGE_ROOT", ""),
        sys.argv[0])
            sys.exit()
        else:
            # some other problem
            raise
set_paths()
import_sageall()
from sage.all import *
var("x")
e = x**2/3-log(x)
print e
print integrate(e, x)
