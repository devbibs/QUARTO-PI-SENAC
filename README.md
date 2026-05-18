# QUARTO-PI-SENAC
Repositório para a entrega do Projeto Integrador do 4º semestre do curso de Análise e Desenvolvimento de Sistemas do SENAC
🎓 PROJETO INTEGRADOR: Desenvolvimento de Sistemas Orientado a Dispositivos Móveis e Baseados na Web

💻 Descrição do Projeto
Este repositório contém todos os entregáveis pedidos na Segunda Entrega (código-fonte organizado nas devidas subpastas e documento README.md com instruções para a execução do projeto) do Projeto Integrador do 4º semestre para o curso de Análise e Desenvolvimento de Sistemas EAD.

🎯 Definição da PoC
A Prova de Conceito (PoC) desenvolvida neste projeto tem como objetivo validar, de forma prática, a viabilidade técnica e funcional da solução proposta, antes de sua implementação completa. A funcionalidade escolhida consiste em um filtro de oportunidades e cursos baseado em palavras-chave, projetada para simular uma experiência real de uso. Também foram desenvolvidos esqueletos para uma página de favoritos, onde o usuário pode colocar em destaque os cursos que mais lhe interessarem, e uma página de perfil, onde é possível cadastrar alguns de seus interesses, informações pessoais e até um texto “sobre mim”. Além disso, utilizando o próprio DevTools em seu navegador, é possível visualizar como a página seria disposta em um dispositivo móvel. 

🛠️ Tecnologias Utilizadas 
Back-end
•	Python 3.10+
•	FastAPI
•	Uvicorn
Front-end
•	HTML5
•	Tailwind CSS
Banco de Dados
•	SQLite

⚙️ Como Executar o Projeto
✅ 1. Clonar o Repositório e Acessar a Pasta Raiz
git clone https://github.com/devbibs/QUARTO-PI-SENAC.git
cd QUARTO-PI-SENAC
✅ 2. Criar e ativar um Ambiente Virtual na pasta do projeto
python -m venv venv
Ativar no Windows:
venv\Scripts\activate
Ativar no Linux/Mac:
source venv/bin/activate
✅ 3. Instalar as Dependências
pip install -r requirements.txt
✅ 4. Executar o Back-end (API)
uvicorn backend.main:app --reload

Após iniciar, a API estará disponível em:
👉 http://127.0.0.1:8000
Documentação automática:
👉 http://127.0.0.1:8000/docs
✅ 5. Executar o Front-end
•	Abra o arquivo:
frontend/index.html
•	Clique duas vezes ou abra no navegador

🧪 Como Testar
1.	Execute o back-end;
2.	Abra o front-end no navegador;
3.	Digite um termo no campo de busca, por exemplo: IA (ou selecione uma das “Opções Populares”);
4.	Clique em Filtrar;
5.	Veja os resultados sendo exibidos dinamicamente.

👥 Integrantes
Este projeto foi desenvolvido em colaboração por toda a equipe. Todos os membros da equipe estão cadastrados como contribuidores neste repositório do GitHub e constam como Colaboradores.
Membro	Github
BRUNO FRESCHI CONTE	@brunofreschii
BIANCA LIMA HABKOUK	@devbibs

