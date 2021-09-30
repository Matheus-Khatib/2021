def ordena(lista):
    for i in range(len(lista)):
        num_minimo = lista[i]
        for j in range(i+1, len(lista)):
            if lista[j]<num_minimo:
                num_minimo=lista[j]
        ind = lista.index(num_minimo)
        lista[i],lista[ind]=lista[ind],lista[i]
    return lista
 

   
  
   
        
