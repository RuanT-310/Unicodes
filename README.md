# Nomeação e Sincronizacão de Tempo
## Alunos
- Ruan Vieira
- Nicolas
- Noé Luiz

## Professor
- Warley - Unifesspa - Sistemas Distribuidos

## Resumo das atividades feitas
1. Criação da Rede Docker: Uma rede Docker com subnet 172.21.0.0/16 foi estabelecida para isolamento e controle dos IPs dos nós.
```
docker network create --subnet=172.21.0.0/16 dist-sys-net
```
2. Containers Docker padrão não rodam systemd como seu processo de inicialização (PID 1). Isso significa que comandos como systemctl start my-service não funcionam como fariam em uma VM completa. Por isso utilizamos um script externo ao container (start_etcd.sh), que realiza as seguintes tarefas.
    - Instalação de pré-requisitos (wget, curl, iputils-ping, python3, python3-pip).
    - Download, extração e instalação dos binários do etcd (v3.5.6) em /usr/local/bin/.
    - Criação do diretório de dados para o etcd (/var/lib/etcd).
4. Preparação dos Containers: Cada container (ubuntu:22.04) foi configurado com o script de inicialização (start_etcd.sh)
3. Inicialização do processo etcd em foreground
```
docker run -d --name mx-nodel --ip 172.21.0.10 --network dist-sys-net `
  -e NODE_NAME=mx-nodel `
  -v "${PWD}/start_etcd.sh:/start_etcd.sh" `
  ubuntu:22.04 /start_etcd.sh
```

# Demostração da atividade pedidas
https://github.com/user-attachments/assets/fb28969a-4209-48a7-8ba1-de7ece6af75a

# Respostas da atividade
1. Tempo medio para eleição do lider
```
2025-06-16 20:35:43 {"level":"warn","ts":"2025-06-16T23:35:43.146Z","caller":"rafthttp/stream.go:421","msg":"lost TCP streaming connection with remote peer","stream-reader-type":"stream MsgApp v2","local-member-id":"74ac2a1902010f1d","remote-peer-id":"3a4ec917aa24ee62","error":"unexpected EOF"}
...
2025-06-16 20:35:44 {"level":"info","ts":"2025-06-16T23:35:44.921Z","logger":"raft","caller":"etcdserver/zap_raft.go:77","msg":"raft.node: 74ac2a1902010f1d elected leader 74ac2a1902010f1d at term 12"}
```

2. ### Conflitos no etcd:
O etcd resolve conflitos de atualização simultânea de uma chave usando o algoritmo de consenso Raft. Todas as escritas são processadas através de um líder único que as ordena, adiciona ao log e replica para a maioria dos seguidores. Apenas após a confirmação pela maioria, a operação é commitada e aplicada ao banco de dados, garantindo que a última operação commitada prevaleça.

3. ?

4. ### Relógio de Lamport com IDs de processo:
Cada processo mantém um relógio local (C_i) e um ID. Ao atualizar (enviar "mensagem" via etcd), C_i é incrementado, atualizado para max(C_i, C_global_etcd) + 1, e salvo no etcd com o ID do processo. Ao ler (receber "mensagem"), C_i é atualizado para max(C_i, C_global_recebido) + 1.


https://github.com/user-attachments/assets/6aedb885-6759-4299-ad25-b8146a7fe4cf



6. ### Latência de leitura ('linearizable' vs `serializable`):
* **`linearizable` (linearizável):** Possui maior latência, pois exige comunicação com o líder e validação de quorum para garantir a versão mais recente dos dados:
* **`serializable` (serializável):** Apresenta menor latência, pois a leitura é feita do estado local do nó, sem consulta ao líder. Pode, no entanto, retornar dados desatualizados.

6. ### `--quota-backend-bytes`:
Esta configuração define o limite máximo de armazenamento para o banco de dados do etcd. Se esse limite for excedido, o etcd entra em modo "somente leitura" para escritas, recusando novas operações e impactando severamente o desempenho de escrita.

7. Sincronização NTP após isolamento:
Ao reconectar após 5 minutos de isolamento, o `chrony` restaura a sincronização usando:
* `iburst` para uma sincronização inicial rápida.
* `makestep` para ajustar instantaneamente o relógio se o desvio for maior que 1 segundo e persistir.
* `driftfile` para compensar a taxa de derivação do relógio local, acelerando a convergência.

8. Derivação de relógio em sistemas de leasing:
Em um cenário de derivação de relógio de `$500ms/min$` (adiantado), um sistema de leasing do etcd seria afetado por:
* Expiração prematura de leases e recursos associados.
* Inconsistências e problemas de disponibilidade, já que os serviços podem assumir que leases são válidos enquanto o etcd já os expirou.

9. Detecção de relógios defeituosos (comunicação entre nós):
Uma estratégia envolve a troca periódica de mensagens entre os nós, incluindo seus timestamps locais. Ao receber as mensagens, os nós calculam o desvio (`offset`) em relação aos relógios dos outros. Um relógio é considerado defeituoso se seu offset exceder um limiar predefinido.

10. Serviço de membership dinâmico com etcd+watch:
A implementação envolve:
* **Registro de Serviço:** Cada instância de serviço se registra no etcd com uma chave e um `lease` (TTL). O `lease` é mantido ativo periodicamente e, em caso de falha da instância, ele expira, removendo automaticamente a chave.
* **Descoberta de Serviço com `watch`:** Clientes fazem um `watch` em um prefixo de chaves no etcd. O `watch` os notifica em tempo real sobre eventos (criação, atualização, exclusão) das chaves, permitindo que atualizem dinamicamente suas listas de membros do serviço.
