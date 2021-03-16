from django.shortcuts import render
import requests

URL_PAG_INICIAL = "https://rickandmortyapi.com/api"
def index(request):
    episodios = []
    URL_pag = URL_PAG_INICIAL + "/episode/?page=1"
    while URL_pag != "":
        response = requests.get(URL_pag).json()
        episodios.append(response['results'])
        URL_pag = response['info']['next']
    episodios_final = []
    for elemento in episodios:
        episodios_final += elemento
    return render(request, 'index.html', {"list": episodios_final})

def about(request):
    return render(request, 'about.html')

def episode(request, id_episode):
    URL_pag = URL_PAG_INICIAL + "/episode/" + str(id_episode)
    episodio = requests.get(URL_pag).json()
    lista_personajes_finales = ''
    for elemento in episodio['characters']:
        lista_elemento = elemento.split('/')[-1]
        lista_personajes_finales += lista_elemento
        lista_personajes_finales += ','
    lista_personajes_finales = lista_personajes_finales[:-1]
    URL_pag = URL_PAG_INICIAL + "/character/" + lista_personajes_finales
    characters = requests.get(URL_pag).json()
    if type(characters) is dict:
        characters = [characters]
    episodio["personajes_finales"] = characters
    informacion_final = episodio
    return render(request, 'episode.html', {"list": informacion_final})

def character(request, id_character):
    URL_pag = URL_PAG_INICIAL + "/character/" + str(id_character)
    personaje = requests.get(URL_pag).json()
    lista_episodios_finales = ''
    for elemento in personaje['episode']:
        lista_elemento = elemento.split('/')[-1]
        lista_episodios_finales += lista_elemento
        lista_episodios_finales += ','
    lista_episodios_finales = lista_episodios_finales[:-1]
    URL_pag = URL_PAG_INICIAL + "/episode/" + lista_episodios_finales
    episodes = requests.get(URL_pag).json()
    if type(episodes) is dict:
        episodes = [episodes]
    personaje['episodios_final'] = episodes
    personaje_final = personaje
    id_location = personaje_final['location']['url'].split('/')[-1]
    id_origin = personaje_final['origin']['url'].split('/')[-1]
    personaje_final['location']['id'] = id_location
    if id_origin =='':
        personaje_final['origin']['id'] = 0
    else:
        personaje_final['origin']['id'] = id_origin
    return render(request, 'character.html', {"list": personaje_final})

def location(request, id_location):
    URL_pag = URL_PAG_INICIAL + "/location/" + str(id_location)
    ubicacion = requests.get(URL_pag).json()
    lista_personajes_finales = ''
    for elemento in ubicacion['residents']:
        lista_elemento = elemento.split('/')[-1]
        lista_personajes_finales += lista_elemento
        lista_personajes_finales += ','
    lista_personajes_finales = lista_personajes_finales[:-1]
    URL_pag = URL_PAG_INICIAL + "/character/" + lista_personajes_finales
    personajes = requests.get(URL_pag).json()
    if type(personajes) is dict:
        personajes = [personajes]
    ubicacion['personajes_final'] = personajes
    return render(request, 'location.html', {"list": ubicacion})

def search(request, texto):
    URL_character = URL_PAG_INICIAL + '/character/?name=' + str(texto)
    json_character = requests.get(URL_character).json()
    resultados_personaje = []
    if 'error' in json_character:
        pass
    else:
        resultados_personaje += json_character['results']
        while json_character['info']['next'] != '':
            json_character = requests.get(json_character['info']['next']).json()
            resultados_personaje += json_character['results']

    URL_location = URL_PAG_INICIAL + '/location/?name=' + str(texto)
    json_location = requests.get(URL_location).json()
    resultados_ubicacion = []
    if 'error' in json_location:
        pass
    else:
        resultados_ubicacion += json_location['results']
        while json_location['info']['next'] != '':
            json_location = requests.get(json_location['info']['next']).json()
            resultados_ubicacion += json_location['results']

    URL_episode = URL_PAG_INICIAL + '/episode/?name=' + str(texto)
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
