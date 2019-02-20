# botnet
<h3>Tarefa sobre sockets passada na disciplina de redes 1 como composição da nota da ab1.1</h3>

Uma botnet ou rede de robôs ou zumbis são redes de computadores infectados por um
malware de acesso remoto, no qual fica aguardando uma ordem para atacar um alvo,
essa ordem normalmente vem do dono da rede de zumbis e o alvo normalmente são
servidores web ou não, que rodam serviços muito utilizados como sites do governo.
Nesse caso o ataque é do tipo DDoS (negação de serviço), que consiste em um numero
de requisição de pacotes extremamente alto e fora do comum, de tal forma que o
servidor não consiga responder a todos os acessos e acabe caindo, ou consiga responder
aos acessos mas por serem muitos, fica extremamente lento, tornando inviável a
utilização do servidor

<h3>Parâmetros da botnet :</h3>
<br><br>
Comando: <b> <esganar slaves> </b><br>
 Ao enviar este comando no server.py os clients que estiverem escutando o
server irão encerrar o processo client.py, interrompendo assim a comunicação
com o mesmo.
<br><br>
Comando: <b> <aperriar ip:port> </b><br>
 Ao enviar este comando no server.py, por exemplo “<aperriar
127.0.0.1:8888>”, você estará enviando vários pacotes através dos clients para a
porta do ip especificado.
<br><br>
Comando: <b> <espiar hosts up> </b><br>
 Ao enviar este comando no server.py para os clients, estes retornaram o seu IP
para o server; assim o server saberá quem está na escuta na botnet. 
