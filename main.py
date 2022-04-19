import json
import numpy

class TheMatrixHash:
    def __init__(self):

        self.sample = '\u2636\u2635'

    def vShift(self, matrix_=list, shift=None, column=None) -> list:
        randomPinLock = []
        randomPinLock_ = []
        numberList = []

        shape = numpy.shape(matrix_)

        if shape[1]:
            for numberlist in numpy.column_stack(matrix_):
                for nums in numberlist:
                    numberList.append(nums)
                randomPinLock_.append(numberList[:shape[1]:])
                del numberList[:shape[1]:]

            else:
                shift_ = shift
                randomPinLock_[column - 1] = randomPinLock_[column - 1][shift_:] + randomPinLock_[column - 1][:shift_]
                for numberlist in randomPinLock_:
                    randomPinLock.append(numberlist)

            numberList.clear()
            randomPinLock_.clear()

            for numberlist in numpy.column_stack(randomPinLock):
                for nums in numberlist:
                    numberList.append(nums)
                randomPinLock_.append(numberList[:shape[1]:])
                del numberList[:shape[1]:]

            return randomPinLock_

    def hShift(self, matrix_=list, shift=int, row=int):

        randomPinLock = []
        matrix_[row - 1] = matrix_[row - 1][shift:] + matrix_[row - 1][:shift]
        for numberlist in matrix_:
            randomPinLock.append(numberlist)

        return randomPinLock

    def createMatrixHash(self, passwd=str):
        bta = bytearray(passwd, 'utf-8')
        mv = list(memoryview(bta))
       

        matrix = []
        hashed = []
        for n in range(len(passwd)):
            stde = int(numpy.median(mv[n])) + int(numpy.mean(mv[n])) / int(numpy.sum(mv))

            matrix.append([i+stde for i in range(1, len(passwd) + 1)])


        for i in range(len(mv)):
            num = mv[i]
            while num >= len(passwd):
                num -= 3
                continue
            if num < len(passwd):
                shiftH = self.hShift(matrix, num+1, i + 1)
                matrix[:] = shiftH
                continue


        for i in range(len(mv)):
            num = mv[i]
            while num >= len(passwd):
                num -= 4
                continue
            if num < len(passwd):
                shiftV = self.vShift(matrix, -num+1, i + 1)
                matrix[:] = shiftV
                continue


        for i in range(len(matrix)):
            numberlist = [n+mv[i-1]+len(str(mv[i-1])) for n in matrix[i]]
            hashed.append(numberlist)

        #print(numpy.vstack(hashed))
        hash_matrix = []
        for numberlist in hashed:
            numberlist[:] = [' '.join(format(ord(b), 'b') .replace('0', self.sample[0]).replace('1', self.sample[1]) for b in str(i)) for i in numberlist]
            hash_matrix.append(numberlist)



        return hash_matrix

### You can delete section 2#

#####################################################################
########################### SECTION 2 ###############################
while True:
    try:
        tmh = TheMatrixHash()
        user = input('password: ')
        matrix_hash = tmh.createMatrixHash(passwd=user)
        


        with open('matrixHash.json', 'r') as f:
            p = json.load(f)


            if p == matrix_hash:
                print('ACCESS: ', True)
            else:
                print('ACCESS: ', False)

        print('\n\n', numpy.vstack(matrix_hash), '\n\n')
    except:
        pass
######################################################################
