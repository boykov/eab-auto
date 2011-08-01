# f2py -m tmp -h tmp.pyf --overwrite-signature sof.f
f2py -m tmp -c sof.f
# f2py --noarch -m nvcc --f90flags="-ffree-line-length-none" -c Nvecc.f90 ep2p.for only: nvecc ep2

#!/bin/sh -x
# build extension module with f2py

