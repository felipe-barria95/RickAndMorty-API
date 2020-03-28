from django.shortcuts import render
import requests


def index(request):
    episodios = []
    URL_pag = "https://rickandmortyapi.com/api/episode/?page=1"
    while URL_pag != "":
        response = requests.get(URL_pag).json()
        episodios.append(response['results'])
        URL_pag = response['info']['next']

    episodios = episodios[0] + episodios[1]
    return render(request, 'index.html', {"list": episodios})

def about(request):
    return render(request, 'about.html')

def episode(request, id_episode):
    URL_pag = "https://rickandmortyapi.com/api/episode/" + str(id_episode)
    episodio = requests.get(URL_pag).json()
    lista_personajes_finales = ''
    for elemento in episodio['characters']:
        lista_elemento = elemento.split('/')[-1]
        lista_personajes_finales += lista_elemento
        lista_personajes_finales += ','
    lista_personajes_finales = lista_personajes_finales[:-1]
    URL_pag = "https://rickandmortyapi.com/api/character/" + lista_personajes_finales
    characters = requests.get(URL_pag).json()
    if type(characters) is dict:
        characters = [characters]
    episodio["personajes_finales"] = characters
    informacion_final = episodio
    return render(request, 'episode.html', {"list": informacion_final})

def character(request, id_character):
    URL_pag = "https://rickandmortyapi.com/api/character/" + str(id_character)
    personaje = requests.get(URL_pag).json()
    lista_episodios_finales = ''
    for elemento in personaje['episode']:
        lista_elemento = elemento.split('/')[-1]
        lista_episodios_finales += lista_elemento
        lista_episodios_finales += ','
    lista_episodios_finales = lista_episodios_finales[:-1]
    URL_pag = "https://rickandmortyapi.com/api/episode/" + lista_episodios_finales
    episodes = requests.get(URL_pag).json()
    if type(episodes) is dict:
        episodes = [episodes]
    personaje['episodios_final'] = episodes
    personaje_final = personaje
    return render(request, 'character.html', {"list": personaje_final})

def location(request, id_location):
    URL_pag = "https://rickandmortyapi.com/api/location/" + str(id_location)
    lista_residentes_final = []
    ubicacion = requests.get(URL_pag).json()
    for url in ubicacion['residents']:
        info_personaje = requests.get(url).json()
        personaje_final = {'id': info_personaje['id'], 'name': info_personaje['name']}
        lista_residentes_final.append(personaje_final)
    ubicacion['residentes_finales'] = lista_residentes_final
    ubicacion_final = [ubicacion]
    return render(request, 'location.html', {"list": ubicacion_final})

def search(request, texto):
    URL_character = 'https://rickandmortyapi.com/api/character/?name=' + str(texto)
    json_character = requests.get(URL_character).json()
    resultados_personaje = []
    if 'error' in json_character:
        pass
    else:
        resultados_personaje += json_character['results']
        while json_character['info']['next'] != '':
            json_character = requests.get(json_character['info']['next']).json()
            resultados_personaje += json_character['results']
    URL_location = 'https://rickandmortyapi.com/api/location/?name=' + str(texto)
    json_location = requests.get(URL_location).json()
    resultados_ubicacion = []
    if 'error' in json_location:
        pass
    else:
        resultados_ubicacion += json_location['results']
        while json_location['info']['next'] != '':
            json_location = requests.get(json_location['info']['next']).json()
            resultados_ubicacion += json_location['results']
    URL_episode = 'https://rickandmortyapi.com/api/episode/?name=' + str(texto)
    json_episode = requests.get(URL_episode).json()
    resultados_episodio = []
    if 'error' in json_episode:
        pass
    else:
        resultados_episodio += json_episode['results']
        while json_episode['info']['next'] != '':
            json_episode = requests.get(json_episode['info']['next']).json()
            resultados_episodio += json_episode['results']
    return render(request, 'search.html', {"lista_personajes": resultados_personaje, "lista_episodios": resultados_episodio, "lista_ubicaciones": resultados_ubicacion},)

