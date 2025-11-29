# Problema Escolhido

Muitas escolas não possuem um canal formal e organizado para que alunos e funcionários compartilhem ideias de melhoria. Essa problemática resulta em falta de sugestões não vistas e perdidas, falta de transparência com os alunos e funcionários sobre qual sugestão é que está sendo considerada. Por isso é de suma necessidade para um ambiente escolar menos hostil e benéfico para o lado docente como também para o discente.

## Objetivo do Sistema

Criar uma plataforma digital onde alunos e funcionários possam enviar, visualizar e apoiar sugestões para melhorar o ambiente escolar, estrutura física, métodos de ensino e outros aspectos da escola, permitindo que a gestão acompanhe, responda e implemente as ideias mais relevantes para uma escola mais acolhedora e produtiva.

## Público-Alvo

Alunos: do ensino fundamental, médio ou superior que desejam expressar suas ideias de melhorias para uma comunidade escolar

Funcionários: professores, coordenadores, equipe administrativa e terceirizados

Gestores escolares: diretores e coordenadores que analisam e respondem às sugestões

## Lista de Funcionalidades

### Para Alunos e Funcionários

1. Cadastro e login (diferenciando aluno/funcionário)  
2. Enviar sugestões com título e descrição  
3. Visualizar todas as sugestões enviadas pela comunidade  
4. Acompanhar status das próprias sugestões (pendente, em análise, aprovada, implementada, recusada)

### Para administrador

1. Painel administrativo para visualizar todas as sugestões  
2. Alterar status das sugestões  
3. Responder às sugestões  
4. Marcar sugestões como implementadas com descrição da ação tomada

## Rotas Principais

### Rotas básicas

1. GET / \- Página inicial
2. GET /login \- Página de login  
3. GET /cadastro \- Página de cadastro

### Rotas Autenticadas (Alunos e Funcionários)

1. GET /sugestoes \- Lista todas as sugestões
2. GET /sugestoes/n\_id \- Detalhes de uma sugestão específica  
3. POST /sugestoes \- Criar nova sugestão  
4. GET /minhas-sugestoes \- Lista sugestões do usuário logado  
5. GET /perfil \- Página do perfil do usuário

### Rotas Administrativas (admin)

1. GET /admin/sugestoes \- Lista completa para gestão  
2. PATCH /admin/sugestoes/n\_id/status \- Atualizar status de sugestão  
3. POST /admin/sugestoes/n\_id/resposta \- Responder a uma sugestão
