# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:36:14 2022

@author: Farhan
"""

# Load libraries
import os
import netCDF4
import numpy as np
import numpy.ma as ma
from netCDF4 import Dataset


# Load dataset
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

#datatraining
file1 = 'D:/DATA SET TA/Januari TBB/29 jan/NC_H08_20220129_0850_R21_FLDK.02401_02401.nc'
file2 = 'D:/DATA SET TA/Tipe awan/januari 17-31/29/08/NC_H08_20220129_0850_L2CLP010_FLDK.02401_02401.nc'

#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dset1 = Dataset(file1,'r')
dset2 = Dataset(file2,'r')



lats = dset1.variables['latitude'][:]
lons = dset1.variables['longitude'][:]

b07 = (ma.getdata((dset1).variables['tbb_07'][:])).ravel()
b08 = (dset1.variables['tbb_08'][:]).ravel()
b09 = (dset1.variables['tbb_09'][:]).ravel()
b10 = (dset1.variables['tbb_10'][:]).ravel()
b11 = (ma.getdata((dset1).variables['tbb_11'][:])).ravel()
b12 = (dset1.variables['tbb_12'][:]).ravel()
b13 = (ma.getdata((dset1).variables['tbb_13'][:])).ravel()
b14 = (dset1.variables['tbb_14'][:]).ravel()
b15 = (dset1.variables['tbb_15'][:]).ravel()
b16 = (dset1.variables['tbb_16'][:]).ravel()

cler = (dset2.variables['CLER_23'][:]).ravel()
clot = (dset2.variables['CLOT'][:]).ravel()
clth = (dset2.variables['CLTH'][:]).ravel()
cltt = (ma.getdata(dset2.variables['CLTT'][:])).ravel()
cltype = (dset2.variables['CLTYPE'][:]).ravel()

#datavalidasi
file3 = 'D:/DATA SET TA/Januari TBB/29 jan/NC_H08_20220129_0900_R21_FLDK.02401_02401.nc'
file4 = 'D:/DATA SET TA/Tipe awan/januari 17-31/29/09/NC_H08_20220129_0900_L2CLP010_FLDK.02401_02401.nc'

dset3 = Dataset(file3,'r')
dset4 = Dataset(file4,'r')


b07v = (ma.getdata(dset3.variables['tbb_07'][:])).ravel()
b08v = (dset3.variables['tbb_08'][:]).ravel()
b09v = (dset3.variables['tbb_09'][:]).ravel()
b10v = (dset3.variables['tbb_10'][:]).ravel()
b11v = (ma.getdata(dset3.variables['tbb_11'][:])).ravel()
b12v = (dset3.variables['tbb_12'][:]).ravel()
b13v = (ma.getdata(dset3.variables['tbb_13'][:])).ravel()
b14v = (dset3.variables['tbb_14'][:]).ravel()
b15v = (dset3.variables['tbb_15'][:]).ravel()
b16v = (dset3.variables['tbb_16'][:]).ravel()

clerv = (dset4.variables['CLER_23'][:]).ravel()
clotv = (dset4.variables['CLOT'][:]).ravel()
clthv = (dset4.variables['CLTH'][:]).ravel()
clttv = (ma.getdata(dset4.variables['CLTT'][:])).ravel()
cltypev = (dset4.variables['CLTYPE'][:]).ravel()

# Split-out validation dataset
from sklearn import model_selection

from tqdm import tqdm

X = []
for i in range(len(b07)):
    X.append([b07[i],b11[i],b13[i]])

Y = []
#for i in range(len(cltype)):
for i in tqdm(range(5764801)):
    if cltype[i] >= 0 and cltype[i] < 1:
        Y.append(1)
    elif cltype[i] >= 1 and cltype[i] < 2:
        Y.append(2)
    elif cltype[i] >= 2 and cltype[i] < 3:
        Y.append(3)
    elif cltype[i] >= 3 and cltype[i] < 4:
        Y.append(4)
    elif cltype[i] >= 4 and cltype[i] < 5:
        Y.append(5)
    elif cltype[i] >= 5 and cltype[i] < 6:
        Y.append(6)
    elif cltype[i] >= 6 and cltype[i] < 7:
        Y.append(7)
    elif cltype[i] >= 7 and cltype[i] < 8:
        Y.append(8)
    elif cltype[i] >= 8 and cltype[i] < 9:
        Y.append(9)
    elif cltype[i] >= 9 and cltype[i] < 10:
        Y.append(10)
    else :
        Y.append(11)
        
        
Y = np.array (Y).reshape(5764801,1)


X_train=X[:]
Y_train=Y[:]

Xv = []
for i in range(len(b07)):
    Xv.append([b07v[i],b11v[i],b13v[i]])

from tqdm import tqdm

Yv = []
#for i in range(len(cltypev)):
for i in tqdm(range(5764801)):
    if cltypev[i] >= 0 and cltypev[i] < 1:
        Yv.append(1)
    elif cltypev[i] >= 1 and cltypev[i] < 2:
        Yv.append(2)
    elif cltypev[i] >= 2 and cltypev[i] < 3:
        Yv.append(3)
    elif cltypev[i] >= 3 and cltypev[i] < 4:
        Yv.append(4)
    elif cltypev[i] >= 4 and cltypev[i] < 5:
        Yv.append(5)
    elif cltypev[i] >= 5 and cltypev[i] < 6:
        Yv.append(6)
    elif cltypev[i] >= 6 and cltypev[i] < 7:
        Yv.append(7)
    elif cltypev[i] >= 7 and cltypev[i] < 8:
        Yv.append(8)
    elif cltypev[i] >= 8 and cltypev[i] < 9:
        Yv.append(9)
    elif cltypev[i] >= 9 and cltypev[i] < 10:
        Yv.append(10)
    else : 
        Yv.append(11)

        
Yv = np.array (Yv).reshape(5764801,1)

X_validation=Xv[:]
Y_validation=Yv[:]


# Build models
from sklearn.linear_model import LogisticRegression
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#from sklearn.naive_bayes import GaussianNB
#from sklearn.svm import SVR
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.ensemble import ExtraTreesClassifier
#from sklearn.neural_network import MLPClassifier

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
#models.append(('LDA', LinearDiscriminantAnalysis()))
#models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVR(gamma='auto')))
#models.append(('RF',RandomForestClassifier(n_estimators=10)))
#models.append(('ETC',ExtraTreesClassifier(n_estimators=10)))
#models.append(('MLP',MLPClassifier()))

Y_prediction=[]
names=[]
for name, model in models:
        model.fit(X_train,Y_train.ravel())
        prediction=model.predict(X_validation)
        Y_prediction.append(prediction)
        names.append(name)

#Accuracy score
from sklearn.metrics import accuracy_score

acc=[]
for i in range (len(Y_prediction)):
        accuracy = accuracy_score(Y_validation, Y_prediction[i])
        acc.append(accuracy)
        
for i in range (len(acc)):
        print (names[i],'=',acc[i])

######## MAP PLOTTING ########
#import modul
proj_lib = os.path.join(os.path.join('Library'), 'share')
os.environ["PROJ_LIB"] = proj_lib
from mpl_toolkits.basemap import Basemap
import pylab

Y_prediction = np.array(Y_prediction)
Y_prediction = 0+(1*Y_prediction)

yp = np.array (Y_prediction).reshape(2401,2401)
#setup map projection
m = Basemap(projection='cyl',llcrnrlat=-7.6,urcrnrlat=-6,
        llcrnrlon=107,urcrnrlon=108,resolution='h')

#menampilkan garis lintang-bujur
paralles = pylab.arange(-90.0,90.,5)
meridians = pylab.arange(0.,360.,10)
m.drawcoastlines(color='k',linewidth=0.3)
m.drawparallels(paralles,labels=[1,0,0,0],fontsize=8,color='k',linewidth=0.2)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=8,color='k',linewidth=0.2)

#filled contour
xv,yv=pylab.meshgrid(lons,lats)
lon,lat = m(xv,yv)

# plot data
clev = pylab.arange(0,11,1) 

label = ['Ci','Cs','DC','Ac','As','Ns','Cu','Sc','St']
cs = m.contourf(lon,lat,yp,levels=clev)
cbar = m.colorbar(cs,location='right',pad='5%')

#garis pantai
m.drawcoastlines(color='k',linewidth=0.3)

#map title
#pylab.title('Cloud Effective Radius Using Band 6')
#pylab.title('Cloud Optical Thickness')
#pylab.title('Cloud Top Height')
#pylab.title('Cloud Top Temperature')
pylab.title('Cloud Type Under ISCCP Cloud Type Classification Definition')

#save figure
#pylab.savefig('Himawari.png')

#show figure
pylab.show()