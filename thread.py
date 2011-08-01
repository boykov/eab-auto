from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
ax.set_zlim3d(-1.01, 1.01)

ax.w_zaxis.set_major_locator(LinearLocator(10))
ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

# from mpi4py import MPI
# import numpy as np
# import random
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# mpisize = comm.Get_size()
# nsamples = 120000/mpisize
# inside = 0
# random.seed(rank)
# for i in range(nsamples):
#     x = random.random();
#     y = random.random();
#     if (x*x)+(y*y)<1:
#       inside += 1
# mypi = (4.0 * inside)/nsamples
# pi = comm.reduce(mypi, op=MPI.SUM, root=0)
# if rank==0:
#     print (1.0 / mpisize)*pi

# import multiprocessing as mp
# import numpy as np
# processes = mp.cpu_count()
# nsamples = 1200000/processes
# def calcInsideNumPy(rank):
#     np.random.seed(rank)
#     xy = np.random.random((nsamples,2))**2 # "vectorized" sample gen
#     return 4.0*np.sum(np.sum(xy,1)<1)/nsamples
# if __name__ == '__main__':
#     pool = mp.Pool(processes)
#     result = pool.map(calcInsideNumPy, range(processes))
#     print np.mean(result)


# import multiprocessing as mp
# import numpy as np
# import random
# processes = mp.cpu_count()
# nsamples = 1200000/processes
# def calcInside(rank):
#     inside = 0
#     random.seed(rank)
#     for i in range(nsamples):
#         x = random.random();
#         y = random.random();
#         if (x*x)+(y*y)<1:
#             inside += 1
#     return (4.0*inside)/nsamples
# if __name__ == '__main__':
#     pool = mp.Pool(processes)
#     result = pool.map(calcInside, range(processes))
#     print np.mean(result)

# from threading import Thread
# from Queue import Queue, Empty
# import random
# def calcInside(nsamples,rank):
#     global inside #we need something everyone can share
#     random.seed(rank)
#     for i in range(nsamples):
#         x = random.random();
#         y = random.random();
#         if (x*x)+(y*y)<1:
#             inside += 1
# if __name__ == '__main__':
#     nt=4 # thread count
#     inside = 0 #you need to initialize this
#     samples=100000
#     threads=[Thread(target=calcInside, args=(samples/nt,i)) for i in range
# (nt)]
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#     print (inside*4.0)/samples
