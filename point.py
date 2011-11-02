#!/usr/bin/python
# -*- coding: utf-8 -*-

import math,sys
# import ep2
# from scitools.numpyutils import *
from numpy import *
# from math import cos,sin,pi

# numpoints = 10000.
# TODO если выделять массив pointsEllipsoide динамически,
# то можно numberPointsEllipsoide не использовать, а брать размер этого массива.


# TODO надо ли вообще alpgl_init?
# Все равно эта функция возвращает единичную (Е) матрицу
# Эта матрица используется в akprav и akpole
def GetCoordMatrix(leviChevita,alpgl_init,alpgl):
    e = zeros((3,3))

    # похоже, что alpgl_init это начальная система координат.
    # а alpgl - та, к которой осуществляется переход.
    e[0:3,0:3] = alpgl_init[0:3,0:3]

    dn = 0.

    # НАХОДИМ ТРЕТИЙ НАПРАВЛЯЮЩИЙ ВЕКТОР ПАРАМЕТРИЗАЦИИ
    e[0:3,2] = dn
    for j in range(0,3,1):
        for k in range(0,3,1):
            e[0:3,2] = e[0:3,2] + leviChevita[0:3,j,k] * e[j,0] * e[k,1]

    # НАХОДИМ ПЕРВЫЙ НАПРАВЛЯЮЩИЙ ВЕКТОР ПАРАМЕТРИЗАЦИИ
    e[0:3,0] = dn
    for j in range(0,3,1):
        for k in range(0,3,1):
            e[0:3,0] = e[0:3,0] + leviChevita[0:3,j,k] * e[j,1] * e[k,2]

    # НОРМИРУЕМ
    for j in range(0,3,1):
        dpol = dn
        for i in range(0,3,1):
            dpol = dpol + e[i,j] * e[i,j]
        dpol = 1./ math.sqrt(dpol)
        e[0:3,j] = e[0:3,j] * dpol

    alpgl[0:3,0:3] = e[0:3,0:3]

def get_h(axes,sqrt_np,radius_hat):
    return radius_hat * 2.*axes[1]*ep2p(1.-(axes[0]/axes[1])**2)/sqrt_np

# TODO Возможно, следует повысить точность этого разбиения.
# есть готовые функции, например elliptic_ec(m) в maxima
def ep2p(m):
    """
    Вычисление полного эллиптического интеграла 2-го рода
    """
    a  = array([0.44325141463e0,0.06260601220e0,0.04757383546e0,0.01736506451e0])
    b  = array([0.24998368310e0,0.09200180037e0,0.04069697526e0,0.00526449639e0])
    m1 = 1. - m
    c  = m1
    s1 = 1.
    s2 = 0.
    for i in range(0,4,1):
        s1 = s1 + a[i] * c
        s2 = s2 + b[i] * c
        c  = c * m1
    return s1 - log(m1) * s2

def RadiusHat():
    return 2.0

def LengthMinimumsMax():
    return 5

def NeighborsMax():
    return 50

def PartsOneDimension(totalParts):
    return int(0.5+math.sqrt(totalParts))-5

def DivideOne(eccentricity,parts,angle):
    """Divide 1 to _parts_ portions with some _eccentricity_ and save to _angle_"""
    n = int(parts)
    addon = eccentricity * (parts - n)
    
    angle[0] = 0.
    for i in range(0,n,1):
        angle[i+1] = angle[i] + 1.+ (eccentricity - 1.)*abs((2.*(i+1)-1.)/parts-1.)
        
    coef = 1 / (angle[n] + addon)
    angle[0:n+1] = angle[0:n+1]*coef

# TODO заменить 2 массива asin и acos на один - двумерный, points.
def CompleteSym(parts,asin,acos):
    """Complete arrays asin,acos with parts/2 elements to full parts elements of half of ellipse"""
    rn = 0.5 * parts
    n = int(rn)
    j = n
    for i in range(int(parts) - n,int(parts),1):
        asin[i] = -asin[j]
        acos[i] =  acos[j]
        j = j - 1

def EqualPartsEllipse(axisMin,axisMax,pointsY,pointsX,totalParts):
    """Divide ellipse into _totalParts_ portions. _totalParts_ may has 0.5 addition"""
    pi = 3.14159265358979324
    n = int(totalParts) + 1
    angle = zeros(n)
    eccentricity = axisMax / axisMin
    
    DivideOne(eccentricity,totalParts,angle)
    pointsY[1:n] = axisMin * sin(pi * angle[1:n])
    pointsX[1:n] = axisMax * cos(pi * angle[1:n])

    # TODO
    # n2 = int(totalParts/2) + 1    
    # DivideOne(eccentricity,totalParts / 2,angle)    
    # pointsY[1:n2] = axisMin * sin((pi / 2)* angle[1:n2])
    # pointsX[1:n2] = axisMax * cos((pi / 2)* angle[1:n2])
    # for j in range(n2,n,1):
    #     pointsY[j] =-axisMin * sin((pi / 2)* angle[j - n2 + 1])
    #     pointsX[j] = axisMax * cos((pi / 2)* angle[j - n2 + 1])
        
    pointsX[0] = axisMax
    pointsY[0] = 0

def SamplingEllipsoide(axes,roughParts,points):
    """ Divide ellipsoid by _roughParts_. Return _totalParts_ < _roughParts_.
    Also array _points_ store coordinates (x,y,z) points of sampling.
    axes[0] = Y ? 
    axes[1] = X ? 
    axes[2] = Z ? 
    """
    ellipseParts = PartsOneDimension(roughParts)
    # TODO избавиться от магических констант, а также неудачных имен p5,p7
    # Чем же, в действительности, ограничены размеры этих массивов? 
    p5 = 5 * ellipseParts
    p7 = 7 * ellipseParts
    ellipsePoints = zeros(p5,integer)
    asin = zeros(p5)
    acos = zeros(p5)                 # rename to [1]
    full_points_sin = zeros((p7,p5)) # rename to [2]
    full_points_cos = zeros((p7,p5)) # rename to [0]
    current_sin = zeros(p7)
    current_cos = zeros(p7)
    ellipsePoints[0] = 1
    ellipsePoints[ellipseParts] = 1
    EqualPartsEllipse(axes[0],axes[1],asin,acos,ellipseParts)
    print "ellipseParts ",ellipseParts

    currentEllipseAxes = zeros(3)
    for i in range(1,ellipseParts,1):
        angle = math.sqrt(1.- (acos[i] / axes[1]) ** 2)
        currentEllipseAxes[2] = axes[2] * angle
        currentEllipseAxes[0] = axes[0] * angle
        # этой формулой определяются максимальные значения p5 и p7
        currentEllipseParts = float(int(0.5 + 2.* ellipseParts * angle * axes[0] * ep2p(1.- (axes[2] / axes[0]) ** 2) / (axes[1] * ep2p(1.- (axes[0] / axes[1]) ** 2))))
        if int(currentEllipseParts) % 2 <> 0:
            currentEllipseParts = currentEllipseParts - 1
            # print "currentEllipseParts + 1",currentEllipseParts
        else:
            pass
            # print "currentEllipseParts    ",currentEllipseParts
        EqualPartsEllipse(currentEllipseAxes[2],currentEllipseAxes[0],current_sin,current_cos,currentEllipseParts / 2)
        CompleteSym(currentEllipseParts,current_sin,current_cos)

        ellipsePoints[i] = currentEllipseParts
        full_points_cos[0,i] = currentEllipseAxes[0]
        full_points_cos[1:currentEllipseParts,i] = current_cos[1:currentEllipseParts]
        full_points_sin[1:currentEllipseParts,i] = current_sin[1:currentEllipseParts]
        
    totalParts = 0
    for i in range(0,ellipseParts + 1,1):
        currentNumberPoints = ellipsePoints[i]
        if currentNumberPoints == 0:
            continue
        for j in range(0,currentNumberPoints,1):
            points[totalParts,0] = full_points_cos[j,i]
            points[totalParts,1] = acos[i]
            points[totalParts,2] = full_points_sin[j,i]
            totalParts = totalParts + 1

    # assert(totalParts < roughParts)
    return totalParts

def SamplingEllipsoideNew(axes,roughParts,points,phi,theta):
    """ Divide ellipsoid by _roughParts_. Return _totalParts_ < _roughParts_.
    Also array _points_ store (x,y,z) points of sampling.
    axes[0] = Y ? 
    axes[1] = X ? 
    axes[2] = Z ? 
    """
    ellipseParts = PartsOneDimension(roughParts)
    # TODO избавиться от магических констант, а также неудачных имен p5,p7
    # Чем же, в действительности, ограничены размеры этих массивов? 
    p5 = 5 * ellipseParts
    p7 = 7 * ellipseParts
    ellipsePoints = zeros(p5,integer)
    asin = zeros(p5)
    acos = zeros(p5)                 # rename to [1]
    full_points_sin = zeros((p7,p5)) # rename to [2]
    full_points_cos = zeros((p7,p5)) # rename to [0]
    current_sin = zeros(p7)
    current_cos = zeros(p7)
    ellipsePoints[0] = 1
    ellipsePoints[ellipseParts] = 1
    EqualPartsEllipse(axes[0],axes[1],asin,acos,ellipseParts)
    print "ellipseParts ",ellipseParts

    currentEllipseAxes = zeros(3)
    for i in range(1,ellipseParts,1):
        angle = math.sqrt(1.- (acos[i] / axes[1]) ** 2)
        currentEllipseAxes[2] = axes[2] * angle
        currentEllipseAxes[0] = axes[0] * angle
        # этой формулой определяются максимальные значения p5 и p7
        currentEllipseParts = float(int(0.5 + 2.* ellipseParts * angle * axes[0] * ep2p(1.- (axes[2] / axes[0]) ** 2) / (axes[1] * ep2p(1.- (axes[0] / axes[1]) ** 2))))
        if int(currentEllipseParts) % 2 <> 0:
            currentEllipseParts = currentEllipseParts - 1
            # print "currentEllipseParts + 1",currentEllipseParts
        else:
            pass
            # print "currentEllipseParts    ",currentEllipseParts
        EqualPartsEllipse(currentEllipseAxes[2],currentEllipseAxes[0],current_sin,current_cos,currentEllipseParts / 2)
        CompleteSym(currentEllipseParts,current_sin,current_cos)

        ellipsePoints[i] = currentEllipseParts
        full_points_cos[0,i] = currentEllipseAxes[0]
        full_points_cos[1:currentEllipseParts,i] = current_cos[1:currentEllipseParts]
        full_points_sin[1:currentEllipseParts,i] = current_sin[1:currentEllipseParts]
        
    totalParts = 0
    for i in range(0,ellipseParts + 1,1):
        currentNumberPoints = ellipsePoints[i]
        phi[i] = math.acos(acos[i] / axes[1])
        print "phi:", phi[i]
        if currentNumberPoints == 0:
            continue
        for j in range(0,currentNumberPoints,1):
            points[totalParts,0] = full_points_cos[j,i]
            points[totalParts,1] = acos[i]
            points[totalParts,2] = full_points_sin[j,i]
            if abs(math.sin(phi[i])) > 1.0e-9:
                theta[i,j] = xy2theta(axes,points[totalParts,:],phi[i])
                # print "theta:",theta[i,j]
            totalParts = totalParts + 1

    # assert(totalParts < roughParts)
    return totalParts

