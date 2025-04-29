# Relatório: SingleClient x MultiClient

## Alunos
- Ruan Vieira - 202240602029
- Wesley Costa -  202240602036

## Professor
- Warley - Unifesspa

## Configuração de Teste:
- 1 único cliente x 10 clientes simultâneos
- 100 requisições
- Máquina: i3 com 10GB de RAM

## Resultados: [SigleClient - MultiClient]

| Servidor         | Status                | Tempo (s)         | CPU (%)         | Memória (MB)     |
|------------------|------------------------|-------------------|-----------------|------------------|
| OneShotServer    | Sucesso - Falhou        | 1.8s - 1.8s       | 1% - 2%         | 9.6MB - 11MB     |
| ThreadedServer   | Sucesso - Sucesso       | 1.6s - 3.2s       | 1.9% - 13%      | 10MB - 11MB      |
| ThreadPoolServer | Sucesso - Sucesso       | 16.3s - 21.5s     | 1% - 6%         | 11MB - 11MB      |


## Video das respostas as perguntas da atividade

https://github.com/user-attachments/assets/02a45474-3780-4e91-9208-607cbb6d6f04

## Video de demostração de execulção dos servidores
https://github.com/user-attachments/assets/e65e685a-5136-4954-863b-7ddab1f41eed
