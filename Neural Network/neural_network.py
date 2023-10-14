import math
import random
from copy import deepcopy
import pickle

clamp = lambda value, minv, maxv: max(min(value, maxv), minv)
remap = lambda value, min1, max1, min2, max2: min2 + (value - min1) * (max2 - min2) / (max1 - min1)

class NeuralNetwork():
    def sigmoid(x,deri=False):
        if deri==False:
            return 1/(1 + math.exp(-x))
        else:
            return NeuralNetwork.sigmoid(x)*(1-NeuralNetwork.sigmoid(x))

    def relu(x,deri=False):
        if deri==False:
            if x>0:
                return x
            else:
                return 0.01*x
        else:
            if x>0:
                return 1
            else:
                return 0.01

    def tan_inverse(x,deri=False):
        if deri==False:
            return 2*(math.atan(x)/math.pi)

        else:
            return 2/(math.pi*(1+pow(x,2)))


    def __init__(self,*args):
        if len(args) == 1:
            n = pickle.load(open(args[0],"rb"))
            self.Ninputs = n.Ninputs
            self.Nhidden1 = n.Nhidden1
            self.Nhidden2 = n.Nhidden2
            self.Nhidden3 = n.Nhidden3
            self.Nhidden4 = n.Nhidden4
            self.Nhidden5 = n.Nhidden5
            self.Noutputs = n.Noutputs
            self.lr = n.lr
            self.inputs = n.inputs
            self.outputs = n.outputs
            self.hiddens1 = n.hiddens1
            self.hiddens2 = n.hiddens2
            self.hiddens3 = n.hiddens3
            self.hiddens4 = n.hiddens4
            self.hiddens5 = n.hiddens5
            self.weights = n.weights
            return

        elif len(args) >= 3 and len(args) <= 8:
            if len(args) == 3:
                self.Ninputs = args[0]
                self.Nhidden1 = 0
                self.Nhidden2 = 0
                self.Nhidden3 = 0
                self.Nhidden4 = 0
                self.Nhidden5 = 0
                self.Noutputs = args[1]
                self.lr = args[2]
            if len(args) == 4:
                self.Ninputs = args[0]
                self.Nhidden1 = args[1]
                self.Nhidden2 = 0
                self.Nhidden3 = 0
                self.Nhidden4 = 0
                self.Nhidden5 = 0
                self.Noutputs = args[2]
                self.lr = args[3]
            if len(args) == 5:
                self.Ninputs = args[0]
                self.Nhidden1 = args[1]
                self.Nhidden2 = args[2]
                self.Nhidden3 = 0
                self.Nhidden4 = 0
                self.Nhidden5 = 0
                self.Noutputs = args[3]
                self.lr = args[4]
            if len(args) == 6:
                self.Ninputs = args[0]
                self.Nhidden1 = args[1]
                self.Nhidden2 = args[2]
                self.Nhidden3 = args[3]
                self.Nhidden4 = 0
                self.Nhidden5 = 0
                self.Noutputs = args[4]
                self.lr = args[5]
            if len(args) == 7:
                self.Ninputs = args[0]
                self.Nhidden1 = args[1]
                self.Nhidden2 = args[2]
                self.Nhidden3 = args[3]
                self.Nhidden4 = args[4]
                self.Nhidden5 = 0
                self.Noutputs = args[5]
                self.lr = args[6]
            if len(args) == 8:
                self.Ninputs = args[0]
                self.Nhidden1 = args[1]
                self.Nhidden2 = args[2]
                self.Nhidden3 = args[3]
                self.Nhidden4 = args[4]
                self.Nhidden5 = args[5]
                self.Noutputs = args[6]
                self.lr = args[7]

            for i in range(len(args)):
                if args[i]<=0:
                    raise Exception("parameters value wrong")
        else:
            raise Exception("parameters wrong")
        self.inputs = []
        self.outputs = []
        self.hiddens1 = []
        self.hiddens2 = []
        self.hiddens3 = []
        self.hiddens4 = []
        self.hiddens5 = []
        self.weights = {}

        for i in range(self.Ninputs):
            self.inputs.append(node(0))

        for i in range(self.Nhidden1):
            self.hiddens1.append(node(None))

        for i in range(self.Nhidden2):
            self.hiddens2.append(node(None))

        for i in range(self.Nhidden3):
            self.hiddens3.append(node(None))

        for i in range(self.Nhidden4):
            self.hiddens4.append(node(None))
        
        for i in range(self.Nhidden5):
            self.hiddens5.append(node(None))

        for i in range(self.Noutputs):
            self.outputs.append(node(None))
        
        for i in range(len(self.inputs)):

            if len(self.hiddens1)>0:

                for j in range(len(self.hiddens1)):
                    self.weights[self.inputs[i],self.hiddens1[j]] = random.uniform(-1,1)

            else:

                for j in range(len(self.outputs)):
                    self.weights[self.inputs[i],self.outputs[j]] = random.uniform(-1,1)


        for i in range(len(self.hiddens1)):

            if len(self.hiddens2)>0:

                for j in range(len(self.hiddens2)):
                    self.weights[self.hiddens1[i],self.hiddens2[j]] = random.uniform(-1,1)

            else:

                for j in range(len(self.outputs)):
                    self.weights[self.hiddens1[i],self.outputs[j]] = random.uniform(-1,1)


                
        for i in range(len(self.hiddens2)):

            if len(self.hiddens3)>0:

                for j in range(len(self.hiddens3)):
                    self.weights[self.hiddens2[i],self.hiddens3[j]] = random.uniform(-1,1)

            else:

                for j in range(len(self.outputs)):
                    self.weights[self.hiddens2[i],self.outputs[j]] = random.uniform(-1,1)

            

        for i in range(len(self.hiddens3)):

            if len(self.hiddens4)>0:

                for j in range(len(self.hiddens4)):
                    self.weights[self.hiddens3[i],self.hiddens4[j]] = random.uniform(-1,1)
                
            else:

                for j in range(len(self.outputs)):
                    self.weights[self.hiddens3[i],self.outputs[j]] = random.uniform(-1,1)


        for i in range(len(self.hiddens4)):

            if len(self.hiddens5)>0:

                for j in range(len(self.hiddens5)):
                    self.weights[self.hiddens4[i],self.hiddens5[j]] = random.uniform(-1,1)
            else:

                for j in range(len(self.outputs)):
                    self.weights[self.hiddens4[i],self.outputs[j]] = random.uniform(-1,1)


        for i in range(len(self.hiddens5)):

            for j in range(len(self.outputs)):
                self.weights[self.hiddens5[i],self.outputs[j]] = random.uniform(-1,1)

    def update(self):
        for i in range(len(self.hiddens1)):
            sum = self.hiddens1[i].bias
            
            for j in range(len(self.inputs)):
                sum += self.weights[self.inputs[j],self.hiddens1[i]] * self.inputs[j].value

            self.hiddens1[i].sum = sum
            self.hiddens1[i].value = NeuralNetwork.tan_inverse(sum)

        for i in range(len(self.hiddens2)):
            sum = self.hiddens2[i].bias

            for j in range(len(self.hiddens1)):
                sum += self.weights[self.hiddens1[j],self.hiddens2[i]] * self.hiddens1[j].value

            self.hiddens2[i].sum = sum
            self.hiddens2[i].value = NeuralNetwork.relu(sum)

        for i in range(len(self.hiddens3)):
            sum = self.hiddens3[i].bias

            for j in range(len(self.hiddens2)):
                sum += self.weights[self.hiddens2[j],self.hiddens3[i]] * self.hiddens2[j].value

            self.hiddens3[i].sum = sum
            self.hiddens3[i].value = NeuralNetwork.tan_inverse(sum)

        for i in range(len(self.hiddens4)):
            sum = self.hiddens4[i].bias

            for j in range(len(self.hiddens3)):
                sum += self.weights[self.hiddens3[j],self.hiddens4[i]] * self.hiddens3[j].value

            self.hiddens4[i].sum = sum
            self.hiddens4[i].value = NeuralNetwork.relu(sum)

        for i in range(len(self.hiddens5)):
            sum = self.hiddens5[i].bias

            for j in range(len(self.hiddens4)):
                sum += self.weights[self.hiddens4[j],self.hiddens5[i]] * self.hiddens4[j].value

            self.hiddens5[i].sum = sum
            self.hiddens5[i].value = NeuralNetwork.tan_inverse(sum)

        for i in range(len(self.outputs)):
            sum = self.outputs[i].bias

            if len(self.hiddens1)<1:

                for j in range(len(self.inputs)):
                    sum += self.weights[self.inputs[j],self.outputs[i]] * self.inputs[j].value

            elif len(self.hiddens2)<1:  

                for j in range(len(self.hiddens1)):
                    sum += self.weights[self.hiddens1[j],self.outputs[i]] * self.hiddens1[j].value

            elif len(self.hiddens3)<1:  

                for j in range(len(self.hiddens2)):
                    sum += self.weights[self.hiddens2[j],self.outputs[i]] * self.hiddens2[j].value

            elif len(self.hiddens4)<1:  

                for j in range(len(self.hiddens3)):
                    sum += self.weights[self.hiddens3[j],self.outputs[i]] * self.hiddens3[j].value

            elif len(self.hiddens5)<1:  

                for j in range(len(self.hiddens4)):
                    sum += self.weights[self.hiddens4[j],self.outputs[i]] * self.hiddens4[j].value

            else:

                for j in range(len(self.hiddens5)):
                    sum += self.weights[self.hiddens5[j],self.outputs[i]] * self.hiddens5[j].value

            self.outputs[i].sum = sum
            self.outputs[i].value = NeuralNetwork.sigmoid(sum)


    def train(self,inp,correctarr):
        self.input(inp)
        self.update()

        loss=self.loss(correctarr)

        sumh1=[0]*self.Nhidden1
        sumh2=[0]*self.Nhidden2
        sumh3=[0]*self.Nhidden3
        sumh4=[0]*self.Nhidden4
        sumh5=[0]*self.Nhidden5

        for i in range(self.Noutputs):

            bias=2*(self.outputs[i].value-correctarr[i])*NeuralNetwork.sigmoid(self.outputs[i].sum,True)*self.lr

            if len(self.hiddens5)>0:
            
                for j in range(self.Nhidden5):
                    weight=bias*self.hiddens5[j].value
                    h5=bias*self.weights[self.hiddens5[j],self.outputs[i]]
                    sumh5[j]+=h5 #store previous layer activation

                    self.weights[self.hiddens5[j],self.outputs[i]]-= weight #update weight

            elif len(self.hiddens4)>0:

                for j in range(self.Nhidden4):
                    weight=bias*self.hiddens4[j].value
                    h4=bias*self.weights[self.hiddens4[j],self.outputs[i]]
                    sumh4[j]+=h4 #store previous layer activation

                    self.weights[self.hiddens4[j],self.outputs[i]]-= weight #update weight

            elif len(self.hiddens3)> 0:

                for j in range(self.Nhidden3):
                    weight=bias*self.hiddens3[j].value
                    h3=bias*self.weights[self.hiddens3[j],self.outputs[i]]
                    sumh3[j]+=h3 #store previous layer activation

                    self.weights[self.hiddens3[j],self.outputs[i]]-= weight #update weight

            elif len(self.hiddens2)> 0:

                for j in range(self.Nhidden2):
                    weight=bias*self.hiddens2[j].value
                    h2=bias*self.weights[self.hiddens2[j],self.outputs[i]]
                    sumh2[j]+=h2 #store previous layer activation

                    self.weights[self.hiddens2[j],self.outputs[i]]-= weight #update weight

            elif len(self.hiddens1)> 0:

                for j in range(self.Nhidden1):
                    weight=bias*self.hiddens1[j].value
                    h1=bias*self.weights[self.hiddens1[j],self.outputs[i]]
                    sumh1[j]+=h1 #store previous layer activation

                    self.weights[self.hiddens1[j],self.outputs[i]]-= weight #update weight

            else:

                for j in range(self.Ninputs):
                    weight=bias*self.inputs[j].value

                    self.weights[self.inputs[j],self.outputs[i]]-= weight #update weight

            self.outputs[i].bias-=bias


        for i in range(self.Nhidden5):

            bias=sumh5[i]*self.lr*NeuralNetwork.tan_inverse(self.hiddens5[i].sum,True)

            for j in range(self.Nhidden4):
                weight=bias*self.hiddens4[j].value
                h4=bias*self.weights[self.hiddens4[j],self.hiddens5[i]]
                sumh4[j]+=h4 #store previous layer activation

                self.weights[self.hiddens4[j],self.hiddens5[i]]-= weight #update weight

            self.hiddens5[i].bias-=bias


        for i in range(self.Nhidden4):

            bias=sumh4[i]*self.lr*NeuralNetwork.relu(self.hiddens4[i].sum,True)

            for j in range(self.Nhidden3):
                weight=bias*self.hiddens3[j].value
                h3=bias*self.weights[self.hiddens3[j],self.hiddens4[i]]
                sumh3[j]+=h3 #store previous layer activation

                self.weights[self.hiddens3[j],self.hiddens4[i]]-= weight #update weight

            self.hiddens4[i].bias-=bias


        for i in range(self.Nhidden3):

            bias=sumh3[i]*self.lr*NeuralNetwork.tan_inverse(self.hiddens3[i].sum,True)

            for j in range(self.Nhidden2):
                weight=bias*self.hiddens2[j].value
                h2=bias*self.weights[self.hiddens2[j],self.hiddens3[i]]
                sumh2[j]+=h2 #store previous layer activation

                self.weights[self.hiddens2[j],self.hiddens3[i]]-= weight #update weight

            self.hiddens3[i].bias-=bias


        for i in range(self.Nhidden2):

            bias=sumh2[i]*self.lr*NeuralNetwork.relu(self.hiddens2[i].sum,True)

            for j in range(self.Nhidden1):
                weight=bias*self.hiddens1[j].value
                h1=bias*self.weights[self.hiddens1[j],self.hiddens2[i]]
                sumh1[j]+=h1 #store previous layer activation

                self.weights[self.hiddens1[j],self.hiddens2[i]]-= weight #update weight

            self.hiddens2[i].bias-=bias

        
        for i in range(self.Nhidden1):

            bias=sumh1[i]*self.lr*NeuralNetwork.tan_inverse(self.hiddens1[i].sum,True)

            for j in range(self.Ninputs):
                weight=bias*self.inputs[j].value

                self.weights[self.inputs[j],self.hiddens1[i]]-= weight #update weight

            self.hiddens1[i].bias-=bias

        
        return loss


    def loss(self,correctarr):
        if len(self.outputs)!=len(correctarr):
            raise Exception("no# of output in neutral network and no# of output in correct array not equal")
        loss=0
        for i in range(len(correctarr)):
            loss+=pow(self.outputs[i].value-correctarr[i],2)

        return loss


    def guess(self):
        arr=[]
        for out in self.outputs:
            arr.append(out.value)
        return arr

    def input(self,arr):
        if len(arr)!=len(self.inputs):
            raise Exception("no# of inputs received and no# of inputs in neutral network not equal")
    
        for i in range(len(arr)):
            if arr[i]<0 or arr[i]>1:
                raise Exception("Input not normalised")
            self.inputs[i].value = arr[i]

    def mutate(self,rate=1):
        for k in self.weights:
            if random.uniform(0,1) <= rate/100:
                n= random.uniform(0,1)
                if n <= 25/100:
                    self.weights[k]= random.uniform(-1,1)
                elif n <= 50/100:
                    self.weights[k]*= random.uniform(0.5,1.5)
                elif n <= 75/100:
                    self.weights[k]+= random.uniform(-1,1)
                else:
                    self.weights[k]*=-1

    def crossbreed(self,n2):
        n3=n2.copy()
        for i in range(self.Noutputs):

            if self.Nhidden5>0:

                for j in range(self.Nhidden5):
                    if random.uniform(0,1) <= 50/100:
                        n3.weights[n3.hiddens5[j],n3.outputs[i]]=self.weights[self.hiddens5[j],self.outputs[i]]

            elif self.Nhidden4>0:

                for j in range(self.Nhidden4):
                    if random.uniform(0,1) <= 50/100:
                        n3.weights[n3.hiddens4[j],n3.outputs[i]]=self.weights[self.hiddens4[j],self.outputs[i]]

            elif self.Nhidden3>0:

                for j in range(self.Nhidden3):
                    if random.uniform(0,1) <= 50/100:
                        n3.weights[n3.hiddens3[j],n3.outputs[i]]=self.weights[self.hiddens3[j],self.outputs[i]]

            elif self.Nhidden2>0:

                for j in range(self.Nhidden2):
                    if random.uniform(0,1) <= 50/100:
                        n3.weights[n3.hiddens2[j],n3.outputs[i]]=self.weights[self.hiddens2[j],self.outputs[i]]

            elif self.Nhidden1>0:

                for j in range(self.Nhidden1):
                    if random.uniform(0,1) <= 50/100:
                        n3.weights[n3.hiddens1[j],n3.outputs[i]]=self.weights[self.hiddens1[j],self.outputs[i]]

            else:

                for j in range(self.Ninputs):
                    if random.uniform(0,1) <= 50/100:
                        n3.weights[n3.inputs[j],n3.outputs[i]]=self.weights[self.inputs[j],self.outputs[i]]

        for i in range(self.Nhidden5):

            for j in range(self.Nhidden4):
                if random.uniform(0,1) <= 50/100:
                    n3.weights[n3.hiddens4[j],n3.hiddens5[i]]=self.weights[self.hiddens4[j],hiddens5[i]]

        for i in range(self.Nhidden4):

            for j in range(self.Nhidden3):
                if random.uniform(0,1) <= 50/100:
                    n3.weights[n3.hiddens3[j],n3.hiddens4[i]]=self.weights[self.hiddens3[j],self.hiddens4[i]]


        for i in range(self.Nhidden3):

            for j in range(self.Nhidden2):
                if random.uniform(0,1) <= 50/100:
                    n3.weights[n3.hiddens2[j],n3.hiddens3[i]]=self.weights[self.hiddens2[j],self.hiddens3[i]]


        for i in range(self.Nhidden2):

            for j in range(self.Nhidden1):
                if random.uniform(0,1) <= 50/100:
                    n3.weights[n3.hiddens1[j],n3.hiddens2[i]]=self.weights[self.hiddens1[j],self.hiddens2[i]]


        for i in range(self.Nhidden1):

            for j in range(self.Ninputs):
                if random.uniform(0,1) <= 50/100:
                    n3.weights[n3.inputs[j],n3.hiddens1[i]]=self.weights[self.inputs[j],self.hiddens1[i]]


        return n3

    def copy(self):
        return deepcopy(self)

    def save(self,file = 'obj'):
        if file == 'obj':
            n = 0
            while os.path.isfile(file+str(n)):
                n+= 1
            pickle.dump(self,open(file+str(n),'wb'))
        else:
            pickle.dump(self,open(file,'wb'))


class node():
    def __init__(self,value,sum=0):
        self.value = value
        self.sum=sum
        self.bias=0
