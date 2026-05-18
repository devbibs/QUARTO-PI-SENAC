# 🎓 PROJETO INTEGRADOR: Desenvolvimento de Sistemas Orientado a Dispositivos Móveis e Baseados na Web

# 💻 Descrição do Projeto
Este repositório contém todos os entregáveis pedidos na Segunda Entrega (código-fonte organizado nas devidas subpastas, documento README.md com instruções para a execução do projeto e um vídeo final de demonstração) do Projeto Integrador do 4º semestre para o curso de Análise e Desenvolvimento de Sistemas EAD.

# 🎯 Definição da PoC
A Prova de Conceito (PoC) desenvolvida neste projeto tem como objetivo validar, de forma prática, a viabilidade técnica e funcional da solução proposta, antes de sua implementação completa. A funcionalidade escolhida consiste em um filtro de oportunidades e cursos baseado em palavras-chave, projetada para simular uma experiência real de uso. Também foram desenvolvidos esqueletos para uma página de favoritos, onde o usuário pode colocar em destaque os cursos que mais lhe interessarem, e uma página de perfil, onde é possível cadastrar alguns de seus interesses, informações pessoais e até um texto “sobre mim”. Além disso, utilizando o próprio DevTools em seu navegador, é possível visualizar como a página seria disposta em um dispositivo móvel. 

# 🛠️ Tecnologias Utilizadas 
**Back-end:**
  Python 3.10+
•	FastAPI
•	Uvicorn

**Front-end:**
  HTML5
•	Tailwind CSS

**Banco de Dados:**
 SQLite

# ⚙️ Como Executar o Projeto
**✅ 1. Clonar o Repositório e Acessar a Pasta Raiz** <br>
git clone https://github.com/devbibs/QUARTO-PI-SENAC.git <br>
cd QUARTO-PI-SENAC <br>
**✅ 2. Criar e ativar um Ambiente Virtual na pasta do projeto**<br>
python -m venv venv<br>
**Ativar no Windows:**<br>
venv\Scripts\activate<br>
**Ativar no Linux/Mac:**<br>
source venv/bin/activate<br>
**✅ 3. Instalar as Dependências**<br>
pip install -r requirements.txt<br>
**✅ 4. Executar o Back-end (API)**<br>
uvicorn backend.main:app --reload<br>

**Após iniciar, a API estará disponível em:**<br>
👉 http://127.0.0.1:8000<br>
**Documentação automática:**<br>
👉 http://127.0.0.1:8000/docs<br>
**✅ 5. Executar o Front-end**<br>
•	Abra o arquivo:<br>
frontend/index.html<br>
•	Clique duas vezes ou abra no navegador<br>

# 🧪 Como Testar
1.	Execute o back-end;
2.	Abra o front-end no navegador;
3.	Digite um termo no campo de busca, por exemplo: IA (ou selecione uma das “Opções Populares”);
4.	Clique em Filtrar;
5.	Veja os resultados sendo exibidos dinamicamente;
6.	Além disso, também é possível verificar as funções de favoritos clicando em ⭐ ou em ❌ e criar/atualizar suas próprias informações de perfil. 

# 👥 Integrantes
Este projeto foi desenvolvido em colaboração por toda a equipe. Todos os membros da equipe estão cadastrados como contribuidores neste repositório do GitHub e constam como Colaboradores.

| Membro                   | GitHub        |
|--------------------------|--------------|
| BRUNO FRESCHI CONTE      | @brunofreschii |
| BIANCA LIMA HABKOUK      | @devbibs      |

