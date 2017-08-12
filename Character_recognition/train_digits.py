import graphlab as gl

trainData = gl.SFrame.read_csv('traindata.csv', header=True)

Y = trainData['Character']

featureColumns = ['Thumb Near', 'Thumb Far', 'Thumb/Index', 'Index Near', 'Index Far', 'Index/Middle', 'Middle Near', 'Middle Far', 'Middle/Ring', 'Ring Near', 'Ring Far', 'Ring/Little', 'Little Near', 'Little Far']
model = gl.classifier.create(trainData, target = 'Character', features = featureColumns)

# classification = model.classify(trainData)
# results = model.evaluate(trainData)
model.save('mymodel')

# print results