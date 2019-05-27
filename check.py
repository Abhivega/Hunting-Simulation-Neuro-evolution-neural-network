from neurlnet import Neuralnet
net = Neuralnet()
net2 = Neuralnet()

value = net.compute([0.994 ,- 0.98924685 ,- 0.14625543])
value2 = net2.compute([0.994, - 0.98924685, - 0.14625543])
print(value)
print(value2)
