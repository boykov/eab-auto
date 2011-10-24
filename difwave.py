#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, math
import os, shutil
import point

from numpy import *
# для корректной работы символических ссылок
sys.path.append(os.getcwd())

os.system("make prepare")

# os.system("mpiexec -np 2 python ex11p.py -mat_type dense -ksp_type gmres")

execfile("config_difwave.py")

alpgl = zeros((3,3),order = 'Fortran')

point.GetCoordMatrix(EPST,alpgl_init,alpgl)

print "alpgl_init",alpgl_init
print "alpgl",alpgl
print "epst",EPST

LOCIA = zeros((3),order = 'Fortran')

LOCIA[0:3] = LOCI[0:3]

os.system("make pnt")

import pnt
KT = 0
print "KTMAX=",KTMAX
KT = pnt.point(KT,XT,LOCIA,numpoints,KTMAX)
print "KT=",KT

# KT = point.point(KT,XT,KTMAX,LOCI,numpoints)
# KT = point.SamplingEllipsoide(LOCI,numpoints,XT)
RHSHA = point.get_h(LOCI,NPOYS,RSHAP) # parameter_h

if (KT > 100):
    KOKRM = 100
else:
    KOKRM =  KT

NVECT = zeros((KT,3),order = 'Fortran')
NVECH = zeros((KT,3),order = 'Fortran')        
NOKR = zeros((KT,KOKRM),int32,order = 'Fortran')
ALPHA = zeros((KT,3,3),order = 'Fortran')
BETA = zeros((KT,3,3),order = 'Fortran')

os.system("make nvcc")
import nvcc
HPOYS=2.*LOCI[1]*nvcc.ep2(1.-(LOCI[0]/LOCI[1])**2)/NPOYS # parameter_h
RHSHA= RSHAP*HPOYS                                       # parameter_h


nvcc.nvecc(ALPHA,BETA,RHSHA,LOCI,AOBR,XT,NVECT,NVECH,RSHAP,NOKR,MINKM,KTO,KT,KTMAX,KOKRM)

# # НАПОМИНАНИЕ: НЕСТЫКОВКА point.nvecc, nvcc.nvecc и ntg.integ
# # RHSHA = 0
# # block:
# point.nvecc(ALPHA,BETA,RHSHA,LOCI,AOBR,XT,NVECT,RSHAP,NOKR,MINKM,KTO,KT,KOKRM,numpoints)
NVECH = zeros((KT,3),order = 'Fortran')
# point.nvecc1(ALPHA,BETA,RHSHA,LOCI,AOBR,XT,NVECT,RSHAP,NOKR,MINKM,KTO,KT,KOKRM,numpoints,NVECH)
# # point.nvecc(ALPHA,BETA,RHSHA,LOCI,AOBR,XT,NVECT,RSHAP,NOKR,MINKM,KTO,KT,KOKRM)
# NOKR[0:KT,0:KOKRM] = NOKR[0:KT,0:KOKRM] + 1
# # exit()

# print "ALPHA",ALPHA
# print "BETA",BETA
# print "RHSHA",RHSHA
# print "NVECT",NVECT
# print "NOKR",NOKR

DINTEG = zeros((KT),order = 'Fortran')
DINTE1 = zeros((KT,3),order = 'Fortran')

XTout = zeros((KT,3),order = 'Fortran')
XTout[0:KT,0:3] = XT[0:KT,0:3]
# XT = XTout

os.system("make ntg")
import ntg

ntg.integ(DINTEG,DINTE1,MAXIK,ITIPF,ITIPF1,IDEJ,PARTEL,NOKR,RHSHA,XTout,BETA,ALPHA,AOBR,KREG,KGM,GREG,KFGM,XREG,ALPNY,BETNY,IKOLF,LOCI,EPSPOL,IELL,KOKRM,KT)
exit()
# NOKR[0:KT,0:KOKRM] = NOKR[0:KT,0:KOKRM] - 1
# # point.integ(DINTEG,DINTE1,MAXIK,ITIPF,ITIPF1,IDEJ,PARTEL,NOKR,RHSHA,XTout,BETA,ALPHA,AOBR,KREG,KGM,GREG,KFGM,XREG,ALPNY,BETNY,IKOLF,LOCI,EPSPOL,IELL,KOKRM,KT)
# point.integ(DINTEG,DINTE1,NOKR,RHSHA,XTout,AOBR,KREG,KGM,GREG,KFGM,XREG,ALPNY,BETNY,LOCI,IELL,KOKRM,KT)

