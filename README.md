# iiaTrab1
trabalho 1 iia, travessia de grafos


Pseudo Código UCS:
```
caminhos <- dicionario de tuplas [cidade : (custo, caminho: [])]

custo(cidade, caminho) <- retorna o custo total de se fazer o caminho e a partir do caminho feito trafegar para a cidade


UCS(grafo, atual, destino, visitados = []) -> solução {
    visitados.append(atual)
    se custo(visitados) < caminhos[atual].custo =  {
        caminhos[atual].custo = custo(atual, visitados)
        caminhos[atual].caminho = visitados.copia()
    }
    para vizinho em node.vizinhos() {
        se !visitados.contains(vizinho) {
            UCS(grafo, vizinho, destino, visitados.copia())
        }
    }
}

dado um grafo, um nó inicial, um destino -> solução se houver, em caso de falha o caminho ficará vazio;
vale notar que caminhos deve ser inicializado com custos infinitos para que ao trafegar pelo grafo os valores sejam atualizados, se possível.
```

Pesudo Código Greedy:
```
custo_linear = [cidade : distancia] <- dicionario que retorna a distancia em linha reta da cidade ao destino
visitados = [] <- lista de nodes visitados

Greedy(grafo, custo_linear, atual, destino, caminho = []) -> solução {
    se atual not in visitados{
        visitados.append(atual)
    }
    sort(atual.vizinhos(), custo_linear[vizinho]) <- organiza os vizinhos do mais próximo linearmente ao destino.
    se atual == destino {
        caminho.append_front(atual)
        return 1
    }
    para vizinho em atual.vizinhos() {
        se vizinho not in visitados {
           se Greedy(grafo, custo_linear, vizinho, destino, caminho) == 1 {
               caminho.append_front(atual)
               return 1
           }
        }
    }
}

dado um grafo e uma tabela com informação extra desejável, priorizar nodes mais próximos do destino para a busca em profundidade, ao atingir destino inserir na lista (na frente) e sinalizar para os nodes anteriores fazerem o mesmo.



``` 

Pesudo Código A*:
```
custo_linear = [cidade : distancia] <- dicionario que retorna a distancia em linha reta da cidade ao destino
visitados = [] <- lista de nodes visitados

Astar(grafo, custo_linear, atual, destino, caminho = []) -> solução {
    se atual not in visitados{
        visitados.append(atual)
    }
    custos = [cidade:custo]
    para vizinho in atual.vizinhos() {
        custos.append(vizinho,custo_linear[vizinho] + grafo[atual][vizinho]) <- considerar o custo para travessia ao vizinho além da distancia linear
    }
    sort(custos) <- organiza os vizinhos em ordem crescente (menor custo primeiro).
    
    se atual == destino {
        caminho.append_front(atual)
        return 1
    }
    para vizinho em atual.vizinhos() {
        se vizinho not in visitados {
           se Astar(grafo, custo_linear, vizinho, destino, caminho) == 1 {
               caminho.append_front(atual)
               return 1
           }
        }
    }
}

dado um grafo e uma tabela com informação extra desejável, priorizar nodes mais próximos do destino para a busca em profundidade, ao atingir destino inserir na lista (na frente) e sinalizar para os nodes anteriores fazerem o mesmo.

``` 
