# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:10:43 2018

@author: Administrator
"""

#!/usr/bin/env python

net_struct = {'alexnet': {'net':[[11,4,0],[3,2,0],[5,1,2],[3,2,0],[3,1,1],[3,1,1],[3,1,1],[3,2,0]],
                   'name':['conv1','pool1','conv2','pool2','conv3','conv4','conv5','pool5']},
       'bonnet': {'net':[[5,1,2],[5,1,2],[5,1,2],[5,1,2],[2,2,0],[5,1,2],[5,1,2],[5,1,2],[2,2,0],[5,1,2],[5,1,2],[5,1,2],
                        [2,2,0],[5,1,2],[5,1,2],[5,1,2],[2,2,0]],
                 'name':['conv1_0','conv1_1','conv1_2','conv1_3','pool1','conv2_1','conv2_2','conv2_3','pool2','conv3_1','conv3_2',
                         'conv3_3', 'pool3','conv4_1','conv4_2','conv4_3','pool4','conv5_1','conv5_2','conv5_3','pool5']},
       'zf-5':{'net': [[7,2,3],[3,2,1],[5,2,2],[3,2,1],[3,1,1],[3,1,1],[3,1,1]],
               'name': ['conv1','pool1','conv2','pool2','conv3','conv4','conv5']}}

imsize_w = 512
imsize_h = 384

def outFromIn(w, h, net, layernum):
    totstride = 1
    insize_w = w
    insize_h = h
    for layer in range(layernum):
        fsize, stride, pad = net[layer]
        outsize_w = (insize_w - fsize + 2*pad) / stride + 1
        outsize_h = (insize_h - fsize + 2*pad) / stride + 1
        insize_w = outsize_w
        insize_h = outsize_h
        totstride = totstride * stride
    return outsize_w, outsize_h , totstride

def inFromOut(net, layernum):
    RF = 1
    for layer in reversed(range(layernum)):
        fsize, stride, pad = net[layer]
        RF = ((RF -1)* stride) + fsize
    return RF

if __name__ == '__main__':
    print "layer output sizes given image = %dx%d" % (imsize_w, imsize_h)
    
    for net in net_struct.keys():
        print '************net structrue name is %s**************'% net
        for i in range(len(net_struct[net]['net'])):
            p = outFromIn(imsize_w, imsize_h, net_struct[net]['net'], i+1)
            #print p
            rf = inFromOut(net_struct[net]['net'], i+1)
            print "Layer Name = %s, Output size = %3d*%3d, Stride = % 3d, RF size = %3d" % (net_struct[net]['name'][i], p[0],p[1], p[2], rf)