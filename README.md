Estrutura básica sugerida

# 🧮 Calculadora Python

Este repositório contém **dois projetos** que juntos formam uma calculadora de estudos:
- **FastHello** → API desenvolvida em **FastAPI**.
- **appWebConsumirFastAPI** → Aplicação **Streamlit** que consome a API.

---

## 📂 Estrutura
CalculadoraPython/
└─ CalculadoraFastApiStreamlit/
├─ FastHello/ # API FastAPI
└─ appWebConsumirFastAPI/ # App Streamlit


---

## 🚀 Tecnologias
- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)

---

## 🔧 Como executar cada projeto

### 1️⃣ FastHello (API)
```bash
cd CalculadoraFastApiStreamlit/FastHello
pip install -r requirements.txt
uvicorn main:app --reload

Acesse em: http://127.0.0.1:8000


appWebConsumirFastAPI (Streamlit)

cd CalculadoraFastApiStreamlit/appWebConsumirFastAPI
pip install -r requirements.txt
streamlit run app.py

Acesse em: http://localhost:8501

📝 Observações

Crie um ambiente virtual (python -m venv venv) antes de instalar os pacotes para cada projeto.

Os arquivos requirements.txt de cada pasta listam as dependências.

📜 Licença

Este projeto é de uso pessoal/educacional. Sinta-se à vontade para clonar e adaptar.


---

## 🟢 3. Enviar para o GitHub
Depois de criar/editar o README.md:

```bash
git add README.md
git commit -m "Adiciona README com instruções"
git push origin main

💡 Dicas de Markdown

# Título → cria títulos grandes.

**negrito** → negrito.

- item → lista.

bash → bloco de código com destaque para comandos.

