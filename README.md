# Microsoft Rewards Bot

Este bot automatiza as pesquisas do Microsoft Rewards usando Selenium.

## Requisitos

- Python 3.7+
- Google Chrome instalado
- Conta Microsoft

## Instalação

1. Clone este repositório
2. Instale as dependências:
```
pip install -r requirements.txt
```

## Como usar

1. Crie um arquivo .env com as suas credenciais da conta Microsoft (EMAIL e PASSWORD) 

2. Execute o script:
```
python microsoft_rewards_bot.py
```

2. Insira suas credenciais da conta Microsoft quando solicitado

O bot irá:
- Fazer login na sua conta Microsoft
- Realizar 30 pesquisas automaticamente no Bing
- Esperar um tempo aleatório entre as pesquisas para simular comportamento humano

## Observações

- O bot está configurado para fazer 30 pesquisas por padrão (3 pontos por pesquisa, somando os 90 pontos diários)
- Você pode modificar o número de pesquisas alterando o parâmetro `num_searches` na função `perform_searches`
- Para executar em modo headless (sem abrir o navegador), na linha do headless_mode, troque `headless_mode=False` por `headless_mode=True`


