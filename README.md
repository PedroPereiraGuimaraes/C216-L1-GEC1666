# 🚧 Projeto Final Sistemas Distribuídos

O objetivo do projeto final foi desenvolver uma aplicação funcional aplicando os conceitos de Sistemas Distribuídos, com as seguintes especificações de serviços: 

- Backend
- Frontend
- Banco de dados

## ⛏️ Ferramentas

Para desenvolver a aplicação seguindo as especificações foram utilizadas as diversas tecnologias para o melhor funcionamento da aplicação.

![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-00B01C?style=for-the-badge&logo=mongodb&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-FF3700?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-BA03A8?&style=for-the-badge&logo=css3&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-0091FF?style=for-the-badge&logo=docker&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-6500FF?style=for-the-badge&logo=bootstrap&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-BC0505?style=for-the-badge&logo=flask&logoColor=white)

## 📰 Sistema de Noticias

O sistemas de noticias foi projetado para as ter as seguintes funcionalidades:
    
- Ver Noticias
- Criar Noticias
- Atualizar Noticias
- Deletar Noticias

## 💻 Frontend

Para o Frontend foi utilizado HTML e CSS para as telas e Python para o unificar as telas e ajudar no funcionamento.

## 👨🏻‍💻 Backend

Para o Backend foi criada uma API com a biblioteca Flask do Python, as rotas desta api e sua documentação são:

####  Listar toda a documentação
- **URL:** `/docs`
- **Método:** `GET`

####  Ver todas as notícias
- **URL:** `/news/all`
- **Método:** `GET`

####  Criar uma notícia
- **URL:** `/news/create`
- **Método:** `POST`

####  Atualizar uma notícia
- **URL:** `/news/update`
- **Método:** `POST`

####  Deletar uma notícia
- **URL:** `/news/delete/{id}`
- **Método:** `POST`

## 🐳 Dockerfile

Foi montado também um dockerfile para containerizar a aplicação e para simplificar seu funcionamento, expansão e controle. Nele são unificados os serviços de **`Backend`** e **`Frontend`**.