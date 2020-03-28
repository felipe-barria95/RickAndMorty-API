import requests

#episodios = []
#URL_pag ="https://rickandmortyapi.com/api/episode/?page=1"
#while URL_pag != "":
#    response = requests.get(URL_pag).json()
#    episodios.append(response['results'])
#    URL_pag = response['info']['next']

#print(episodios)

#URL_pag = "https://rickandmortyapi.com/api/episode/1"
#episodio = requests.get(URL_pag).json()
#lista_personajes_finales = []
#for personaje in episodio["characters"]:
#    URL_personaje = personaje
#    info_personaje = requests.get(URL_personaje).json()
#    personaje_final = {'id': info_personaje['id'], 'name': info_personaje['name']}
#    lista_personajes_finales.append(personaje_final)

#episodio["personajes_finales"] = lista_personajes_finales
#print(episodio)

#URL_pag = "https://rickandmortyapi.com/api/character/1"
#personaje = requests.get(URL_pag).json()
#url_location = personaje['location']['url']
#url_location = str(url_location)
#url = url_location.split("/")
#personaje['location']['id'] = url[-1]
#url_origin = personaje['origin']['url']
#url_origin = str(url_origin)
#url = url_origin.split("/")
#personaje['origin']['id'] = url[-1]
#print(personaje)


#URL_pag = "https://rickandmortyapi.com/api/location/1"
#lista_residentes_final = []
#ubicacion = requests.get(URL_pag).json()
#for url in ubicacion['residents']:
#    info_personaje = requests.get(url).json()
#    personaje_final = {'id': info_personaje['id'], 'name': info_personaje['name']}
#    lista_residentes_final.append(personaje_final)
#ubicacion['residentes_finales'] = lista_residentes_final
#print(ubicacion)

#id_character = 395
#URL_pag = "https://rickandmortyapi.com/api/character/" + str(id_character)
#personaje = requests.get(URL_pag).json()
#url_location = personaje['location']['url']
#url_location = str(url_location)
#url = url_location.split("/")
#personaje['location']['id'] = url[-1]#
#url_origin = personaje['origin']['url']
#url_origin = str(url_origin)
#url = url_origin.split("/")
#personaje['origin']['id'] = url[-1]
#lista_episodes_final = []
#for url in personaje['episode']:
#    episode = requests.get(url).json()
#    episode_final = {'id': episode['id'], 'name': episode['name']}
#    lista_episodes_final.append(episode_final)
#personaje['episodios_final'] = lista_episodes_final
#personaje_final = [personaje]
#print(personaje_final)


#texto = 'rick'

#URL_character = 'https://rickandmortyapi.com/api/character/?name=' + str(texto)
#URL_location = 'https://rickandmortyapi.com/api/location/?name=' + str(texto)
#URL_episode = 'https://rickandmortyapi.com/api/episode/?name=' + str(texto)
#json_character = requests.get(URL_character).json()
#json_location = requests.get(URL_location).json()
#json_episode = requests.get(URL_episode).json()


#print(json_character)

#if 'error' in json_character:
#    print("error")
#else:
#    print("ok")

#resultados_personaje = []
#resultados_personaje += json_character['results']
#while json_character['info']['next'] != '':
#    json_character = requests.get(json_character['info']['next']).json()
#    resultados_personaje += json_character['results']
#
#
#print(resultados_personaje)
#id_episode = 1
#URL_pag = "https://rickandmortyapi.com/api/episode/" + str(id_episode)
#episodio = requests.get(URL_pag).json()
#lista_personajes_finales = ''
#print(episodio)
#for elemento in episodio['characters']:
#    lista_elemento = elemento.split('/')[-1]
#    lista_personajes_finales +=lista_elemento
#    lista_personajes_finales += ','
#lista_personajes_finales = lista_personajes_finales[:-1]
#URL_pag = "https://rickandmortyapi.com/api/character/" + lista_personajes_finales
#characters = requests.get(URL_pag).json()
#episodio["personajes_finales"] = characters
#print(characters)
id_character = 223



URL_pag = "https://rickandmortyapi.com/api/character/" + str(id_character)
personaje = requests.get(URL_pag).json()

lista_episodios_finales = ''
for elemento in personaje['episode']:
    lista_elemento = elemento.split('/')[-1]
    lista_episodios_finales +=lista_elemento
    lista_episodios_finales += ','
lista_episodios_finales = lista_episodios_finales[:-1]
URL_pag = "https://rickandmortyapi.com/api/episode/" + lista_episodios_finales
episodes = requests.get(URL_pag).json()
personaje['episodios_final'] = episodes
personaje_final = personaje
print(type(personaje_final)is dict)
id_episode = 1

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
episodio["personajes_finales"] = characters
informacion_final = episodio
