#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *

#############################
#### Ellipsoid subsystem ####
#############################
  
LOCI=[float(0.75),float(1.),float(0.5)] # axes
AOBR=[float(0.0),float(0.0),float(0.0)] # axesInverse

AOBR[0]=float(1.)/LOCI[0]
AOBR[1]=float(1.)/LOCI[1]
AOBR[2]=float(1.)/LOCI[2]

#############################
#### Constants subsystem ####
#############################

GR_=array([0.153240036697161e-3,0.154552319473658e-2,0.646988906855853e-2,0.171975750465530e-1,0.338545650168141e-1,0.528837887669642e-1,0.674522193814378e-1,0.700695077086663e-1,0.562729364028081e-1,0.274340887100975e-1,0.261262346519463e-3,0.257439864560872e-2,0.104061165793522e-1,0.263432809025498e-1,0.485406278645065e-1,0.692843956898047e-1,0.776735691605555e-1,0.654895370333966e-1,0.327601451110397e-1,0.0e0,0.468517784034697e-3,0.447452171301441e-2,0.172468637802350e-1,0.408144263885440e-1,0.684471834216533e-1,0.852847691719388e-1,0.768180932672226e-1,0.397789578066906e-1,2.0e0,0.892688033689207e-3,0.816292563230469e-2,0.294222112895286e-1,0.631463787088913e-1,0.917338032797953e-1,0.906988246126861e-1,0.492765017764381e-1,3.0e0,0.183107580686930e-2,0.157202971849451e-1,0.512895711296162e-1,0.945771867485412e-1,0.107376499736781e-0,0.625387027265809e-1,4.0,0.411382520309900e-2,0.320556007229620e-1,0.892001612215900e-1,0.126198961899911e0,0.817647842857709e-1,5.0,0.103522407499181e-1,0.686338871729231e0,0.143458789799214e0,0.110888415611278e0,6.0e0,0.299507030085807e-1,0.146246269239866e0,0.157136361064887e0,7.0e0,0.0e0]) #,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0])
# A_k

XR_=array([0.491257073594768e-1,0.128289925425592e0,0.234652320451892e0,0.360390511345290e0,0.496192873585126e0,0.631992149550662e0,0.757718803867476e0,0.864049765949771e0,0.943101849466342e0,0.989031547543826e0,0.587541357867258e-1,0.152563157986763e0,0.276731428259665e0,0.420305943648837e0,0.570546354612187e0,0.714108911660780e0,0.838240483235925e0,0.931915470406232e0,0.986834114402886e0,0.0e0,0.714910350400931e-1,0.184228296416716e0,0.330447728175639e0,0.494402921815511e0,0.658348008522798e0,0.804524831511260e0,0.917099382514349e0,0.983902240448079e0,2.0e0,0.888168334369972e-1,0.226482753408562e0,0.399978486721007e0,0.585997855402940e0,0.759445873951942e0,0.896910970851951e0,0.979867226226599e0,3.0e0,0.113194383822438e0,0.284318872688286e0,0.490963586835248e0,0.697563081977109e0,0.868436058342015e0,0.974095444906333e0,4.0e0,0.148945787052984e0,0.365666527369113e0,0.610113612934481e0,0.826519679228304e0,0.965421060081785e0,5.0e0,0.204148582103227e0,0.482952704895632e0,0.761399262448138e0,0.951499450553003e0,6.0e0,0.294997790111502e0,0.652996233961648e0,0.927005975926850e0,7.0e0,0.0e0]) #,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0,0.0e0])
# x_k

EPS_ = array([0.0000000000000000,0.0000000000000000,0.0000000000000000,
             0.0000000000000000,0.0000000000000000,1.00000000000000000,
             0.0000000000000000,-1.00000000000000000,0.0000000000000000,
             0.0000000000000000,0.0000000000000000,-1.00000000000000000,
             0.0000000000000000,0.0000000000000000,0.0000000000000000,
             1.00000000000000000,0.0000000000000000,0.0000000000000000,
             0.0000000000000000,1.00000000000000000,0.0000000000000000,
             -1.00000000000000000,0.0000000000000000,0.0000000000000000,
             0.0000000000000000,0.0000000000000000,0.0000000000000000])

# http://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB_%D0%9B%D0%B5%D0%B2%D0%B8-%D0%A7%D0%B8%D0%B2%D0%B8%D1%82%D1%8B
# LEVI_CHEVITA

alpgl_init = zeros((3,3),order = 'Fortran')

alpgl_init[0,0]=1.
alpgl_init[0,1]=0.
alpgl_init[0,2]=0.

alpgl_init[1,0]=0.
alpgl_init[1,1]=1.
alpgl_init[1,2]=0.

alpgl_init[2,0]=0.
alpgl_init[2,1]=0.
alpgl_init[2,2]=1.

# откуда берутся эти начальные данные? Независимо, 0. здесь или 1., все равно alpgl получается единичной матрицей.

GR_.shape=(6,10)
XR_.shape=(6,10)
EPS_.shape = (3,3,3)

EPST = EPS_

