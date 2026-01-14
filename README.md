<h1 align="center">
   Python - Workspace
</h1>

<div align="center">

![Maintenance](https://img.shields.io/maintenance/yes/2025?style=for-the-badge)
![License MIT](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

## 📌 Sobre o Projeto

Este repositório funciona como um ambiente de trabalho para projetos de ciência de dados e análise exploratória, centralizando dados e notebooks em uma estrutura organizada.

### 📂 Estrutura do Repositório

```text
src/
├── data/
│   └── external/
│       ├── file.csv
│       └── ...
│
├── projects/
│    ├── name_project/
│    │   ├── name_project_analysis.ipynb
│    │   └── name_project_analysis.py
│    └── ...
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LICENSE
├── ...
```

## 🧰 Tecnologias Utilizadas

- Python 3.12
- JupyterLab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Docker & Docker Compose

## 🚀 Como Executar

### ✅ Pré-requisitos

- Docker
- Docker Compose (plugin ou standalone)

💡 Obs: Não é necessário instalar Python ou bibliotecas localmente.

### ▶️ Como subir o ambiente

1. Na raiz do projeto, execute o comando abaixo para construir e iniciar o ambiente (apenas na primeira vez ou se houver alterações no Dockerfile):

```bash
docker compose up --build
```

Nas próximas execuções, basta rodar:

```bash
docker compose up
```

2. Aguarde o build e a inicialização dos containers. O JupyterLab estará disponível em:

http://localhost:8888

3. O token de acesso será exibido no terminal. Copie e cole no navegador para acessar o JupyterLab.

### 🧪 Desenvolvimento

- Os notebooks (.ipynb) ficam em `src/projects`
- Os datasets CSV ficam centralizados em `src/data/external`
- Todo o código Python pode ser executado tanto via Jupyter quanto via scripts `.py`

## 👤 Sobre o Desenvolvedor <a name="sobre-o-desenvolvedor"></a>

<table align="center">
  <tr>
    <td align="center">
        <br>
        <a href="https://github.com/0nF1REy" target="_blank">
          <img src="./resources/images/docs/developer/alan-ryan.jpg" height="160" alt="Foto — Alan Ryan">
        </a>
        </p>
        <a href="https://github.com/0nF1REy" target="_blank">
          <strong>Alan Ryan</strong>
        </a>
        </p>
        ☕ Peopleware | Tech Enthusiast | Code Slinger ☕
        <br>
        Apaixonado por código limpo, arquitetura escalável e experiências digitais envolventes
        </p>
          Conecte-se comigo:
        </p>
        <a href="https://www.linkedin.com/in/alan-ryan-b115ba228" target="_blank">
          <img src="https://img.shields.io/badge/LinkedIn-Alan_Ryan-0077B5?style=flat&logo=linkedin" alt="LinkedIn">
        </a>
        <a href="https://gitlab.com/alanryan619" target="_blank">
          <img src="https://img.shields.io/badge/GitLab-@0nF1REy-FCA121?style=flat&logo=gitlab" alt="GitLab">
        </a>
        <a href="mailto:alanryan619@gmail.com" target="_blank">
          <img src="https://img.shields.io/badge/Email-alanryan619@gmail.com-D14836?style=flat&logo=gmail" alt="Email">
        </a>
        </p>
    </td>
  </tr>
</table>

</div>

---

## 📜 Licença <a name="licenca"></a>

Este projeto está sob a **licença MIT**. Consulte o arquivo **[LICENSE](LICENSE)** para obter mais detalhes.

> ℹ️ **Aviso de Licença:** &copy; 2026 Alan Ryan da Silva Domingues. Este projeto está licenciado sob os termos da licença MIT. Isso significa que você pode usá-lo, copiá-lo, modificá-lo e distribuí-lo com liberdade, desde que mantenha os avisos de copyright.

⭐ Se este repositório foi útil para você, considere dar uma estrela!
