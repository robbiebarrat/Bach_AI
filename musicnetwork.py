from pybrain.structure import RecurrentNetwork
from pybrain.structure import FullConnection, LinearLayer, LSTMLayer
from parsemusic import ds
import random
print ds


layerCount = 10

net = RecurrentNetwork()
net.addInputModule(LinearLayer(10, name='in'))
for x in range(layerCount):
    net.addModule(LSTMLayer(20, name='hidden' + str(x)))
net.addOutputModule(LinearLayer(10, name='out'))
net.addConnection(FullConnection(net['in'], net['hidden1'], name='cIn'))
for x in range(layerCount - 1):
    net.addConnection(FullConnection(net[('hidden' + str(x))], net['hidden' + str(x + 1)], name=('c' + str(x + 1))))
net.addConnection(FullConnection(net['hidden' + str(layerCount - 1)], net['out'], name='cOut'))
net.sortModules()
from pybrain.supervised import RPropMinusTrainer
trainer = RPropMinusTrainer(net, dataset=ds)

epochcount = 0
while True:
    startingnote = random.choice(range(1, 17))
    startingnote2 = random.choice(range(1, 17))
    startingduration = random.choice(range(1,17))
    startingduration2 = random.choice(range(1, 17))
    song = [[startingnote, startingduration, 1, 1, 0, startingnote2, startingduration2, 1, 1, 0]]
    length = 50
    while len(song) < length:
        song.append(net.activate(song[-1]).tolist())
    newsong = []
    for x in song:
        newx = []
        newy = []
        for i in x:
            if len(newx) < 5:
                newx.append(int(i))
            else:
                newy.append(int(i))
        newsong.append(newx)
        newsong.append(newy)

    print newsong
    print "The above song is after " + str(epochcount) + " epochs."
    trainer.trainEpochs(epochs=1)
    epochcount += 1