print "DINTE1",DINTE1
print "DINTEG",DINTEG

# exit()

XT[0:KT,0:3] = DINTE1[0:KT,0:3]
XTOB = zeros((KT,3),order = 'Fortran')
COSNOR = zeros((KT,3),order = 'Fortran')
XTOB[0:KT,0:3] = XT[0:KT,0:3]
COSNOR[0:KT,0:3] = NVECT[0:KT,0:3]
ASIST = zeros((6,NOBM),complex,order = 'Fortran')

NumberVariantsSolvingTask=1
NEQ=6*KT
NPR=NumberVariantsSolvingTask
NOB=NEQ+NPR

# 
# A.setValue
os.system("make pjdraw")
import pjdrw
pjdrw.pjdraw(betalsr,alflsr,pkasr,PKA,BETAL,ALFL,ASIST,COSNOR,XTOB,DINTEG,pmusr,plasr,NumberLayersModelEnvironment,GAM1,OMEGA,SKOROS,RO1,ROVK,PMUVK,PLAVK,NOB,NOBM,KT)
print "ALFL difwave",ALFL
# new routine kernel(core) should returns (i,j) element of matrix A
# then in ex11p we pass only dimension on matrix A, and 2 functions A(i,j) and b(i)

# b.set
os.system("make akpravw")
import kprvw
INDPR = 3
kprvw.akpravw(DINTEG,ROMEGA,HPRF,T1PRF,ASIST,XTOB,alpgl,COSNOR,XIST,AMOCH,ITIPIS,CKA3,NTPRF,NPRF,NNACH,ZELL,NOB,INDPR,NumberVariantsSolvingTask,NPRFM,NOBM,KT,MaxNumberVariantsSolvingTask)
# new routine right_hand_member should returns (i) element of vector b

# TODO можно прочитать файл for_mn2out.TXT, извлечь оттуда A, b и передать в gmres
# код для чтения подобных файлов есть в norm.py
# А вообще, это будет еще одно ужасное нагромождение.

# ksp.solve(b,x)
os.system("make eqoptw")
import qptw
qptw.eqoptw(NEQ,NPR,NPRM,NEQM)
# new routine solve should gets next parameters: (D,A,b) and returns vector x.

os.system("make akpravw")
import kprvw
INDPR = 2
kprvw.akpravw(DINTEG,ROMEGA,HPRF,T1PRF,ASIST,XTOB,alpgl,COSNOR,XIST,AMOCH,ITIPIS,CKA3,NTPRF,NPRF,NNACH,ZELL,NOB,INDPR,NumberVariantsSolvingTask,NPRFM,NOBM,KT,MaxNumberVariantsSolvingTask)

os.system("make akpolew")
import kplw
kplw.akpolew(SS,FANOM,HPRF,T1PRF,XTOB,DINTEG,alpgl,NEQ,NEQM,INDPR,MaxNumberVariantsSolvingTask,NumberVariantsSolvingTask,NPRF,NTPRF,ZELL,PLAVK,PMUVK,ALFL,BETAL,PKA,GAM1,NNACH,NumberLayersModelEnvironment,plasr,pmusr,pkasr,alflsr,betalsr,NPRFM,KT)


# os.system("make uprall-nvcc")
# # os.system("make akpole")
# import uprupr
# uprupr.uprer(LOCI,AOBR,GR,XR,XT,DINTEG,DINTE1,NVECT,NOKR,ALPHA,BETA,alpgl,RHSHA,KOKRM,KT)

# os.system("make uprall")
# import uprall
#for i in range(10):
# uprall.uprer(LOCI,AOBR,GR,XR,XT,DINTEG,DINTE1,NVECT,NOKR,ALPHA,BETA,RHSHA,KOKRM,KT)


# os.system("python norm.py")
#cmd='diff upr71.TXT fortestupr71.TXT'
#     failure=os.system(cmd)
#cmd='rm fortestupr71.TXT'
#     failure=os.system(cmd)     
#    if failure:
#        print 'running diff failed\n%s' % cmd; sys.exit(1)


# PRCOR(XIST,TIPIS,MaxNumberVariantsSolvingTask,T1PRF,HPRF,NPRF,NTPRF,ZELL,ZSL,NumberLayersModelEnvironment,OMEGA,SIGVK,ROVK,EPSVK,NumberVariantsSolvingTask,SIG,ROSR,SKORSR,KLTCHH,LOCI,ALPGL,NREJM)