def dab(point,h,phi):
    tmp = h / norm(point,[0,0,0])
    if tmp > 1.0:
        angle = math.pi / 2
    else:
        angle = math.asin(tmp)
    tmp = h / (norm(point,[0,0,0]) * math.sin(phi))
    if tmp > 1.0:
        angle2 = math.pi
    else:
        angle2 = math.asin(tmp)
    return angle, angle2

def xyz2ft(axes,point):
    phi = math.acos(point[1] / axes[1])
    theta = xy2theta(axes,point,phi)
    return phi,theta

def xy2theta(axes,point,phi):
    tmp = (point[2] / (axes[2] * math.sin(phi)))
    if tmp > 1.0:
        tmp = 1.0
    if tmp < -1.0:
        tmp = -1.0
    # print "theta:", math.asin(tmp)

    if point[2] > 0.0 and point[0] > 0.0:
        theta = math.asin(tmp)
    if (point[2] > 0.0 and point[0] <= 0.0):
        theta = math.pi - math.asin(tmp)
    if (point[2] <= 0.0 and point[0] <= 0.0):
        theta = -math.asin(tmp) + math.pi
    if (point[2] <= 0.0 and point[0] > 0.0):
        theta = math.asin(tmp) + 2 * math.pi
    if theta >= 2 * math.pi:
        theta = theta - 2 * math.pi
    return theta
    
def ell(axisMin,axisMax,outSin,outCos,numPoints,outFi,isone):
    """
    Вычисление точек эллипса, делящих его на почти равные части.
    """
    eccent = axisMax/axisMin
    if isone==1:
        # здесь случай половины эллипса, есть симметрия
        # кстати, если numPoints четное, то addon = 0
        # этот случай нужен, чтобы не дублировать эллипсоид:
        # сначала разбивается целый эллипс, а затем для каждой точки
        # строится половинка эллипса - в итоге получаем правильный проход эллипсоида.
        rn = 0.5*numPoints
        n  = int(rn)
        # print "n=",n
        addon = eccent*(rn - n)
    else:
        # здесь случай целого эллипса, добавка h (высота?) равна нулю.
        n  = numPoints
        rn = numPoints*1.
        addon  = 0.

    # Делим на rn частей
    outFi[0] = 0.
    for i in range(0,n,1):
        outFi[i+1] = outFi[i] + 1.+ (eccent - 1.)*abs((2.*(i+1)-1.)/rn-1.)
        
    coef = pi/(outFi[n] + addon)
    
    outFi [1:n+1] = outFi[1:n+1]*coef
    outCos[1:n+1] = axisMax*cos(outFi[1:n+1])
    outSin[1:n+1] = axisMin*sin(outFi[1:n+1])
        
    outCos[0] = axisMax
    outSin[0] = 0.

    # в случае половины, дополняем остальные значения по формулам:
    if isone==1:
        j = n
        for i in range(numPoints - n,numPoints,1):
            outFi[i] = 2.*pi - outFi[j]
            outCos[i] = outCos[j]
            outSin[i] = -outSin[j]
            j = j - 1
    return 0

def dpair(xt,i,j):
    return dot(xt[i,:] - xt[j,:],xt[i,:] - xt[j,:])

def point(kt,xt,ktmax,a,numpoints):
    n2    = int(0.5+math.sqrt(numpoints))
    m2    = 5 * n2
    m13   = 7 * n2
    # print "a=",a
    # TODO откуда эта формула для n2? 
    # print "numpoints = ", numpoints
    n     = zeros(m2,integer)
    x2    = zeros(m2)
    x     = zeros(m2)
    x1    = zeros((m13,m2))
    x3    = zeros((m13,m2))
    xx1   = zeros(m13)
    xx3   = zeros(m13)
    fi    = zeros((m13,m2))
    f     = zeros(m2)
    ffi   = zeros(m2)
    n[0]  = 1
    n[n2] = 1
    # Делим на  части основной эллипс
    # используем только x2
    ell(a[0],a[1],x,x2,n2,f,0)
    
    # print "n2",n2
    # print "x2[0]",x2[0]
    for i in range(1,n2,1):
        aa = math.sqrt(1. - (x2[i]/a[1])**2)
        # print "aa =",aa
        aa3 = a[2]*aa
        aa1 = a[0]*aa
        # print "nn:",n2,aa,a[0],a[2],a[1],ep2p(1.-(a[2]/a[0])**2),ep2p(1.-(a[0]/a[1])**2),(0.5+2.*n2*aa*a[0]*ep2p(1.-(a[2]/a[0])**2)/(a[1]*ep2p(1.-(a[0]/a[1])**2)))
        nn = int(0.5+2.*n2*aa*a[0]*ep2p(1.-(a[2]/a[0])**2)/(a[1]*ep2p(1.-(a[0]/a[1])**2)))
        # print "nn=",nn

        # Делим на части уже с добавками.
        ell(aa3,aa1,xx3,xx1,nn,ffi,1)
        
        # print "xx3=",xx3
        # print "xx1[...]=",xx1[0],xx1[1],xx1[2],xx1[3]
        n[i]    = nn
        x1[0,i] = aa1
        x1[1:nn,i] = xx1[1:nn]
        x3[1:nn,i] = xx3[1:nn]
        fi[1:nn,i] = ffi[1:nn]
    kt = 0
    
    for i in range(0,n2+1,1):
        nn = n[i]
        # print "nn=",nn
        # print "x1[..]",x1[0,i],x1[1,i],x1[2,i],x1[3,i]
        if nn == 0:
            # print "bingo"
            continue
        for j in range(0,nn,1):
            xt[kt,0] = x1[j,i]
            xt[kt,1] = x2[i]
            xt[kt,2] = x3[j,i]
            kt = kt + 1
    
    # print "xt[...]=",xt[0,0],xt[1,0],xt[2,0],xt[3,0]    
    # print "kt = ",kt
    return kt

def myfilt(x,h):
    if (x < h):
        return 1
    else:
        return 0

def checkH(i,j,h,c):
    return ((i == j) or (c < h))

# TODO сделать единообразно
def FilterElements(KT,h,NOKR,axes,pointsEllipsoide,condition):
    # C	ОТЫСКАНИЕ НОСИТЕЛЕЙ КАЖДОЙ ШАПОЧКИ И НОСИТЕЛЕЙ ШАПОЧЕК,
    # C	ИМЕЮЩИХ ОБЩИЕ ТОЧКИ С НОСИТЕЛЕМ ДАННОЙ ШАПОЧКИ
    # tmp = zeros(KT)
    # maximums = zeros(KT)
    # minumums = zeros(KT)    
    lst = []
    for i in range(0,KT,1):
        lst.append([])
        for j in range(0,KT,1):
            candidate = dpair(pointsEllipsoide,i,j)
            # tmp[j] = candidate
            if condition(i,j,h,candidate):
                lst[i].append(j)
        # maximums[i] = tmp.max()
        # minimums[i] = tmp.min()
    lenghts = map(lambda x:len(x),lst)
    # maxim = maximums.max()
    # minim = minimums.min()    
    KOKRM = array(lenghts).max() # get maximum lenghts
    tmp = zeros((KT,KOKRM),int,order = 'fortran') # allocate array
    for i in range(0,KT,1):
        l = len(lst[i])
        tmp[i,0:l] = lst[i][0:l]
        NOKR[i,0:l] = tmp[i,0:l]

def GetPointsInterpolation(distanceMax,numberPointsMax,numberPointsEllipsoide,pointsEllipsoide,INTER):
    # C	ВЫЧИСЛЕНИЕ НОМЕРОВ ТОЧЕК, ПО КОТОРЫМ БУДЕМ ВЕСТИ ИНТЕРПОЛЯЦИЮ    
    M = numberPointsMax
    interpolationValues = zeros(M)
    interpolationIndex = zeros(M)    
    for kx in range(0,numberPointsEllipsoide,1):
        interpolationValues[0:M] = distanceMax
        for k in range(0,numberPointsEllipsoide,1):
            if k == kx:
                continue
            candidate = dpair(pointsEllipsoide,k,kx)
            for i in range(0,M,1):
                if candidate < interpolationValues[i]:
                    if i == (M - 1):
                        interpolationValues[i] = candidate
                        interpolationIndex[i] = k
                    else:
                        interpolationValues[i + 1:M - 1] = interpolationValues[i:M - 2]
                        interpolationIndex[i + 1:M - 1] = interpolationIndex[i:M - 2]
            INTER[kx,1:M + 1] = interpolationIndex[0:M]
            INTER[kx,0] = kx

def PrepareStroke(numberPointsEllipsoide,KTO,numberPointsMax,NTSHA,INTER,NVECT,NVECH):
    tmpVector = zeros(3)
    for i in range(0,numberPointsEllipsoide,1):
        index = list(NTSHA[i,:]).index(-1) # get first index of element -1 in NTSHA
        lengthVectorSquare = 0.
        for j in range(0,3,1):
            tmpVector[j] = 0
            for k in range(0,KTO,1):
                
                # TODO сделать эти условия более читабельными при помощи логических переменных
                if (index < numberPointsMax):
                    if (k > numberPointsMax):
                        break
                    candidate = INTER[i,k]
                else:
                    candidate = NTSHA[i,k]
                    
                if candidate == -1:
                    break
                # получается, что частично зацепляются и кандидаты из NTSHA
                tmpVector[j] = tmpVector[j] + NVECT[candidate,j]
            lengthVectorSquare = lengthVectorSquare + tmpVector[j] * tmpVector[j]

        if lengthVectorSquare <> 0.:
            x = 1./ math.sqrt(lengthVectorSquare)
            
        NVECH[i,0:3] = tmpVector[0:3] * x

