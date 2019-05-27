from neurlnet import Neuralnet
net = Neuralnet()

value = net.compute([0.994 ,- 0.98924685 ,- 0.14625543])
value2 = net.compute([10, - 0.98924685, - 0.24625543])
print(value)
print(value2)
