import requests

def test_api_zenquotes():

    resposta = requests.get("https://zenquotes.io/api/random")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert "q" in dados[0]