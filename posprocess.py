import preprocess as prp
import math as m

def getNearestCentroid( users , clusters , treino ):
    maior = 0
    result = 0

    for cluster in clusters:
        c = prp.cosine( users[cluster] , treino)
        if(c > maior):
            maior = c
            result = cluster

    return users[result]


def calculateRMSE( real , estimated):
    result = 0
    n = len(real)

    for r , e in list( zip( real , estimated)):
        x = (r - e)**2
        result += x
    
    
    result = result / n
    return m.sqrt(result)

def getClusterHash( file_name):
    clusterHash = dict({})

    arq = open(file_name)

    arq = arq.readlines()

    for line in arq:
        line = line.strip("\n").split()
        id = int( line[0])
        cluster = int( line[1])
        
        if( cluster in clusterHash):
            clusterHash[cluster].append( id )
        else:
            clusterHash[cluster] = [id]
    
    return clusterHash
        

users = prp.getArq("treino.dat") 
treinos = prp.getArq("teste.dat")

apHash = getClusterHash("cluster.dat")
kmHash = getClusterHash("clusterkm.dat")

reals = []
estimateds = []

# print( len(apHash.keys()))
# for treino in treinos:
#     centroid = getNearestCentroid( users , apHash.keys() , treino)
#     for t_rat , c_rat in list( zip( treino , centroid )):
#         reals.append( t_rat)
#         estimateds.append( c_rat )

# print( "Affinity Propagation RMSE: " , calculateRMSE( reals , estimateds))

reals = []
estimateds = []


for treino in treinos:
    centroid = getNearestCentroid( users , kmHash.keys() , treino)
    for t_rat , c_rat in list( zip( treino , centroid )):
        reals.append( t_rat)
        estimateds.append( c_rat )



print( "K-Means RMSE: " , calculateRMSE( reals , estimateds))




        

for t in treino:
    centroid = ObterCentroidMaisProximo()
    for f in filmes:
        NotaUsuarioFilme = Nota( centroid , filme)

    
    


    


