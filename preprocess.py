import math as m

def norma( vec ):
   result = 0

   for x in vec:
       result += x**2

   return m.sqrt( result )

def cosine( vec1 , vec2 ):
   num = 0

   for x,y in zip( vec1 , vec2):
       num += ( x * y)
  
   den = 0

   den = norma( vec1 ) * norma( vec2 )

   return num / den

def NegEuclidean( vec1 , vec2):
   result = 0

   for x,y in zip(vec1 , vec2):
       result += ( x - y ) ** 2
  
   return m.sqrt( result)

def getArq( file_name ):
    arq = open(file_name)
    file = arq.readlines()

    users = []
    for linha in file:
        users.append( [int(x) for x in linha.strip("\n").split()])

    return users



if( __name__ == "__main__"):
    users = getUsers( "treino.dat")
    for x in range( len( users)):
        for y in range( len( users)):
            if( x != y):
                print( str(x) + " "+  str(y) +" "+ str(cosine( users[x] , users[y])))
    print( len(users))    
