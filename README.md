# Kpop API Project Api-Development Documentatie

## Beschrijving van het gekozen thema
Ik heb voor het thema 'Kpop' gekozen, aangezien dit mijn favoriet muziekgenre is. Het leek me een tof idee om een API te bouwen die Kpop songs bevat en kan opvragen.

[Link front-end](https://sooivervloessem.github.io/apidevelopment-project/)  
[Link front-end repository (deze repo)](https://github.com/sooivervloessem/apidevelopment-project)  
[Hosted API link](https://project-service-sooivervloessem.cloud.okteto.net/)  

## API functionaliteit van de back-end
![Image Backend Setup](/images_readme/setup_backend.png)  
Op bovenstaande afbeelding wordt de API geïnitialiseerd.
CORS wordt toegepast.
Ook wordt er een klasse 'KpopSong' aangemaakt. Deze bevat de structuur voor een Kpop song.

![Image kpop_songs](/images_readme/kpop_song_list_backend.png)  
Hierboven wordt een dictionary 'kpop_songs' aangemaakt. Deze bevat al enkele Kpop songs om van te starten.

![Image methods_backend](/images_readme/get_post_method_backend.png)  
Er zijn 3 GET en 1 POST method ingesteld voor de API.

### get_kpop_songs()
get_kpop_songs() geeft simpelweg de hele dictionary met kpop songs in terug.

### get_random_kpop_song()
get_random_kpop_song() geeft een random kpop song terug.
Er wordt een randint gebruikt met als maximum waarde de hoogste key in de dictionary.

### get_kpop_song_by_id(id: int)
get_kpop_song_by_id(id: int) geeft de song met het meegegeven id terug.
Er wordt gecheckt of het id bestaat als key in de dictionary. 

### create_kpop_song(kpop_song: KpopSong)
create_kpop_song(kpop_song: KpopSong) creëert een nieuwe kpop song in de dictionary. De meegegeven 'kpop_song' moet dezelfde structuur als de klasse KpopSong hebben.

## API functionaliteit van de front-end
Vervolgens bekijken we de front-end

### Front-end
![Front end](/images_readme/front_end.png)  
De gehele front-end ziet er uit zoals hierboven.

### Random Song
![Random Song](/images_readme/front_end_random_song.png)  
Met de Random Song functie kan een random song uit de dictionary opgevraagd worden. Deze wordt mooi getoond op de front-end.

### Song by ID
![Song by id](/images_readme/front_end_song_by_id.png)  
Met de Song by ID functie kan een song uit de dictionary gezocht worden op basis van het id van deze song.

![Song by id fail](/images_readme/fail_id_too_big.png)  
![Song by id fail](/images_readme/fail_id_smaller_zero.png)  
De back-end validatie die op dit ID gebeuren worden weergegeven bij een error zoals hierboven.

### Add a song to the database
Een song kan toegevoegd worden aan de dictionary.

![Validatie POST](/images_readme/validation_front_end_post.png)  
Er moet minstens een 'song' en een 'artist' meegegeven worden. Wanneer dit niet het geval is krijgt men bovenstaande alert.

![Successful POST](/images_readme/successful_post.png)  
Wanneer de veldjes juist zijn ingevuld, wordt de song toegevoegd aan de dictionary en krijgt men bovenstaande alert.

![Test POST](/images_readme/successful_post_by_id.png)  
De song is successvol toegevoegd aan de dictionary, aangezien deze kan opgevraagd worden op basis van het id zoals hierboven.

## Werking API met Postman
Vervolgens toon ik de werking van de API met Postman

![Get Kpop songs](/images_readme/postman_kpop.png)  
Hierboven worden alle songs uit de dictionary opgevraagd.

![Get Kpop random 1](/images_readme/postman_kpop_random1.png)  
![Get Kpop random 2](/images_readme/postman_kpop_random2.png)  
Hierboven wordt een random song uit de dictionary opgevraagd.

![Get Kpop by id](/images_readme/postman_kpop_2.png)  
Hierboven wordt de song met id 2 opgevraagd.

![Postman Post](/images_readme/postman_post_kpop.png)  
Hierboven wordt een post request uitgevoerd met als body een song. De API returned de ingegeven waardes en geeft 'null' voor de waardes die niet werden ingevuld.

![Postman Post check](/images_readme/postman_post_kpop_check.png)  
Wanneer we het id van de song opzoeken met een GET request kunnen we vaststellen dat de song is toegevoegd aan de dictionary.

## OpenAPI Docs
![OpenAPI Docs All](/images_readme/openapidocs.png)  
We bekijken ook even de OpenAPI Docs van de API.

### Get /kpop
![OpenAPI Docs /kpop](/images_readme/get_kpop_docs.png)  

### Get /kpop/random
![OpenAPI Docs /kpop/random](/images_readme/get_kpop_random_docs.png)  

### Get /kpop/{id}
![OpenAPI Docs /kpop/id](/images_readme/get_kpop_id_docs.png)  

### Post /kpop
![OpenAPI Docs Post /kpop](/images_readme/post_docs.png)  

### Schemas
![OpenAPI Docs Schemas](/images_readme/Schemas.png)  

## Besluit
Het project is successvol ten einde gebracht. Ik heb opdrachten uitgevoerd voor een maximum van 75 %

- Algemene eisen & documentatie 65 %
- Stijlgeving op de front-end 5 %
- POST endpoint ook op de front-end 5 %