def DistanceMax(KT,pointsEllipsoide):
    # C	ВЫЧИСЛЕНИЕ МАКСИМАЛЬНОГО РАССТОЯНИЯ МЕЖДУ ТОЧКАМИ ПОВ-ТИ    
    candidates = zeros(KT)
    max_candidates = zeros(KT)
    # Здесь показана краткая запись поиска PM. MAXLOC - для поиска индекса максимального элемента.
    for kx in range(0,KT,1):
        for k in range(0,KT,1):
            candidates[k] = dpair(pointsEllipsoide,kx,k)
        max_candidates[kx] = candidates.max()
        # max_index_j[kx] = candidates.index(max_candidates[kx])
    PM = max_candidates.max()
    # max_index_i = max_candidates.index(PM)
    return PM

# TODO провести рефакторинг этих ужасных функций
# TODO общий кусок с init_stroke (prepareStroke)
def shiftValue(value,num,vn,i,ind,KTO,NTSHA,MINKV,INTER,mult,NVECT):
    ivalue = value
    inum = num
    ivn = vn
    for k in range(0,KTO,1):
        # см. PrepareStroke
        if (ind < MINKV):
            if (k > MINKV):
                break
            candidate = INTER[i,k]
        else:
            candidate = NTSHA[i,k]
            
        if candidate == (-1):
            break
        ivn = ivn + 1
            
        VS = 0.
        for j in range(0,3,1):
            VS = VS + mult[j] * NVECT[candidate,j]

        # VS = dot(NVECH[i,:],NVECT[candidate,:])
            
        if VS < ivalue:
            ivalue = VS
            inum = candidate
            
    return ivalue,inum,ivn


def NormalVectorStroke(normalVectors,pointsEllipsoide,numberPointsEllipsoide,numbersCloseEnvirons,normal_vectors_stroke):
    """
       this function computes normal_vectors_stroke (n')
    """
    max_neighbors = NeighborsMax()
    lengthMinimums = LengthMinimumsMax() - 1

    PM = DistanceMax(numberPointsEllipsoide,pointsEllipsoide)

    # Найти набор точек, по которым ведется интерполяция
    points_interpolation  = zeros((numberPointsEllipsoide,LengthMinimumsMax()),int,order = 'Fortran')
    points_interpolation[0:numberPointsEllipsoide,0:LengthMinimumsMax()] = -1
    length = lengthMinimums - 1
    GetPointsInterpolation(PM,length,numberPointsEllipsoide,pointsEllipsoide,points_interpolation)

    tmpVector = zeros(3)        
    normal_vectors_stroke[0:numberPointsEllipsoide,0:3]=0.

    # задать начальные значения для n'
    PrepareStroke(numberPointsEllipsoide,max_neighbors,lengthMinimums,numbersCloseEnvirons,points_interpolation,normalVectors,normal_vectors_stroke)
    
    for i in range(0,numberPointsEllipsoide,1):
        ind = list(numbersCloseEnvirons[i,:]).index(-1)
        candidate1,index_candidate1,number_candidate1 = shiftValue(1.0,0,0.,i,ind,max_neighbors,numbersCloseEnvirons,lengthMinimums,points_interpolation,normal_vectors_stroke[i,:],normalVectors)

        tmpVector[0:3] = normal_vectors_stroke[i,0:3]

        count = 0
        while (count < 100):
            count = count + 1
            candidate2,index_candidate2,number_candidate2 = shiftValue(1.,0,0.,i,ind,max_neighbors,numbersCloseEnvirons,lengthMinimums,points_interpolation,tmpVector,normalVectors)
            if candidate2 - candidate1 >=- 1.0e-17:
                candidate1 = candidate2
                if number_candidate2 <> 0.:
                    number_candidate2 = 1./ number_candidate2

                tmp = 0.
                for j in range(0,3,1):
                    tmpVector[j] = tmpVector[j] + number_candidate2 * normalVectors[index_candidate2,j]
                    tmp = tmp + tmpVector[j] * tmpVector[j]
                if tmp <> 0.:
                    tmp = 1./ math.sqrt(tmp)
                tmpVector[0:3] = tmp * tmpVector[0:3]

        normal_vectors_stroke[i,0:3] = tmpVector[0:3]

        if candidate1 < 0.:
            print "ОКРЕСТНОСТЬ ТОЧКИ",i,"НЕЛЬЗЯ ОДНОЗНАЧНО СПРОЕКТИРОВАТЬ НА ВЫБРАННУЮ ПЛОСКОСТЬ, ВОЗМОЖНО, ЕЕ СЛЕДУЕТ УМЕНЬШИТЬ"
            
    return


# TODO Внимание! Даже изменив здесь 1./(...) на просто X[0:3] / (...)
# получаем существенное расхождение в знаках, например в albet.
def NormalVector(pointsEllipsoide,axesReverse,numberPointsEllipsoide,normalVectors):
    """Compute normal vector for each point from ellipsoid sampling pointsEllipsoide"""
    normalVectors[0:numberPointsEllipsoide,0:3] = 0.
    X = zeros(3)
    for i in range(0,numberPointsEllipsoide,1):
        X[0:3] = pointsEllipsoide[i,0:3] * (axesReverse[0:3]) * (axesReverse[0:3])
        normXReverse = 1./ math.sqrt(X[0]*X[0]+X[1]*X[1]+X[2]*X[2])
        normalVectors[i,0:3] = X[0:3] * normXReverse
    return

def nvecc1(ALPHA,BETA,RHSHA,axes,aobr,xt,NVECT,RSHAP,NOKR,MINKM,KTO,KT,KOKRM,numpoints,NVECH):
    # compute normal vectors (n)
    NormalVector(xt,aobr,KT,NVECT)
    
    # neighbors(NVECT,xt,axes,KT,numpoints,NVECH,NOKR)
    h_2 = (get_h(axes,PartsOneDimension(numpoints),RadiusHat())) ** 2

    # get NOKR numbers_environs (neighbors)
    NOKR[0:KT,0:KT] = -1
    FilterElements(KT,4 * h_2,NOKR,axes,xt,checkH)

    # get numbersCloseEnvirons (close neighbors)
    numbersCloseEnvirons = zeros((KT,NeighborsMax()),int,order = 'Fortran')
    numbersCloseEnvirons[0:KT,0:NeighborsMax()] = -1
    FilterElements(KT,  h_2,numbersCloseEnvirons,axes,xt,checkH)

    # compute normal vectors stroke (n')
    NormalVectorStroke(NVECT,xt,KT,numbersCloseEnvirons,NVECH)

    # compute matrix α for change coordinate system from 0x_1x_2x_3 to 0y_1y_2y_3
    # also auxiliary matrix BETA = α^(-1)
    albet(NVECH,ALPHA,BETA,KT)
    # nvecc(ALPHA,BETA,RHSHA,axes,aobr,xt,NVECT,RSHAP,NOKR,MINKM,KTO,KT,KOKRM,numpoints)
    return

def delta(i,j):
    if i == j:
        return 1
    else:
        return 0

# скорее, всего здесь реализуются формулы (МММП, с. 66)
# проекции направляющего вектора e_k, удовлетворяющего условию:
# | n'_j * e_k | = min( | n'_j * e_m | ,m = 1..3)
# подвижной ковариантный базис:
# e_j1 = (e_k - n'_j(n'_j * e_k)) /|(e_k - n'_j(n'_j * e_k))| 
# e_j2 = n'_j x e_j1
# e_j3 = n'_j
# обозначения:
# α^i_jl = (e_i * e_jl)
# β^i_jl = α^i_jl / a_i

def albet(NVECH,ALPHA,BETA,KT):
    
    IH = zeros((KT,3,3),order = 'Fortran')
    tmpVector = zeros(3)
    
    EPS = array([0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,1.00000000000000000,
                 0.0000000000000000,-1.00000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,-1.00000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,1.00000000000000000,0.0000000000000000,
                 -1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000])
    
    EPS.shape = (3,3,3)
    # print "EPS",EPS[0,1,2],EPS[0,2,1],EPS[1,0,2],EPS[1,2,0],EPS[2,0,1],EPS[2,1,0]
    
    ALPHA[0:KT,0:3,0:3]=0.
    BETA[0:KT,0:3,0:3]=0.
    IH[0:KT,0:3,0:3]=0.
    
    # C	НАХОДИМ ПЕРВЫЙ НАПРАВЛЯЮЩИЙ ВЕКТОР ДЛЯ ПАРАМЕТРИЗАЦИИ
    absNVECH = zeros(3)
    for i in range(0,KT,1):

        # Какая координата вектора n' имеет минимальное значение?
        absNVECH[0:3] = abs(NVECH[i,0:3])
        VS = min(absNVECH) # minval in Fortran
        indexMinValue = list(absNVECH).index(VS) # minloc in Fortran. ! первый попавшийся!!!

        # DONE из-за того, что для функции delta нельзя воспользоваться синтаксисом
        # delta(0:3,i) вынужден ввести дополнительную переменную tmpVector
        # for k in range (0,3,1): tmpVector[k] = delta(k,indexMinValue)
        # РЕШЕНИЕ: использовать map(f,[0,1,2]) вместо цикла.
        IH[i,0:3,0] = -NVECH[i,0:3] * NVECH[i,indexMinValue] + map(lambda j:delta(j,indexMinValue),[0,1,2])

        # здесь для функции sum() также требуется вектор
        normIHreverse = 1./ math.sqrt(dot(IH[i,:,0],IH[i,:,0]))
        IH[i,0:3,0] = IH[i,0:3,0] * normIHreverse

    # ТРЕТИЙ НАПРАВЛЯЮЩИЙ ВЕКТОР равен просто n'
    IH[0:KT,0:3,2] = NVECH[0:KT,0:3]

    # forall (i = 1:3,j = 1:3,l = 1:3)...

    # C	НАХОДИМ ВТОРОЙ НАПРАВЛЯЮЩИЙ ВЕКТОР ДЛЯ ПАРАМЕТРИЗАЦИИ
    # Он использует значения первого и третьего вектора.
    for k in range(0,KT,1):
        for i in range(0,3,1):
            VS = 0.
            for j in range(0,3,1):
                for l in range(0,3,1):
                    VS = VS + EPS[i,j,l] * IH[k,j,2] * IH[k,l,0]
            IH[k,i,1] = VS

    print "IH",IH[:,:,0],IH[:,:,1],IH[:,:,2]

    # ALPHA это и есть направляющие вектора для параметризации, т.е.
    # каждой pointsEllipsoide[:,:] соответствует локальная система координат (ej1, ej2, ej3 = n')
    ALPHA[0:KT,0:3,0:3]=IH[0:KT,0:3,0:3]

    # похоже, что β = α^(-1)
    for k in range(0,KT,1):
        DALPH = 0.
        for i in range(0,3,1):
            for j in range(0,3,1):
                for l in range(0,3,1):
                    DALPH = DALPH + EPS[i,j,l] * ALPHA[k,i,0] * ALPHA[k,j,1] * ALPHA[k,l,2]
    
        DOBRA = 1./DALPH
        VS = 1.
        for i in range(0,3,1):
            I1 = delta(i,0)
            I2 = 2 - delta(i,2)
            for j in range(0,3,1):
                J1 = delta(j,0)
                J2 = 2 - delta(j,2)
    
                BETA[k,j,i] = VS * DOBRA * (ALPHA[k,I1,J1] * ALPHA[k,I2,J2] - ALPHA[k,I1,J2] * ALPHA[k,I2,J1])
                VS = -VS
    
    return

