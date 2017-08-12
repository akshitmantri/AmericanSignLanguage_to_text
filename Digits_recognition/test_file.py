import graphlab as gl

testData = gl.SFrame.read_csv('traindata.csv', header=True)

loaded_model = gl.load_model('mymodel')
classification = loaded_model.classify(testData)
f = open('output.txt','w')
for elem in classification:
	f.write(str(elem))
f.close()
# print classification
