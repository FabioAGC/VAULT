### Ativar a Venv Marota
Set-ExecutionPolicy Unrestricted -Scope Process
python -m venv .venv
&& source venv/bin/activate

### Testes
pip install -U pytest
&& pytest --version
https://docs.pytest.org/en/latest/getting-started.html


### Dependências
$pip install nome_pacote

gerenciador:
UV:https://github.com/astral-sh/uv
Poetry:https://python-poetry.org/docs/

![[Pasted image 20260303082522.png]]