def norm(x,y):
    return math.sqrt(dot(x[:] - y[:],x[:] - y[:]))

def xdelta(expr):
    if expr:
        return 1
    else:
        return 0

def FiStroke(x,x_m,h):
    r_m = norm(x,x_m)
    return xdelta(r_m < h) * (1 - (r_m / h) ** 2) ** 3

def Fi(m,points,x,NOKR,KOKRM,h):
    pass

def dFi(m):
    pass
    
# Attention! In this function fhloc the value BETA is different from BETA in albet
# point[0:2] - 2d point for computing y_j3 = f_j3(y_j1,y_j2)
# TODO numberPointsEllipsoide not used in this function!
def fhloc(numberPoint,alpha,axesReverse,coordPoint2d,leviChevita,dfdy):
    """C	ЛОКАЛЬНАЯ ПАРАМЕТРИЗАЦИЯ ПОВЕРХНОСТИ В КООРДИНАТАХ IH1,IH2
C	ВЫЧИСЛЕНИЕ ПРОИЗВОДНОЙ ОТ f ПО К-КООРДИНАТЕ
"""

    sumEb2b = zeros(2)    
    b2b = zeros(2)
    beta = zeros((3,3),order = 'Fortran') # not like beta in albet!
    betaPoint3d = zeros(3)

    for i in range(0,3,1):
        beta[i,0:3] = alpha[numberPoint,i,0:3] * axesReverse[i] # β = α^i_jl / a_i
        betaPoint3d[i] = dot(beta[i,0:2], coordPoint2d[0:2]) # = β x

    # похоже, что здесь составляется f_j3
    # Σ (i = 1..3)
    C = 0.
    A = 0.
    sumF2 = 0.
    dfdy[0:2] = 0.
    for i in range(0,3,1):
        F = 0.
        sumEb2b[0:2] = 0.
        for l in range(0,3,1):
            for m in range(0,3,1):
                # sumEb2b = Σ ε * β * β
                sumEb2b[0:2] = sumEb2b[0:2] + leviChevita[i,l,m] * beta[l,2] * beta[m,0:2]
                # F = Σ ε * β * β * x
                F = F + leviChevita[i,l,m] * beta[l,2] * betaPoint3d[m]

        # сложная формула для df_j3 / dy_jk
        dfdy[0:2]=dfdy[0:2]+sumEb2b[0:2]*F # = Σ ε * β * β (Σ ε * β * β * x)
        b2b[0:2]=b2b[0:2]+beta[i,2]*beta[i,0:2] # = Σ ββ

        C=C+beta[i,2]*betaPoint3d[i] # Σ β (Σ β * x)
        A=A+beta[i,2]*beta[i,2] # = A_j
        sumF2=sumF2+F*F # = F^2

    B2 = A - sumF2 # = (A_j - F^2)
    isB2negativeORzero = 0
    if B2 <= 0.:
        # if F^2 <= 0 then f = 0. and dfdy = 0. why?
        # Потому, что в дальнейшем происходит деление на B2, а т.к. B2 - сумма квадратов, то "<=0" равносильно "=0".
        isB2negativeORzero = 1
        # TODO next line wrong? 
        f = 0.
        dfdy = 0.
        return f,isB2negativeORzero
    else:
        B = math.sqrt(B2) # = sqrt(A_j - F^2) = B
        f = ( -C + B) / A # = ( B - ? ) / A_j
        dfdy[0:2]=-(b2b[0:2]+dfdy[0:2] / B) / A
    return f,isB2negativeORzero

def PhiStroke(r,h):
    return (1 - (r / h) ** 2) ** 3

def DPhiStroke(dr,r,h):
    return -6 * ((1 - (r / h) ** 2) ** 2) * (dr / h ** 2)

# KOKRM may compute from NOKR
def sumPhi(NOKR,KOKRM,numberPoint,pointsEllipsoide,point,RHSH2,ALPVL):
    pass

# Используется только pointsEllipsoide[numberPoint,:] i.e.
# we may use one parameter pointsEllipsoide[numberPoint,:] - point[:] instead three: numberPoint, pointsEllipsoide and point
# instead BETNY and ALPNY we may use concrete function PhiStroke, where
# substitute x = RXY = dot(pointsEllipsoide[numberPoint,:] - point[:],pointsEllipsoide[numberPoint,:] - point[:])
# for computing Σφ in points NOKR we may using PhiStroke
# Зачем ALPVL в finfi? 
def finfi(numberPoint,pointsEllipsoide,point,numbersCloseEnvirons,KOKRM,metricForm,DFINY,h):
    """C  	*ВЫЧЕСЛЕНИЕ ФУНКЦИИЙ ДАЮЩИХ РАЗБИЕНИЕ ЕДИНИЦЫ 
C  	*ВЫЧЕСЛЕНИЕ ПРОИЗВОДНЫХ ОТ ФИНИТНЫХ ФУНКЦИЙ ДАЮЩИХ РАЗБИЕНИЕ ЕДИНИЦЫ"""

    sumDphi = zeros(2)
    DR = zeros(2)
    dPhi = zeros(2)
    curDphi = zeros(2)

    RHOBR=1./h
    RHSH2=h*h
    
    DFINY[0:2] = 0.
    curPhi = 0.
    sumPhi = 0.
    
    # RXY = 0.
    # for i in range(0,3,1):
    #     VS = pointsEllipsoide[numberPoint,i] - point[i]
    #     RXY = RXY + VS * VS
    RXY = dot(pointsEllipsoide[numberPoint,:] - point[:],
              pointsEllipsoide[numberPoint,:] - point[:])

    if RXY >= RHSH2:
        FINYO = 0.
        DFINY[0:2] = 0.
        return FINYO
    else:
        # cycle on all points from environs
        for nr in range(0,KOKRM,1):
            currentNumber = numbersCloseEnvirons[numberPoint,nr]
            
            # это низкоуровневое знание об устройстве numbersCloseEnvirons
            if currentNumber == (-1):
                break

            # RXY = 0.
            # for i in range(0,3,1):
            #     VS = pointsEllipsoide[currentNumber,i] - point[i]
            #     RXY = RXY + VS * VS
            RXY = dot(pointsEllipsoide[currentNumber,:] - point[:],
                      pointsEllipsoide[currentNumber,:] - point[:])

            # is | x - x_m |^2 < h^2 ? 
            if RXY >= RHSH2:
                continue

            RXY = math.sqrt(RXY)
            VS1 = PhiStroke(RXY,(1. / RHOBR))

            # if delta = 0 then curPhi = curPhi_previous 
            curPhi = (VS1 - curPhi)* delta(currentNumber, numberPoint) + curPhi
            sumPhi = sumPhi + VS1
            
            DR[0:2] = 0.
            for i in range(0,3,1):
                DR[0:2] = DR[0:2] - (pointsEllipsoide[currentNumber,i] - point[i]) * metricForm[i,0:2]
                
            # VS0 = -(ALPNY + 1.) * BETNY * RHOBR * RHOBR * RBET2 * VS
            # dPhi[0:2] = VS0 * DR[0:2]
            
            dPhi[0] = DPhiStroke(DR[0],RXY,(1./ RHOBR))
            dPhi[1] = DPhiStroke(DR[1],RXY,(1./ RHOBR))            
            
            # if currentNumber == numberPoint:
            #     curDphi[0:2] = dPhi[0:2]
            
            curDphi[0:2] = (dPhi[0:2] - curDphi[0:2]) * delta(currentNumber, numberPoint) + curDphi[0:2]
            sumDphi[0:2] = sumDphi[0:2] + dPhi[0:2]

    # here curPhi = current VS1
    # here curDphi[0:2] = current dPhi[0:2]
    if sumPhi <= 0.:
        FINYO = 0.
        DFINY[0] = 0.
        DFINY[1] = 0.
        return FINYO

    FINYO=curPhi*(1./sumPhi)

    # хитрая формула для производной.
    # возможно, DFINY вычисляется не верно, т.к. не тестировалось.
    DFINY[0:2]=((sumPhi-curPhi)*curDphi[0:2]-curPhi*(sumDphi[0:2]-curDphi[0:2]))*(1./sumPhi) ** 2
    return FINYO

def ComputeX(ky,ALPHA,ZY,X):
    X[0:3] = 0.
    for j in range(0,2,1):
        X[0:3] = X[0:3] + ALPHA[ky,0:3,j] * ZY[j]
    X[0:3] = X[0:3] + ALPHA[ky,0:3,2] * ZY[2]

def ComputeMetricForm(ky,ALPHA,dfdy,metricForm):
    for j in range(0,2,1):
        metricForm[0:3,j] = ALPHA[ky,0:3,j] + ALPHA[ky,0:3,2] * dfdy[j]

