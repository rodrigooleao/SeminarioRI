import preprocess as prp
import posprocess as psp
import heapq
import random as rd

def getMovieInfo():
    movies = []
    arq = open("ml-latest-small/movies.csv")
    arq = arq.readlines()

    arq.remove( arq[0])
    i = 0
    for line in arq:
        line = line.strip("\n\r").split(",")
        line[0] = i
        line[2] = line[2].split("|")
        movies.append( line )
        # print( line )
        i+=1

    return movies

def getClusterMovies( cluster , apHash , users):
    u = apHash[cluster]
    users = [ users[x] for x in u]

    notas = []

    for i in range(9125):
        notas.append(0)

    for user in users:
        movs = list( enumerate(user))

        for movieId, nota in movs:
            notas[movieId] += nota

    
    heapMovies = []
    maior = notas[0]
    m = 0

    for i , nota in list(enumerate(notas)):
        if( len(heapMovies) < 20 ):
            heapq.heappush( heapMovies , ( nota , i))
        elif( nota > heapMovies[0][0]):
            heapq.heappushpop( heapMovies , ( nota , i))

    result = []
    while heapMovies:
        result = [heapq.heappop( heapMovies)[1]] + result

    return result

if( __name__ == "__main__"):
    moviesInfo = getMovieInfo()
    users = prp.getArq("treino.dat")
    teste = prp.getArq("teste.dat")
    apHash = psp.getClusterHash("cluster.dat")

    id = rd.randint(0 , 71)
    t = teste[id]

    i = 0
    # for cluster in apHash.keys():
    #     x = getClusterMovies( cluster , apHash , users)
    #     print("Os filmes preferido do cluster: " + str(i) + " sao:\n ")
    #     j = 1
    #     for id in x:
    #         print(j , " - " , moviesInfo[id][1])
    #         j += 1

    #     i += 1

    
    c = psp.getNearestCentroidId( users , apHash.keys() , t )
    x = getClusterMovies( c , apHash , users)

    print(" *** Teste " + str(id) + " identificado como pertencente ao cluster " + str(c) + " ***\n\n")
    print("\nFilmes do cluster do usuário")
    print(c)
    j = 1
    for id in x:
        print(j , " - " , moviesInfo[id][1])
        j += 1

    t = [(id) for (id , nota) in list(enumerate(t)) if(nota != 0)]
    
    print("\n\n\nFilmes que o usuário assistiu")
        
    print([moviesInfo[id][1] for id in t])

    result = [k for k in x if( k in t)] 
    print("\n\n\nFilmes que o usuário assistiu e estavam no cluster dele")
    for id  in result:
        print( moviesInfo[id][1] )

    rec = [k for k in x if ( not ( k in t))]
    print("\n\n\nRecomendações ( Filmes do cluster que o usuário ainda não assistiu )")
    for id  in rec:
        print( moviesInfo[id][1] )


    # t = [0 for x in range(9125)]
    # ass = []

    # c = 0
    # while( c < 10 ):
    #     movieId = rd.randint(0 , 9125)
    #     print("Qual nota vc daria para o filme: " + moviesInfo[movieId][1])
    #     x = int(input())
    #     t[movieId] = x
    #     if(x != 0 ):
    #         ass.append(x)
    #         c+=1
    
    # c = psp.getNearestCentroidId( users , apHash.keys() , t)
    # m = getClusterMovies( c , apHash , users)

    # rec = [k for k in m if ( not ( k in ass))]
    # print("\n\n\nRecomendações:")
    # for id  in rec:
    #     print( moviesInfo[id][1] )


