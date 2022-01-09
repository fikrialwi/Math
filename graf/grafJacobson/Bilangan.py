
class Bilangan:
    def __init__(self, number):
        self.number = number
    def uniq(self, set):
        res =[]
        [res.append(i) for i in set if i not in res]
        return res
    def intersect(self, setA, setB):
        set = []
        [set.append(a) for a in setA if a in setB]            
        [set.append(b) for b in setB if b in setA]
        res =[]
        [res.append(i) for i in set if i not in res]
        return res
    def subset(self, setA, setB):
        k = 0
        for i in setA:
            if i in setB:
                k += 1
        if k == len(setA):
            return True
        else:
            return False
    def identity(self):
        if self.operation == "*":
            identity = [1]
        elif self.operation == "+":
            identity = [0]
        return identity
    def show(self, matrix):
        string = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                string += ' | '+ str(matrix[i][j]) +' | '
                if i == len(matrix[i]):
                    string += '\n'
        print(string)


class Prime(Bilangan):
    def __init__(self, number):
        super().__init__(number)
    def isPrime(self, number = None):
        if number == None:
            number = self.number
        if number < 2:
            return False
        for i in range(2,number):
            if number%i == 0:
                return False
        return True
    def primeInterval(self, numberAwal = None, numberAkhir = None):
        prime = []
        if numberAwal == None:
            numberAwal = self.number
        if numberAkhir == None:
            numberAkhir = self.number
        for i in range(numberAwal, numberAkhir+1):
            if self.isPrime(i):
                prime.append(i)
        return prime

class Modulo(Bilangan):
    def __init__(self, number, operation):
        super().__init__(number)
        self.operation = operation
    def element(self):
        moduloZ_n = []
        for i in range(self.number):
            moduloZ_n.append(i)
        return moduloZ_n
    def generator(self, number):
        if self.operation == "*":
            gen = {1}
            for i in range(self.number):
                gen.add(number**i%self.number)
        elif self.operation == "+":
            gen = {0}
            for i in range(self.number):
                gen.add(number*i%self.number)
        gener = []
        for i in gen:
            gener.append(i)
        return gener
    
    def idealMax(self):
        set = []
        for i in self.element():
            if self.generator(i) != self.element():
                if self.generator(i) != self.identity():
                    set.append(self.generator(i))
        if len(set) == 0:
            set.append(self.identity())
            return set
        res = []
        [res.append(i) for i in set if i not in res]
        return res

    def unit(self):
        set = []
        for i in self.element():  
            for j in self.element():
                if i*j % self.number == 1:
                    set.append(i)
        return set
    def zeroDivisor(self):
        set = []
        for i in self.element():
            for j in self.element():
                if i != 0 or j != 0:
                    if i*j % self.number == 0:
                        set.append(i)
        return set 
    def cayley(self):
        row = []
        for i in self.element():
            col = []
            for j in self.element():
                if self.operation == '*':
                    e = (i*j)%self.number
                elif self.operation == '+':
                    e = (i+j)%self.number
                col.append(e)
            row.append(col)
        return row

class Jacobson(Modulo):
    def __init__(self, number, operation):
        super().__init__(number, operation)
    def element(self):
        return super().element()
    def idealMax(self):
        return super().idealMax()
    def intersect(self, setA, setB):
        return super().intersect(setA, setB)
    def jacobson(self):
        if len(self.idealMax()) == 0:
            return []
        if len(self.idealMax()) == 1:
            return [*self.idealMax()]
        irisan = self.intersect(self.idealMax()[0], self.idealMax()[1])
        for i in self.idealMax():
            temp = self.intersect(irisan, i)
            if len(temp) < len(irisan):
                irisan = [*temp]
        return irisan