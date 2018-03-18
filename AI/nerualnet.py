from neural_layer import NerualLayer
from activation import Linear
import numpy as np
class NerualNet():
    def __init__(self, shape): #shape is a list of sizes for neural layers
        self._first = NerualLayer(inputs=shape[0], outputs=shape[1])
        tmp = self._first
        for i in range(1, len(shape) - 1):
            self._last = NerualLayer(inputs=shape[i], outputs=shape[i+1], prev=tmp)
            tmp = self._last
        self._last._activation = Linear()

    def predict(self, input):
        return self._first.feed_forward(input)[0]

    def train(self, error):
        self._last.backpropagate(error)