# TODO в этой функции смешаны многие, ортогональные по смыслу, сущности, например:
# переход от координат y' к y, квадратуры и замена переменных x -> (1 - x)^(0.5)
# понимая, что делают функции fhloc и finfi выяснить порядок выполнения integ
def integ(barPhi,DINTE1,numbersCloseEnvirons,h,pointsEllipsoide,BETA,ALPHA,axesReverse,orderQuadratureRho,weights,centres,IELL,KOKRM,KT):

    EPS = array([0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,1.00000000000000000,
                 0.0000000000000000,-1.00000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,-1.00000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,1.00000000000000000,0.0000000000000000,
                 -1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000])
    EPS.shape = (3,3,3)
    
    PI=3.14159265358979324

    # Непонятно, зачем этот блок. Никакие значения, используемые далее, здесь не вычисляются.
    # for ky in range(0,KT,1):
    #     for j in range(0,3,1): Z[j] = dot(BETA[ky,j,:],pointsEllipsoide[ky,:]) # z_j = α^(-1)x_j

    #     f,INF = fhloc(ky,ALPHA,axesReverse,Z,EPS,dfdy)

    #     # TODO что такое цикл по j = 0,1 - две неизвестных
    #     # скорее всего, это как раз и есть y_j3 = f_j3(y_jk), k = 1,2
    #     # Здесь начинаем наполнять вектор Y[0:3]
    #     if INF == 0:
    #         for j in range(0,2,1):
    #             Y[0:3] = ALPHA[ky,0:3,j] + ALPHA[ky,0:3,2] * dfdy[j]
    #             normY = math.sqrt(dot(Y[:],Y[:]))
    #             Y[0:3] = Y[0:3] / normY

#######################################################                
    
    orderQuadratureAngle=orderQuadratureRho * 4
    
    rho = zeros(orderQuadratureRho) # centres - это x_i - оптимальные узлы 
    BREG = zeros(orderQuadratureRho) # weights - это C_i - оптимальные веса
    angle = zeros((2,orderQuadratureAngle),order = 'Fortran')
    
    deltaAngle=2.*PI/orderQuadratureAngle
    for i in range(0,orderQuadratureAngle,1): # цикл по переменной от 0 до 2 * Pi
        angle[0,i] = math.cos(deltaAngle * (i + 1))  #  cos(α)
        angle[1,i] = math.sin(deltaAngle * (i + 1))  #  sin(α)
    
    # обратная замена? x -> (1 - x)^(0.5) или x -> 1 - x^2
    # rho идет в аргумент вычисления y'
    # Extract the values of rho from array of centres
    rho[0:orderQuadratureRho] = map(lambda x:math.sqrt(1.- x),
                                  centres[0:orderQuadratureRho]) # sqrt(1 - x_i) узлы
    BREG[0:orderQuadratureRho] = 0.5 * deltaAngle * (h**2) * weights[0:orderQuadratureRho] / (centres[0:orderQuadratureRho] * centres[0:orderQuadratureRho])
    # ( Pi / N) * i * h^2 * C_i / (x_i)^2 - веса

    X = zeros(3)
    metricForm = zeros((3,2),order = 'Fortran')
    centerWeightPhi = zeros((KT,3),order = 'Fortran')
    ZY = zeros(3)
    dfdy = zeros(2)
    Z = zeros(3)
    for ky in range(0,KT,1):
        # Compute Z
        # identical value for each combination of counterRho and counterAngle
        for j in range(0,3,1): Z[j] = dot(BETA[ky,j,:], pointsEllipsoide[ky,:]) # z_j = α^(-1)x_j
        # Берем точку эллипсоида pointsEllipsoide[ky,:] (точку сетки) в системе координат 0x_1x_2x_3
        # и начинаем преобразовывать её в систему 0y_1y_2y_3

        barPhi[ky] = 0.
        centerWeightPhi[ky,0:3] = 0.
        for counterRho in range(0,orderQuadratureRho,1): # цикл по переменной от 0 до 1
            for counterAngle in range(0,orderQuadratureAngle,1): # цикл по переменной от 0 до 2 * Pi
                # Compute ZY
                # Compute dfdy
                ########################################################
                # y_jm = angle * rho - переменная, по которой ведется интегрирование
                # (y_jm + z_jm) m = 1..2
                # вычисляем значение ZY в системе 0y_1y_2y_3
                ZY[0:2] = Z[0:2] + h * angle[0:2,counterAngle] * rho[counterRho] # делаем ZY из Z (сетки) и комбинации шага по Pi и оптимальных узлов
                # ZY[0] = Σβx + y_1 = Σβx + ρh cos(α) = Σβx + h(1 - z)^(0.5) cos(α)
                # ZY[1] = Σβx + y_2 = Σβx + ρh sin(α) = Σβx + h(1 - z)^(0.5) sin(α)

                f,INF = fhloc(ky,ALPHA,axesReverse,ZY,EPS,dfdy)
                # параметризация в локальных координатах f_j3(y'_j)
                # получаем из ZY - f и dfdy
                
                ZY[2] = f
                
                if INF <> 0:
                    break


                # Compute X
                # Compute metricForm
                # Compute Phi
                # Compute Tensor
                #######################################################
                X[0:3] = 0.
                for j in range(0,2,1):
                    metricForm[0:3,j] = ALPHA[ky,0:3,j] + ALPHA[ky,0:3,2] * dfdy[j] # составляем из ALPHA и dfdy
                    # матрица перехода от глобальных координат к локальным?
                    # Если ZY в системе координат (ej), то здесь умножение на орты.
                    # здесь продолжаем наполнять вектор X[0:3]
                    X[0:3] = X[0:3] + ALPHA[ky,0:3,j] * ZY[j] # = x_i = Σ(m = 1..2)β(y_jm + z_jm)
                    # j = 0,1 -  сумма по 2м
                    # Σα(y + Σβx)

                # X и есть точка y'
                # y'_i = x_i + [α(:,:,2) * f_j3](m = 3) = Σ(m = 1..3)β(y_jm + z_jm)
                X[0:3] = X[0:3] + ALPHA[ky,0:3,2] * ZY[2] # комбинация из ALPHA, ZY и f
                # это значение в системе 0x_1x_2x_3
                # y' = Σα(y + Σβx) + α(fhloc(y + Σβx))
                # аргумент φ.
                #######################################################
                
                DFINY = zeros(2)
                FINYO = finfi(ky,pointsEllipsoide,X,numbersCloseEnvirons,KOKRM,metricForm,DFINY,h)
                # FINYO = φ'(y'), y' in D_j. это и есть Φ'(Y) = Φ'(z_counterRho,2 * Pi * counterAngle / orderQuadratureAngle) уже от двух линейных переменных
                if IELL == 0:
                    TENMET=math.sqrt((metricForm[1,0]*metricForm[2,1]-metricForm[1,1]*metricForm[2,0])**2+(metricForm[2,0]*metricForm[0,1]-metricForm[2,1]*metricForm[0,0])** 2+(metricForm[0,0]*metricForm[1,1]-metricForm[0,1]*metricForm[1,0])**2)
                    # J(y*) = 1 (т.е. эллипсоид). 
                    # q(y') -  дискриминант (тензор? ) метрической формы поверхности в системе (y')  - составляется из metricForm
                    # φ' -  выражение φ в локальных координатах, связанных с узловой точкой x

                barPhi[ky] = barPhi[ky] + BREG[counterRho] * TENMET * FINYO
                centerWeightPhi[ky,0:3] = centerWeightPhi[ky,0:3] + BREG[counterRho] * TENMET * FINYO * X[0:3]
                # φ = Σ (веса) * (метрический тензор) * (функция разбиения единицы) = Σ (веса) * q(y') * φ(y')

    DINT = 0.
    for i in range(0,KT,1):
        DINTE1[i,:] = pointsEllipsoide[i,:]
            # DINTE1[i,:] = centerWeightPhi[i,:] / barPhi[i]
        DINT = DINT + barPhi[i]

    DINTT = DINT / KT
    return