GR=GR_.transpose()
XR=XR_.transpose()

############################
####  Points subsystem  ####
############################

KT = 0    # number_points # np

RSHAP=2.0 # radius_hat
MINKM=5   # length_minimums
KTO=50    # max_neighbors

KTMAX = 1000          # max_np
XT = zeros((1000,3))  # points_array
numpoints = 100 # approximate_np

NPOYS = int(0.5+math.sqrt(1.*numpoints)) # one_dimension_np # sqrt_np

#############################
#### Ellipsoid subsystem ####
#############################

# тип звездной поверхности
ITIPF = zeros((10),int,order = 'Fortran')
ITIPF1 = zeros((10),int,order = 'Fortran')
IDEJ = zeros((10),int,order = 'Fortran')
PARTEL = zeros((10,13),order = 'Fortran')

MAXIK=10
ITIPF[0]=1 
ITIPF1[0]=2
IDEJ[0]=0

PARTEL[0,0]=-1.0
PARTEL[0,1]=2.0
PARTEL[0,2]=1.0
PARTEL[0,3]=1.0
PARTEL[0,4]=1.0
PARTEL[0,5]=1.0
PARTEL[0,6]=1.0
PARTEL[0,7]=4.0
PARTEL[0,8]=1.0
PARTEL[0,9]=4.0
PARTEL[0,10]=1.0
PARTEL[0,11]=0.0
PARTEL[0,12]=2.0

IKOLF=1
EPSPOL=0.00001

IELL=0 
#######################################################

KLTCH=9
KREG=KLTCH+1
KGM=10

GREG = zeros((10),order = 'Fortran')
XREG = zeros((10),order = 'Fortran')

GREG[0:(KLTCH + 1)]=GR[0:(KLTCH + 1),10-KLTCH - 1] 
XREG[0:(KLTCH + 1)]=XR[0:(KLTCH + 1),10-KLTCH - 1]

# print 'difwave greg',GREG
# print 'difwave xreg',XREG

KFGM=6*KGM

# функции разбиения единицы
ALPNY=2
BETNY=2

#######################################################

ROSR = zeros((3),order = 'Fortran')
ZSL =  zeros((3),order = 'Fortran')
SKORSR =  zeros((3),order = 'Fortran')

ROSR[0]=20
ZSL[0]=0 
plasr=2.
pmusr=1.
SKORSR[0]=.33
SKORSR[1]=.33
ROSR[1]=.5
ZSL[1]=-2.
SKORSR[2]=.3
ROSR[2]=.5
ZSL[2]=-2.

PLAVK=2.
PMUVK=1.
ROVK=4.

SKOROS = SKORSR[0]
RO1 = ROSR[0]

OMEGA=1.

MaxNumberVariantsSolvingTask=5
NPRM=MaxNumberVariantsSolvingTask
NEQM=6*KTMAX
NOBM=NEQM+NPRM

# not use, i.e. in mpl
ALFL = zeros((2),order = 'Fortran')
BETAL = zeros((2),order = 'Fortran')
PKA = zeros((3),order = 'Fortran')

# not use, i.e. in mpl
alflsr = zeros((2),order = 'fortran')
betalsr = zeros((2),order = 'fortran')
pkasr = zeros((3),order = 'fortran')

GAM1=2.3

NumberLayersModelEnvironment=1
#######################################################

# (NNACH,DINTEG,OMEGRO,HPRF,T1PRF,ASIST,XTOB,ALPGL,COSNOR,XIST,AMOCH,ITIPIS,PPKA,NTPRF,NPRF,NPRFM,ZELL,KT,NumberVariantsSolvingTask,MaxNumberVariantsSolvingTask,NOBM,NOB,INDPR)

NNACH=0
ROMEGA = zeros((5),order = 'fortran')
ROMEGA[0]=ROSR[0]*OMEGA

HPRF = zeros((19,3),order = 'fortran')

NPRF=19
for i in range(0,NPRF,1):
    HPRF[i,0] = 0.05
    HPRF[i,1] = 0.
    HPRF[i,2] = 0.

T1PRF = zeros((19,3),order = 'fortran')
for i in range(0,NPRF,1):
    T1PRF[i,0] = -0.45
    T1PRF[i,1] = -0.45 + 0.05 * i
    T1PRF[i,2] = -0.75

pi=3.14159265358979324

XIST = zeros((5,3),order = 'fortran')
XIST[0,0]=0
XIST[0,1]=0
XIST[0,2]=-2*pi
XIST[1,0]=0.
XIST[1,1]=1.5
XIST[1,2]=-1.0


AMOCH = zeros((5),order = 'fortran')
AMOCH[0:1]=1

ITIPIS = zeros((5),order = 'fortran')
ITIPIS[0] = 0
ITIPIS[1] = 1


CKA3 = zeros((5),order = 'fortran')
CKA3[0]=OMEGA/SKORSR[0]
NTPRF=19

NPRFM=19
ZELL=-1
#######################################################
SS = zeros((19,5),complex,order = 'fortran')
FANOM = zeros((19,5),complex,order = 'fortran')
