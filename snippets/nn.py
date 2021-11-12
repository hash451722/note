import numpy as np

class Net:
    ''' 入力層：5ノード
        隠れ層：4ノード
        隠れ層：3ノード
        出力層：2ノード
    '''
    def __init__(self, params=np.random.randn(47)) -> None:
        self.network = {}
        self.network['W1'] = params[0:20].reshape(5, 4)
        self.network['b1'] = params[20:24]
        self.network['W2'] = params[24:36].reshape(4, 3)
        self.network['b2'] = params[36:39]
        self.network['W3'] = params[39:45].reshape(3, 2)
        self.network['b3'] = params[45:47]
    
    def __repr__(self):
        return "NN()"

    def count(self):
        ''' 変数の個数 '''
        nw = self.network['W1'].size + self.network['W2'].size + self.network['W3'].size
        nb = self.network['b1'].size + self.network['b2'].size + self.network['b3'].size
        return nw + nb

    def sigmoid(self, x):
        ''' 隠れ層の活性化関数 '''
        return 1 / (1 + np.exp(-x))

    def tanh(self, x):
        ''' 出力層の活性化関数 '''
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    def forward(self, x):
        W1, W2, W3 = self.network['W1'], self.network['W2'], self.network['W3']
        b1, b2, b3 = self.network['b1'], self.network['b2'], self.network['b3']

        a1 = np.dot(x, W1) + b1
        z1 = self.sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = self.sigmoid(a2)
        a3 = np.dot(z2, W3) + b3
        y = self.tanh(a3)

        return y



if __name__ == '__main__':
    print("nn module")

    net = Net()
    # print(net)

    x = np.array([1.0, 0.5, 0.3, 0.2, 0.9])
    output = net.forward(x)
    print(output)

    print( net.count() )

    x = np.array([1.0, 0.5, 0.3, 0.2, 0.9])
    output = net.forward(x)
    print(output)