def nvecc(ALPHA,BETA,RHSHA,A,aobr,xt,NVECT,RSHAP,NOKR,MINKM,KTO,KT,KOKRM,numpoints):
    # NVECT = zeros((KT,3),order = 'Fortran')
    # ALPHA = zeros((KT,3,3),order = 'Fortran')
    # BETA = zeros((KT,3,3),order = 'Fortran')
    # NOKR = zeros((KT,KOKRM),int,order = 'Fortran')
    
    NTSHA = zeros((KT,KTO),int,order = 'Fortran')
    NVECH = zeros((KT,3),order = 'Fortran')
    IH1 = zeros((KT,3),order = 'Fortran')
    IH2 = zeros((KT,3),order = 'Fortran')
    IH3 = zeros((KT,3),order = 'Fortran')
    VSPOM = zeros(3)
    ADOP = zeros((2,2),order = 'Fortran')
    # EPS = zeros((3,3,3),order = 'Fortran')
    INTER = zeros((KT,MINKM),int,order = 'Fortran')
    INTER[0:KT,0:MINKM] = -1
    IMIN = zeros(10,int,order = 'Fortran')
    PMIN = zeros(10)
    XA = zeros(3)
    PX = zeros(3)
    
    EPS = array([0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,1.00000000000000000,
                 0.0000000000000000,-1.00000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,-1.00000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,1.00000000000000000,0.0000000000000000,
                 -1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000])
    
    EPS.shape = (3,3,3)
    # print "EPS",EPS[0,1,2],EPS[0,2,1],EPS[1,0,2],EPS[1,2,0],EPS[2,0,1],EPS[2,1,0]
    NPOYS = int(0.5+math.sqrt(numpoints))
    
    MINKV = 4
    HPOYS = 2.*A[1]*ep2p(1.-(A[0]/A[1])**2)/NPOYS
    
    RHSHA = RSHAP*HPOYS
    RHSH2 = RHSHA*RHSHA	
    PMAX = 0.
    PMINN = A[1]*A[1]
    
    NTSHA[0:KT,0:KTO] = -1
    NOKR[0:KT,0:KOKRM] = -1

    JM = 0
    IMINT = 0
    JMIN = 0
    
    for i in range(0,KT,1):
        NR = -1
        NR1 = -1
        PM = A[1]*A[1]
        P2 = PM
        for j in range(0,KT,1):
            if i <> j:
                PX[0:3] = xt[i,0:3] - xt[j,0:3]
                P2 = PX[0]*PX[0]+PX[1]*PX[1]+PX[2]*PX[2]
                if P2 >= 4.* RHSH2:
                    if PM <= P2:
                        continue
                    PM = P2
                    JM = j
                    continue
            NR1 = NR1 + 1
            NOKR[i,NR1] = j
    
            if ((i <> j) and (P2 >= RHSH2)):
                if PM <= P2:
                    continue
                PM = P2
                JM = j
                continue
    
            NR = NR + 1
            if NR > KTO:
                print "КОЛИЧЕСТВО УЗЛОВ В ОКРЕСТНОСТИ ПОД ШАПОЧКОЙ ТОЧКИ С НОМЕРОМ",i,"ПРЕВЫШАЕТ МАКСИМАЛЬНО ДОПУСТИМОЕ"
                return
            NTSHA[i,NR] = j
        
        if PMAX < PM:
            PMAX = PM
            JMAX = JM
            IMAX = i
            continue
        if PMINN > PM:
            PMINN = PM
            JMIN = JM
            IMINT = i
    
    PMAX = math.sqrt(PMAX)
    PMINN = math.sqrt(PMINN)

    # print "МИНИМУМ КРАТЧАЙШЕГО РАССТОЯНИЯ РАВНЫЙ",PMINN,"ИМЕЕМ МЕЖДУ ТОЧКАМИ",IMINT,"И",JMIN,"МАКСИМУМ РАВЕН",PMAX,"МЕЖДУ",IMAX,"И",JMAX
    
    PM = 0.
    for kx in range(0,KT,1):
        for k in range(0,KT,1):
            R2 = 0.
            for i in range(0,3,1):
                VS = xt[kx,i] - xt[k,i]
                R2 = R2 + VS * VS
            if R2 > PM:
                PM = R2
    
    NMIN1 = MINKV - 1
    for kx in range(0,KT,1):
        if MINKV == 0:
            continue
        PMIN[0:NMIN1] = PM
        for k in range(0,KT,1):
            if k == kx:
                continue
            R2 = 0.
            for i in range(0,3,1):
                VS = xt[k,i] - xt[kx,i]
                R2 = R2 + VS * VS
            for i in range(0,NMIN1,1):
                if R2 < PMIN[i]:
                    # continue???
                    if i == (NMIN1 - 1):
                        PMIN[i] = R2
                        IMIN[i] = k
                    else:
                        IVS = i + 1
                        for j in range(IVS,NMIN1,1):
                            PMIN[NMIN1 + IVS - j] = PMIN[NMIN1 + IVS - j - 1]
                            IMIN[NMIN1 + IVS - j] = IMIN[NMIN1 + IVS - j - 1]
                            # PMIN[NMIN1 + IVS - j - 1] = PMIN[NMIN1 + IVS - j - 2]
                            # IMIN[NMIN1 + IVS - j - 1] = IMIN[NMIN1 + IVS - j - 2]
                    break
        
        INTER[kx,1:NMIN1 + 1] = IMIN[0:NMIN1]
        INTER[kx,0] = kx
    
    
    ALPHA[0:KT,0:3,0:3]=0.
    BETA[0:KT,0:3,0:3]=0.
    IH1[0:KT,0:3]=0.
    IH2[0:KT,0:3]=0.
    NVECT[0:KT,0:3]=0.
    NVECH[0:KT,0:3]=0.
    
    for i in range(0,KT,1):
        XA[0:3] = xt[i,0:3] * (aobr[0:3]) * (aobr[0:3])
        DLX = 1./math.sqrt(XA[0]*XA[0]+XA[1]*XA[1]+XA[2]*XA[2])
        NVECT[i,0:3] = XA[0:3] * DLX
    
    for i in range(0,KT,1):
        VS = 0.
        for INDS in range(0,KTO,1):
            if NTSHA[i,INDS] == (-1):
                ind = INDS
                break
    
        for j in range(0,3,1):
            VSPOM[j] = 0.
            for k in range(0,KTO,1):
                NSN = NTSHA[i,k]
                if ((ind < MINKV) and (k > MINKV)):
                    break
                if ind < MINKV:
                    NSN = INTER[i,k]
                if NSN == -1:
                    break
                VSPOM[j] = VSPOM[j] + NVECT[NSN,j]
            VS = VS + VSPOM[j] * VSPOM[j]
    
        if VS <> 0.:
            VS = 1./math.sqrt(VS)
        NVECH[i,0:3] = VSPOM[0:3] * VS
    
    for i in range(0,KT,1):
        VMIN1 = 1.
        for INDS in range(0,KTO,1):
            if NTSHA[i,INDS] == (-1):
                ind = INDS
                break
        for k in range(0,KTO,1):
            NSN = NTSHA[i,k]
            if ((ind < MINKV) and (k > MINKV)):
                break
            if ind < MINKV:
                NSN = INTER[i,k]
            if NSN == (-1):
                break
            VS = 0.
            for j in range(0,3,1):
                VS = VS + NVECH[i,j] * NVECT[NSN,j]
    
            if VS < VMIN1:
                VMIN1 = VS
    
        VSPOM[0:3] = NVECH[i,0:3]
        INVS = 0
    
        while (INVS < 100):
            VN = 0.
            INVS = INVS + 1
            VMIN2 = 1.
            # TODO возможно, здесь неправильно
            NMIN = 0
            for k in range(0,KTO,1):
                NSN = NTSHA[i,k]
                if ((ind < MINKV) and (k > MINKV)):
                    break
                if ind < MINKV:
                    NSN = INTER[i,k]
                if NSN == (-1):
                    break
                VN = VN + 1.
                VS = 0.
                for j in range(0,3,1):
                    VS = VS + NVECT[NSN,j] * VSPOM[j]
    
                if VS >= VMIN2:
                    continue
                VMIN2 = VS
                NMIN = NSN
            if VMIN2 >= VMIN1:
                VMIN1 = VMIN2
                if VN <> 0.:
                    VN = 1./VN
                VS = 0.
                for j in range(0,3,1):
                    VSPOM[j] = VSPOM[j] + VN * NVECT[NMIN,j]
                    VS = VS + VSPOM[j] * VSPOM[j]
                if VS <> 0.:
                    VS = 1./math.sqrt(VS)
                VSPOM[0:3] = VS * VSPOM[0:3]
    
        NVECH[i,0:3] = VSPOM[0:3]
    
        if VMIN1 >= 0.:
            continue
        print "ОКРЕСТНОСТЬ ТОЧКИ",i,"НЕЛЬЗЯ ОДНОЗНАЧНО СПРОЕКТИРОВАТЬ НА ВЫБРАННУЮ ПЛОСКОСТЬ, ВОЗМОЖНО, ЕЕ СЛЕДУЕТ УМЕНЬШИТЬ"
    
    for i in range(0,KT,1):
        VSPOM[0:3] = abs(NVECH[i,0:3])
        VS = VSPOM[0]
        for j in range(1,3,1):
            if VS > VSPOM[j]:
                VS = VSPOM[j]
    
        for j in range(0,3,1):
            if (abs(VS - VSPOM[j]) <= 1.e-10):
                jj = j
                break
    
        VS = 0.
        for k in range(0,3,1):
            IH1[i,k] = -NVECH[i,k] * NVECH[i,jj]
            if k == jj:
                IH1[i,k] = IH1[i,k] + 1.
            VS = VS + IH1[i,k] * IH1[i,k]
        VS = 1./math.sqrt(VS)
        IH1[i,0:3] = IH1[i,0:3] * VS
    
    IH3[0:KT,0:3] = NVECH[0:KT,0:3]
    
    for k in range(0,KT,1):
        for i in range(0,3,1):
            VS = 0.
            for j in range(0,3,1):
                for l in range(0,3,1):
                    VS = VS + EPS[i,j,l] * IH3[k,j] * IH1[k,l]
            IH2[k,i] = VS

    print "IH",IH1,IH2,IH3
    
    ALPHA[0:KT,0:3,0]=IH1[0:KT,0:3]
    ALPHA[0:KT,0:3,1]=IH2[0:KT,0:3]
    ALPHA[0:KT,0:3,2]=IH3[0:KT,0:3]
    
    for k in range(0,KT,1):
        DALPH = 0.
        for i in range(0,3,1):
            for j in range(0,3,1):
                for l in range(0,3,1):
                    DALPH = DALPH + EPS[i,j,l] * ALPHA[k,i,0] * ALPHA[k,j,1] * ALPHA[k,l,2]
    
        DOBRA = 1./DALPH
        VS = 1.
        for i in range(0,3,1):
            if i == 0:
                I1 = 1
                I2 = 2
            elif i == 1:
                I1 = 0
                I2 = 2
            else:
                I1 = 0
                I2 = 1
            for j in range(0,3,1):
                if j == 0:
                    J1 = 1
                    J2 = 2
                elif j == 1:
                    J1 = 0
                    J2 = 2
                else:
                    J1 = 0
                    J2 = 1
                # C	BETA(I,J) МОЖНО ВЫЧИСЛИТЬ ЕСЛИ СКАЛЯРНО ПЕРЕМНОЖИТЬ
                # C	НАПРАВЛЯЮЩИЙ ОРТ С НОМЕРОМ I ШТРИХОВАННОЙ СИСТЕМЫ НА ОРТ
                # C	J НЕШТРИХОВАННОЙ
                BETA[k,j,i] = VS * DOBRA * (ALPHA[k,I1,J1] * ALPHA[k,I2,J2] - ALPHA[k,I1,J2] * ALPHA[k,I2,J1])
                VS = -VS
    
    return

