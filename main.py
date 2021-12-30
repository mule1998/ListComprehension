class ListComprehension:

    def list_1(self,n):
        '''printing numbers in multiple of 10'''
        number=[i*10 for i in range(1,n+1)]
        print (number)

comp=ListComprehension()
comp.list_1(10)
