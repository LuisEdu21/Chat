# Chat
Um chat com Python e se conectando com webhook 

/saq_project
│
├── /app                    # Diretório principal da aplicação
│   ├── __init__.py          # Inicializa o app Flask
│   ├── routes.py            # Define as rotas/endpoints do chat
│   ├── models.py            # Modelos de dados (Usuários, Conteúdo, etc.)
│   ├── services.py          # Lógica de negócios e integração com WebHook
│   ├── permissions.py       # Módulo para controle de permissões de usuário
│   ├── /static              # Arquivos estáticos (imagens, CSS, JS)
│   └── /templates           # Templates HTML, caso use renderização de páginas (opcional)
│
├── /config                  # Configurações do projeto
│   ├── __init__.py          # Inicialização da configuração
│   └── config.py            # Arquivo de configuração (URLs, WebHook, etc.)
│
├── /tests                   # Testes automatizados
│   ├── __init__.py          # Inicialização dos testes
│   └── test_chat.py         # Testes unitários para a lógica do chat
│
├── /migrations               # Arquivos de migração de banco de dados (se necessário)
│
├── run.py                   # Arquivo principal para executar a aplicação Flask
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação inicial do projeto
└── .env                     # Variáveis de ambiente (configurações sensíveis como senhas, API keys)
