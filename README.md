# 📊 Projeto Final - SaaS com Streamlit + IA

**Disciplina**: Fundamentos de Inteligência Artificial   
**Grupo**: DAVI BRITO MACHADO, DJALMA FELIPE DE SOUSA NETO e HILTON MEDEIROS AMORIM

---

## 💡 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação SaaS (Software as a Service) construída com Streamlit. A ferramenta se conecta à API do Google Gemini para oferecer um serviço de sumarização de textos.

A proposta da aplicação é fornecer uma ferramenta online que resume automaticamente textos longos, utilizando o poder da inteligência artificial generativa para extrair as informações mais importantes de forma rápida e coesa.


---

## 🚀 Funcionalidades

- Interface interativa com Streamlit
- Sumarização Inteligente: Utiliza a IA do Google para gerar resumos precisos em português.
- Exibição Instantânea: O resumo é exibido na tela logo após o processamento.
- Configuração Segura: A chave da API é gerenciada de forma segura através de um arquivo de ambiente (.env).

---

## 🧠 API de IA Utilizada

- **API Utilizada**: Gemini (Google AI)  

---

## 🛠️ Tecnologias e Ferramentas

- [✔️] Python
- [✔️] Streamlit
- [✔️] API de IA (Gemini / outra)

---


## 📂 Como Executar Localmente

Siga os passos abaixo para rodar o projeto na sua máquina.

**1. Clone o Repositório:**
```bash
git clone [https://github.com/djalma-neto/saas-com-streamlit-ia.git](https://github.com/djalma-neto/saas-com-streamlit-ia.git)
cd saas-com-streamlit-ia
```

**2. Crie e Ative um Ambiente Virtual:**
```bash
# Crie o ambiente
python -m venv venv

# Ative o ambiente (Windows)
venv\Scripts\activate

# Ative o ambiente (macOS/Linux)
source venv/bin/activate
```

**3. Instale as Dependências:**
Crie um arquivo `requirements.txt` com o conteúdo abaixo e execute o comando de instalação.

**`requirements.txt`**:
```txt
streamlit
requests
python-dotenv
```

**Comando:**
```bash
pip install -r requirements.txt
```

**4. Configure sua Chave de API:**
Altere o variável api_key e coloque sua chave

```
api_key="SUA_CHAVE_SECRETA_DO_GEMINI_AQUI"
```
*(Você pode obter uma chave na [Google AI Studio](https://aistudio.google.com/app/apikey)).*

**5. Execute a Aplicação:**
```bash
streamlit run app.py
```
O aplicativo será aberto no seu navegador local, geralmente em `http://localhost:8501`.

## 🚀 Site usado para Deploy
 
* Acesse [share.streamlit.io](https://share.streamlit.io/) e crie sua conta, preferencialmente usando a opção "Continue with GitHub" para uma integração mais fácil.
