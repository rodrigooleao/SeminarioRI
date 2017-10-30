import preprocess as prp

def getNearestCentroid( users , clusters , treino ):
    maior = 0
    result = 0

    for cluster in clusters:
        c = prp.cosine( users[cluster] , treino)
        if(c > maior):
            maior = c
            result = cluster

    return result



clusterHash = dict({})

arq = open("cluster.dat")

arq = arq.readlines()

for line in arq:
    line = line.strip("\n").split()
    id = int( line[0])
    cluster = int( line[1])
    
    if( cluster in clusterHash):
        clusterHash[cluster].append( id )
    else:
        clusterHash[cluster] = [id]
    

users = prp.getArq("teste.dat") 
treinos = prp.getArq("treino.dat")

reals = []
estimateds = []

for treino in treinos:
    centroid = getNearestCentroid( users , clusterHash.keys() , treino)
    for t_rat , c_rat in list( zip( treino , centroid )):
        reals.append( t_rat)
        estimateds.append( c_rat )


        


    
    


    


