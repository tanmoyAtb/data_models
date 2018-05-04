from sklearn import tree

clf = tree.DecisionTreeClassifier()

#outlook, temperature, humidity, wind
X = [[0, 0,  0,  0],
	 [0, 0,  0,  1],
	 [1, 0,  0,  0],
	 [2, 1,  0,  0],
	 [2, 2,  1,  0],
	 [2, 2,  1,  1],
	 [1, 2,  1,  1],
	 [0, 1,  0,  0],
	 [0, 2,  1,  0],
	 [2, 1,  1,  0],
	 [0, 1,  1,  1],
	 [1, 1,  0,  1],
	 [1, 0,  1,  0],
	 [2, 1,  0,  1]]

#played?
Y =  ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 
		'no', 'yes','yes','yes','yes','yes','no']

# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict([[1, 0,  1, 0]])
 
# CHALLENGE compare their reusults and print the best one!

print(prediction)

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict([[150, 55, 39]])

# CHALLENGE compare their reusults and print the best one!

print(prediction)