# Python Technical Challenge


## Descrição da solução 1

Foi criado um método get_topN_open_contracts que recebe uma lista com todos os contratos abertos, uma segunda lista que contém os contratos que já foram renegociados e o valor top_n.

Nesse método, foquei em tentar ser o mais performático possível, transformando a lista de contratos em um set do Python, pois um set tem a vantagem de ser implementado no Python como uma tabela hash, sendo assim, suas operações de inserção, exclusão e busca tem um tempo constate em média, tornando assim em um algoritmo de tempo de execução O(1) em média, sendo assim, muito mais rápido na busca que uma lista que possui uma execução O(n) na média.

Após essa conversão, percorro o conjunto usando compressão de lista, onde eu percorro todo meu conjunto procurando por ids que não estejam presentes na lista de contratos renegociados, dessa maneira eu removo todos os ids renegociados na lista resultante.

Após isso utilizo o método sort para ordenar o meu conjunto, para isso utilizo um método lambda function que percorre todo o conjunto e com base nos valores de contract.debt os ordena em ordem decrescente.

Por fim, com o conjunto devidamente ordenado, percorro o meu conjunto novamente usando um compressor de lista selecionando os maiores devedores até chegar em top_n e retorno os valores.

Exemplo para testes:
```python
if __name__ == "__main__":
    contracts = [
        Contract(1, 5),
        Contract(2, 5),
        Contract(3, 5),
        Contract(4, 5),
        Contract(5, 5),
    ]
    renegotiated = [3]
    top_n = 3

    actual_open_contracts = Contracts().get_top_N_open_contracts(
        contracts, renegotiated, top_n
    )

    expected_open_contracts = [1, 2, 4]
    print(actual_open_contracts)
    assert expected_open_contracts == actual_open_contracts
```


## Descrição da solução 2

Foi criado um método combine_orders que recebe uma lista de valores que devem ser feito as entregas e o valor máximo que pode ser levado em cada entrega, tendo em vista que podem ser feitas apenas 2 entregas por viagem no máximo, foi criado o algoritmo abaixo.

Primeiramente ordeno a lista de valores de cada entrega, em ordem decrescente, crio uma variável para marcar o número de viagens, iniciando em 0, um ponteiro para demarcar o inicio da lista(start) e um ponteiro para demarcar o final da lista(end).

Após isso faço um laco com while, enquanto start for menor ou igual a end, dentro das iterações desse laço tento mesclar a viagem de maior valor com a viagem de menor valor, caso eu consiga, incremento o número de viagens, incremento o start e decremento o end, caso não dê para mesclar, apenas incremento o número de viagens e o start, faço isso até terminar toda a lista.

Ao final, tenho o valor de viagens que vão ser feitas e retorno o mesmo.

Exemplo para testes:
```python
if __name__ == "__main__":
    orders = [10, 20, 60]
    n_max = 100
    expected_orders = 1

    how_many = Orders().combine_orders(orders, n_max)
    print(how_many)

    assert how_many == expected_orders
```


## Extra
Pensando na solução 1, fiz uma segunda opção, onde utilio o Factory Method para criar as instâncias de classes de Contract, a lógico é praticamente a mesma, mudando apenas que não utilizo o set por uma particularidade que ele só aceita objetos diferentes.

Exemplo para testes:
```python
if __name__ == "__main__":
    contracts = Contracts()
    contracts.add_contract(1, 5)
    contracts.add_contract(2, 5)
    contracts.add_contract(3, 5)
    contracts.add_contract(4, 5)
    contracts.add_contract(5, 5)

    renegotiated = [3]
    top_n = 3

    actual_open_contracts = contracts.get_top_N_open_contracts(renegotiated, top_n)

    expected_open_contracts = [1, 2, 4]
    print(actual_open_contracts)
    assert expected_open_contracts == actual_open_contracts
```

## Como rodar cada um dos testes

Question 1
```bash
python3 ./src/question1.py
```
Question 2
```bash
python3 ./src/question2.py
```
Question 1 extra
```bash
python3 ./src/question1_extra.py
```