def neighbors(NVECT,xt,A,KT,numpoints,NVECH,NOKR):
    KTO = NeighborsMax()
    MINKM = LengthMinimumsMax()

    # tmp = zeros(KT)
    # yatmp = zeros(KT)
    # VSPOM = zeros(3)
    
    MINKV = 4
    RHSHA = get_h(A,PartsOneDimension(numpoints),RadiusHat())
    RHSH2 = RHSHA*RHSHA
    
    NTSHA = zeros((KT,KTO),int,order = 'Fortran')
    NTSHA[0:KT,0:KTO] = -1
    FilterElements(KT,  RHSH2,NTSHA,A,xt,checkH)

    KOKRM = KT    
    NOKR[0:KT,0:KOKRM] = -1    
    FilterElements(KT,4*RHSH2,NOKR, A,xt,checkH)


    # C	ОТЫСКАНИЕ НОСИТЕЛЕЙ КАЖДОЙ ШАПОЧКИ И НОСИТЕЛЕЙ ШАПОЧЕК,
    # C	ИМЕЮЩИХ ОБЩИЕ ТОЧКИ С НОСИТЕЛЕМ ДАННОЙ ШАПОЧКИ
    # IMIN = zeros(10,int,order = 'Fortran')
    # PMIN = zeros(10)
    # PMAX = 0.
    # PMINN = A[1]*A[1]
    # for i in range(0,KT,1):
    #     PM = A[1]*A[1]

    #     lstmp = []
    #     lstnokr = []
    #     for j in range(0,KT,1):
    #         P2 = dpair(xt,i,j)
            
    #         if ((i == j) or (P2 < 4.* RHSH2)):
    #             lstnokr.append(j)
            
    #         if ((i == j) or (P2 < RHSH2)):
    #             lstmp.append(j)
    #             continue

    #         if PM > P2:
    #             PM = P2
    #             JM = j

    #     if len(lstmp) > KTO:
    #         print "КОЛИЧЕСТВО УЗЛОВ В ОКРЕСТНОСТИ ПОД ШАПОЧКОЙ ТОЧКИ С НОМЕРОМ",i,"ПРЕВЫШАЕТ МАКСИМАЛЬНО ДОПУСТИМОЕ"
    #         return

    #     # NTSHA[i,0:len(lstmp)] = lstmp[0:len(lstmp)]
    #     # NOKR[i,0:len(lstnokr)] = lstnokr[0:len(lstnokr)]        
        
    #     if PMAX < PM:
    #         PMAX = PM
    #         JMAX = JM
    #         IMAX = i
    #         continue
    #     if PMINN > PM:
    #         PMINN = PM
    #         JMIN = JM
    #         IMINT = i
    
    # PMAX = math.sqrt(PMAX)
    # PMINN = math.sqrt(PMINN)
    
    # print "МИНИМУМ КРАТЧАЙШЕГО РАССТОЯНИЯ РАВНЫЙ",PMINN,"ИМЕЕМ МЕЖДУ ТОЧКАМИ",IMINT,"И",JMIN,"МАКСИМУМ РАВЕН",PMAX,"МЕЖДУ",IMAX,"И",JMAX
    
    PM = DistanceMax(KT,xt)
    # PM = 0.
    # for kx in range(0,KT,1):
    #     for k in range(0,KT,1):
    #         # R2 = 0.
    #         # for i in range(0,3,1):
    #         #     VS = xt[kx,i] - xt[k,i]
    #         #     R2 = R2 + VS * VS
    #         R2 = dpair(xt,kx,k)
    #         if R2 > PM:
    #             PM = R2

    # C	ВЫЧИСЛЕНИЕ МАКСИМАЛЬНОГО РАССТОЯНИЯ МЕЖДУ ТОЧКАМИ ПОВ-ТИ
    # # Здесь показана краткая запись поиска PM. MAXLOC - для поиска индекса максимального элемента.
    # for kx in range(0,KT,1):
    #     for k in range(0,KT,1):
    #         tmp[k] = dpair(xt,kx,k)
    #     yatmp[kx] = tmp.max()
    #     # max_index_j[kx] = tmp.index(yatmp[kx])
    # PM = yatmp.max()
    # # max_index_i = yatmp.index(PM)


#######################################################
    # судя по всему, здесь вычисляются в порядке возрастания/убывания
    # NMIN1 значений, ближайших к PM, т.е. самое большое, предыдущее и т.д.
    # Очевидно, здесь какой-то алгоритм сортировки.
    # Ищем точки, ближайшие к данной и накапливаем их NMIN1 штук.
    # C	ВЫЧИСЛЕНИЕ НОМЕРОВ ТОЧЕК, ПО КОТОРЫМ БУДЕМ ВЕСТИ ИНТЕРПОЛЯЦИЮ

    INTER = zeros((KT,MINKM),int,order = 'Fortran')
    INTER[0:KT,0:MINKM] = -1
    NMIN1 = MINKV - 1
    GetPointsInterpolation(PM,NMIN1,KT,xt,INTER)
    # for kx in range(0,KT,1):
    #     # if MINKV == 0:
    #     #     continue
    #     PMIN[0:NMIN1] = PM # заполняем массив числами заведомо >= любого текущего расстояния между точками
    #     for k in range(0,KT,1):
    #         if k == kx:
    #             continue
    #         # for i in range(0,3,1):
    #         #     R2 = dpair(xt,i,j)
    #         R2 = dpair(xt,k,kx)
    #         for i in range(0,NMIN1,1):
    #             if R2 < PMIN[i]:
    #                 if i == (NMIN1 - 1):
    #                     PMIN[i] = R2 # add element
    #                     IMIN[i] = k
    #                 else:
    #                     # but max i = NMIN1 - 1 i.e.
    #                     # PMIN[NMIN1] = PMIN[NMIN1 - 1]
    #                     # IMIN[NMIN1] = IMIN[NMIN1 - 1]
    #                     # NMIN1,...,I + 1
    #                     # NMIN1 - 1,...,I
    #                     # PMIN[i:NMIN1] = PMIN[i - 1:NMIN1 - 2] # shift
    #                     # IMIN[i + 1:NMIN1 - 1] = IMIN[i:NMIN1 - 2]
    #                     PMIN[i + 1:NMIN1 - 1] = PMIN[i:NMIN1 - 2]
    #                     IMIN[i + 1:NMIN1 - 1] = IMIN[i:NMIN1 - 2]
    #                     # IVS = i + 1
    #                     # for j in range(IVS,NMIN1,1):
    #                     #     PMIN[NMIN1 + IVS - j - 1] = PMIN[NMIN1 + IVS - j - 2]
    #                     #     IMIN[NMIN1 + IVS - j - 1] = IMIN[NMIN1 + IVS - j - 2]
    #                         # т.к. i = NMIN1 - 2 сюда только доходило
    #                         # поэтому лишний сдвиг происходил при P[NMIN1]
    #                         # PMIN[NMIN1 + IVS - j] = PMIN[NMIN1 + IVS - j - 1]
    #                         # IMIN[NMIN1 + IVS - j] = IMIN[NMIN1 + IVS - j - 1]
    #                 break
        
    #     INTER[kx,1:NMIN1 + 1] = IMIN[0:NMIN1]
    #     INTER[kx,0] = kx

    VSPOM = zeros(3)        
    NVECH[0:KT,0:3]=0.

    # ...но сохраняются только номера этих точек, т.е. IMIN.
#######################################################
    # # C	ВЫЧИСЛЕНИЕ НОРМАЛЬНОГО ВЕКТОРА СО ШТРИХОМ (NVECH? ) n' (МММП, с. 65 - 66)
    # for i in range(0,KT,1):
    #     ind = list(NTSHA[i,:]).index(-1)
    #     # for INDS in range(0,KTO,1):
    #     #     if NTSHA[i,INDS] == (-1):
    #     #         ind = INDS
    #     #         break

    # # общая сумма векторов NVECT по всем k

    #     VS = 0.
    #     for j in range(0,3,1):
    #         VSPOM[j] = 0.
    #         for k in range(0,KTO,1):
    #             NSN = NTSHA[i,k]
    #             if ((ind < MINKV) and (k > MINKV)):
    #                 break
    #             if ind < MINKV:
    #                 NSN = INTER[i,k]
    #             if NSN == -1:
    #                 break
    #             VSPOM[j] = VSPOM[j] + NVECT[NSN,j]
    #         VS = VS + VSPOM[j] * VSPOM[j]
        
    #     if VS <> 0.:
    #         VS = 1./math.sqrt(VS)
            
    #     NVECH[i,0:3] = VSPOM[0:3] * VS
    
    PrepareStroke(KT,KTO,MINKV,NTSHA,INTER,NVECT,NVECH)
#######################################################
    # ... по этим номерам собирается NVECH 
    for i in range(0,KT,1):
        ind = list(NTSHA[i,:]).index(-1)
        # for INDS in range(0,KTO,1):
        #     if NTSHA[i,INDS] == (-1):
        #         ind = INDS
        #         break

        # для каждого k своя сумма VS и ищется минимум.
        VMIN1,NMIN,VN = shiftValue(1.,0,0.,i,ind,KTO,NTSHA,MINKV,INTER,NVECH[i,:],NVECT)
        # print "shift ",VMIN1
        # VMIN1 = 1.        
        # for k in range(0,KTO,1):
        #     NSN = NTSHA[i,k]
        #     if ((ind < MINKV) and (k > MINKV)):
        #         break
        #     if ind < MINKV:
        #         NSN = INTER[i,k]
        #     if NSN == (-1):
        #         break
            
        #     VS = 0.
        #     for j in range(0,3,1):
        #         VS = VS + NVECH[i,j] * NVECT[NSN,j]

        #     # VS = dot(NVECH[i,:],NVECT[NSN,:])
            
        #     if VS < VMIN1:
        #         VMIN1 = VS
                
        # print "old ",VMIN1
        VSPOM[0:3] = NVECH[i,0:3]
        
        INVS = 0
        while (INVS < 100):

            INVS = INVS + 1
            VMIN2,NMIN,VN = shiftValue(1.,0,0.,i,ind,KTO,NTSHA,MINKV,INTER,VSPOM,NVECT)
            # VN = 0.           
            # VMIN2 = 1.
            # # TODO возможно, здесь неправильно
            # NMIN = 0
            # for k in range(0,KTO,1):
            #     NSN = NTSHA[i,k]
            #     if ((ind < MINKV) and (k > MINKV)):
            #         break
            #     if ind < MINKV:
            #         NSN = INTER[i,k]
            #     if NSN == (-1):
            #         break
            #     VN = VN + 1.
                
            #     VS = 0.
            #     for j in range(0,3,1):
            #         VS = VS + NVECT[NSN,j] * VSPOM[j]

            #     # VS = dot(NVECT[NSN,:],VSPOM[:])
                
            #     if VS < VMIN2:
            #     # if (VS - VMIN2) <= - 1.0e-17:
            #         VMIN2 = VS
            #         NMIN = NSN

            if VMIN2 - VMIN1 >= -1.0e-17:
                VMIN1 = VMIN2
                if VN <> 0.:
                    VN = 1./VN
                    
                VS = 0.
                for j in range(0,3,1):
                    VSPOM[j] = VSPOM[j] + VN * NVECT[NMIN,j]
                    VS = VS + VSPOM[j] * VSPOM[j]
                if VS <> 0.:
                    VS = 1./math.sqrt(VS)
                VSPOM[0:3] = VS * VSPOM[0:3]
                
            # # вроде работает, но вот правильно ли это? 
            # else:
            #     break
    
        NVECH[i,0:3] = VSPOM[0:3]
    
        if VMIN1 < 0.:
            print "ОКРЕСТНОСТЬ ТОЧКИ",i,"НЕЛЬЗЯ ОДНОЗНАЧНО СПРОЕКТИРОВАТЬ НА ВЫБРАННУЮ ПЛОСКОСТЬ, ВОЗМОЖНО, ЕЕ СЛЕДУЕТ УМЕНЬШИТЬ"

    return

