import angle, scipy, h5py

f = h5py.File('C:/Users/ltopuser/behavioral_syntax/utilities/data.mat')

#getting the right cell array:
l1 = f.get('worm')

l2 = l1.get('posture')

l3 = l2.get('skeleton')

#getting the x and y coordinates:
X = l3.get('x')

Y = l3.get('y')

angleArray, meanAngles = angle(X,Y)

#save data
scipy.io.savemat('angleArray.mat', dict(x=angleArray))
scipy.io.savemat('meanAngles.mat', dict(y=meanAngles))


#loading data:
#angles = sio.loadmat('C:/Users/ltopuser/behavioral_syntax/data/angles.mat')
#array = angles.get('x')
