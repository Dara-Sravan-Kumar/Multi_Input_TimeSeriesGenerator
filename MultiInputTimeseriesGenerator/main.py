import tensorflow as tf
keras = tf.compat.v1.keras
Sequence = keras.utils.Sequence
import numpy as np

class MultiInputTimeseriesGenerator(Sequence):

  def __init__(self, data, targets, length,ptotal,batch_size,sampling_rate=1, start_index=0,end_index=None,same=0):

          if len(data) != len(targets):
              raise ValueError('Data and targets have to be' +' of same length. ' 'Data length is {}'.format(len(data)) + ' while target length is {}'.format(len(targets)))
          self.ptotal=ptotal
          self.data = data
          self.targets = targets
          self.length = length
          self.sampling_rate = sampling_rate
          self.start_index = start_index + length
          if end_index is None:
              end_index = len(data) - 1
          self.end_index = end_index
          self.batch_size = batch_size
          self.same = same
          self.max = int(np.ceil((len(self.data) - (self.length-same)*(len(self.data)//self.ptotal))/self.batch_size))

          if self.start_index > self.end_index:
              raise ValueError('`start_index+length=%i > end_index=%i` ''is disallowed, as no part of the sequence ' 'would be left to be used as current step.' % (self.start_index, self.end_index))

  def __len__(self):
      return self.max
  

  def __getitem__(self, index):

      # _i = (index + ((index)//(self.ptotal-self.length+1))*(self.length-1))
      # i = self.start_index + self.batch_size * index
      # rows = np.arange(i, min(i + self.batch_size , self.end_index + 1))
      # print(i, rows)

      st = self.ptotal * ((index*self.batch_size)//(self.ptotal - self.length + 1)) + self.length - 1 + ((index*self.batch_size) % (self.ptotal - self.length + 1))
      cmps = int(np.ceil(self.batch_size/(self.ptotal - self.length + 1))) + 1
      en = min(st + (self.ptotal * cmps), len(self.data))
      rows = np.arange(st, en)
      rows = rows[rows%self.ptotal >= (self.length - (self.same==1))]
      rows = rows[:min(len(rows), self.batch_size)]
      rows+=self.same
      # rows=np.asarray(rows).astype("int32")
      

      samples = np.array([self.data[row - self.length:row:self.sampling_rate]for row in rows])
      targets = np.array([self.targets[row-self.same] for row in rows])

      return samples, targets

  def __next__(self):
        if self.n >= self.max:
           self.n = 0
        result = self.__getitem__(self.n)
        self.n += 1
        return result