def integtmp(DINTEG,DINTE1,MAXIK,ITIPF,ITIPF1,IDEJ,PARTEL,NOKR,RHSHA,XT,BETA,ALPHA,AOBR,KREG,KGM,GREG,KFGM,XREG,ALPNY,BETNY,IKOLF,LOCI,EPSPOL,IELL,KOKRM,KT):

    RREG = zeros(KGM)
    BREG = zeros(KGM)
    REG = zeros((2,KFGM),order = 'Fortran')
    DFINY = zeros(2)
    A = zeros(3)
    YHSET = zeros(3)
    FHDIF = zeros(2)
    YH = zeros(3)
    Y = zeros(3)
    ALPVL = zeros((3,2),order = 'Fortran')
    VSPOM = zeros(3)
    COSCAS = zeros((KT,2,3),order = 'Fortran')
    ELOC = zeros((3,2),order = 'Fortran')
    GLOC = zeros((2,2),order = 'Fortran')
    GSOP = zeros((2,2),order = 'Fortran')
    ESOP = zeros((3,2),order = 'Fortran')
    
    EPS = array([0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,1.00000000000000000,
                 0.0000000000000000,-1.00000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,-1.00000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000,
                 1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,1.00000000000000000,0.0000000000000000,
                 -1.00000000000000000,0.0000000000000000,0.0000000000000000,
                 0.0000000000000000,0.0000000000000000,0.0000000000000000])
    EPS.shape = (3,3,3)
    
    PI=3.14159265358979324
    
    AEL=LOCI[0]
    BEL=LOCI[1]
    CEL=LOCI[2]

    A[0]=LOCI[0]
    A[1]=LOCI[1]
    A[2]=LOCI[2]
    
    for ky in range(0,KT,1):
        
        # YHSET[0:3] = 0.
        # for j in range(0,3,1):
        #     YHSET[0:3] = YHSET[0:3] + BETA[ky,0:3,j] * XT[ky,j]
        for j in range(0,3,1): YHSET[j] = dot(BETA[ky,j,:],XT[ky,:])

        FH,INF = fhloc(ky,ALPHA,AOBR,YHSET,EPS,FHDIF)

        if INF == 0:
            for j in range(0,2,1):
                
                # VEK = 0.
                # for i in range(0,3,1):
                #     Y[i] = ALPHA[ky,i,j] + ALPHA[ky,i,2] * FHDIF[j]
                #     VEK = VEK + Y[i] * Y[i]
                    
                Y[0:3] = ALPHA[ky,0:3,j] + ALPHA[ky,0:3,2] * FHDIF[j]
                VEK = dot(Y[:],Y[:])

                VEK = math.sqrt(VEK)
                Y[0:3] = Y[0:3] / VEK
                COSCAS[ky,j,0:3] = Y[0:3]

#######################################################                
    BEL=A[1]
    AEL=A[0]
    
    KFREG=4*KREG
    
    RHOBR=1./RHSHA
    RHSH2=RHSHA*RHSHA
    
    VS=2.*PI/KFREG
    for i in range(0,KFREG,1):
        VSS = VS * (i + 1)
        REG[0,i] = math.cos(VSS) * RHSHA
        REG[1,i] = math.sin(VSS) * RHSHA

    RREG[0:KREG] = map(lambda x:math.sqrt(1.- x),XREG[0:KREG])
    BREG[0:KREG] = 0.5 * VS * RHSH2 * GREG[0:KREG] / (XREG[0:KREG] * XREG[0:KREG])

    for ky in range(0,KT,1):
        # YHSET[0:3] = 0.
        # for j in range(0,3,1):
        #     YHSET[0:3] = YHSET[0:3] + BETA[ky,0:3,j] * XT[ky,j]
        for j in range(0,3,1): YHSET[j] = dot(BETA[ky,j,:], XT[ky,:])

        DINTEG[ky] = 0.
        for l1 in range(0,KREG,1):
            for l2 in range(0,KFREG,1):
                YH[0:2] = YHSET[0:2] + REG[0:2,l2] * RREG[l1]
                FH,INF = fhloc(ky,ALPHA,AOBR,YH,EPS,FHDIF)
                if INF <> 0:
                    break
                
                Y[0:3] = 0.
                for j in range(0,2,1):
                    ALPVL[0:3,j] = ALPHA[ky,0:3,j] + ALPHA[ky,0:3,2] * FHDIF[j]
                    Y[0:3] = Y[0:3] + ALPHA[ky,0:3,j] * YH[j]
                
                Y[0:3] = Y[0:3] + ALPHA[ky,0:3,2] * FH
                FINYO = finfi(ky,XT,Y,NOKR,KOKRM,ALPVL,DFINY,RHSHA)
                AL13=ALPHA[ky,0,2]
                AL23=ALPHA[ky,1,2]
                AL33=ALPHA[ky,2,2]
                if IELL == 0:
                    TENMET=math.sqrt((ALPVL[1,0]*ALPVL[2,1]-ALPVL[1,1]*ALPVL[2,0])**2+(ALPVL[2,0]*ALPVL[0,1]-ALPVL[2,1]*ALPVL[0,0])** 2+(ALPVL[0,0]*ALPVL[1,1]-ALPVL[0,1]*ALPVL[1,0])**2)

                DINTEG[ky] = DINTEG[ky] + BREG[l1] * TENMET * FINYO

    DINT = 0.
    for i in range(0,KT,1):
        for j in range(0,3,1):
            DINTE1[i,j] = XT[i,j]
        DINT = DINT + DINTEG[i]

    DINTT = DINT / KT
    return
                        
# a1 = 0.75 # 1 axis of ellipse
# a2 = 1. # 2 axis of ellipse
# a3 = 0.5

# n2 = 10 # sqrt from 100 TODO: ???


# print 'Pi=',pi
# print 'Cos(pi)=',cos(pi)

# m = 51

# fi = zeros(m)
# x2 = zeros(m)
# x1 = zeros(m)

# x1f = zeros(m)
# x2f = zeros(m)
# fif = zeros(m)

# for i in range(0,3,1):
#     print fi[0:100]
# # ell(a1,a2,x1,x2,m,n2,fi,0)
# # ell(a1,a2,x1,x2,m,n2,fi,1)

# print '%.16g' % (ep2.ep(0.10))
# print '%.16g' % (ep2p(0.1))

# ell(a1,a2,x1,x2,m,n2,fi,0)
# ep2.ell(a1,a2,a3,x1f,x2f,m,n2,fif,0)
# for i in range(0,n2+1,1):
#     print "test point.ell-ep2.ell in=0 --- ",abs(x1[i]-x1f[i])
#     print "x1f[",i,"] = ",x1f[i]


# x1 = zeros(m)
# x2 = zeros(m)
# fi = zeros(m)
# ell(a1,a2,x1,x2,m,n2,fi,1)
# x1f = zeros(m)
# x2f = zeros(m)
# fif = zeros(m)
# ep2.ell(a1,a2,a3,x1f,x2f,m,n2,fif,1)
# for i in range(0,n2+1,1): # n2 items
#     print "ell in=1 --- ",abs(x1[i]-x1f[i]),abs(x2[i]-x2f[i])
#     print "x1f[",i,"] = ",x1f[i]
        
# kt = 0
# ktmax = 120
# xt = zeros((120,3))
# a = array([a1,a2,a3])
# point(kt,xt,ktmax,a)
# print "py.point.kt=",kt

# xtep = array([zeros(120*3)])
# xtep.shape = (3,120)
# xtep = xtep.transpose()
# ep2.point(kt,xtep,ktmax,a)

# # variables not transfer, although in point.f90 variable kt intent(inout)
# print "ep2.point.kt=",kt
# s = 0.
# xtot = 0.
# # only arrays transfer from ep2.point and py.point
# for i in range (0,96,1):
#     s = s + abs(xtep[i][0]-xt[i][0])+abs(xtep[i][1]-xt[i][1])+abs(xtep[i][2]-xt[i][2])
#     xtot = xtot + abs(xtep[i][0])+abs(xtep[i][1])+abs(xtep[i][2])
#     print xtep[i][0]
#     # print "s=",s

# print "norm(py.point.xtep - f90.point.xt) = ",s
# print "xtep[1][0]=",xtep[1][0]
# print "xtep total", xtot
# # print xt
# # print xtep

if __name__ == '__main__':
    """
    """

    # integrate from 0 to tstop
    try:
        numpoints = float(sys.argv[1])
    except:
        print 'Usage: %s numpoints' % sys.argv[0]; sys.exit(1)

    LOCI=[float(0.75),float(1.),float(0.5)]

    KTMAX = 10000
    XT = zeros((10000,3))
    KT = 0
    # KT = point(KT,XT,KTMAX,LOCI,numpoints)
    KT = SamplingEllipsoide(LOCI,numpoints,XT)
    # unittest for point
    print DistanceMax(numpoints,XT)
    
    # s = zeros(3)
    # for i in range(0,KT,1):
    #     s[0:3] =  s[0:3] +  XT[i,0:3]
    #     print "%s,%s,%s" % (XT[i,0],XT[i,1],XT[i,2])
    # print s

