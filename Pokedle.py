import sys
import random

pokemon_gen1_2_3_4 = [
  {'nombre':'Bulbasaur','tipo1':'Planta','tipo2':'Veneno','Evolucion':1,'gen':1},
  {'nombre':'Ivysaur','tipo1':'Planta','tipo2':'Veneno','Evolucion':2,'gen':1},
  {'nombre':'Venusaur','tipo1':'Planta','tipo2':'Veneno','Evolucion':3,'gen':1},
  {'nombre':'Charmander','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Charmeleon','tipo1':'Fuego','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Charizard','tipo1':'Fuego','tipo2':'Volador','Evolucion':3,'gen':1},
  {'nombre':'Squirtle','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Wartortle','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Blastoise','tipo1':'Agua','tipo2':' ','Evolucion':3,'gen':1},
  {'nombre':'Caterpie','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Metapod','tipo1':'Bicho','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Butterfree','tipo1':'Bicho','tipo2':'Voldaor','Evolucion':3,'gen':1},
  {'nombre':'Weedle','tipo1':'Bicho','tipo2':'Veneno','Evolucion':1,'gen':1},
  {'nombre':'Kakuna','tipo1':'Bicho','tipo2':'Veneno','Evolucion':2,'gen':1},
  {'nombre':'Beedrill','tipo1':'Bicho','tipo2':'Veneno','Evolucion':3,'gen':1},
  {'nombre':'Pidgey','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Pidgeotto','tipo1':'Normal','tipo2':'Volador','Evolucion':2,'gen':1},
  {'nombre':'Pidgeot','tipo1':'Normal','tipo2':'Volador','Evolucion':3,'gen':1},
  {'nombre':'Rattata','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Raticate','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Spearow','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Fearow','tipo1':'Normal','tipo2':'Volador','Evolucion':2,'gen':1},
  {'nombre':'Ekans','tipo1':'Veneno','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Arbok','tipo1':'Veneno','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Pikachu','tipo1':'Eléctrico','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Raichu','tipo1':'Eléctrico','tipo2':' ','Evolucion':3,'gen':1},
  {'nombre':'Sandshrew','tipo1':'Tierra','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Sandslash','tipo1':'Tierra','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Nidoran_Hembra','tipo1':'Veneno','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Nidorina','tipo1':'Veneno','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Nidoqueen','tipo1':'Veneno','tipo2':'Tierra','Evolucion':3,'gen':1},
  {'nombre':'Nidoran_Macho','tipo1':'Veneno','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Nidorino','tipo1':'Veneno','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Nidoking','tipo1':'Veneno','tipo2':'Tierra','Evolucion':3,'gen':1},
  {'nombre':'Clefairy','tipo1':'Hada','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Clefable','tipo1':'Hada','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Vulpix','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Ninetales','tipo1':'Fuego','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Jigglypuff','tipo1':'Normal','tipo2':'Hada','Evolucion':1,'gen':1},
  {'nombre':'Wigglytuff','tipo1':'Normal','tipo2':'Hada','Evolucion':2,'gen':1},
  {'nombre':'Zubat','tipo1':'Veneno','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Golbat','tipo1':'Veneno','tipo2':'Volador','Evolucion':2,'gen':1},
  {'nombre':'Oddish','tipo1':'Planta','tipo2':'Veneno','Evolucion':1,'gen':1},
  {'nombre':'Gloom','tipo1':'Planta','tipo2':'Veneno','Evolucion':2,'gen':1},
  {'nombre':'Vileplume','tipo1':'Planta','tipo2':'Veneno','Evolucion':3,'gen':1},
  {'nombre':'Paras','tipo1':'Bicho','tipo2':'Planta','Evolucion':1,'gen':1},
  {'nombre':'Parasect','tipo1':'Bicho','tipo2':'Planta','Evolucion':2,'gen':1},
  {'nombre':'Venonat','tipo1':'Bicho','tipo2':'Veneno','Evolucion':1,'gen':1},
  {'nombre':'Venomoth','tipo1':'Bicho','tipo2':'Veneno','Evolucion':2,'gen':1},
  {'nombre':'Diglett','tipo1':'Tierra','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Dugtrio','tipo1':'Tierra','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Meowth','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Persian','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Psyuck','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Golduck','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Mankey','tipo1':'Lucha','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Primeape','tipo1':'Lucha','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Growlithe','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Arcanine','tipo1':'Fuego','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Poliwag','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Poliwhirl','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Poliwrath','tipo1':'Agua','tipo2':'Lucha','Evolucion':3,'gen':1},
  {'nombre':'Abra','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Kadabra','tipo1':'Psíquico','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Alakazam','tipo1':'Psíquico','tipo2':' ','Evolucion':3,'gen':1},
  {'nombre':'Machop','tipo1':'Lucha','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Machoke','tipo1':'Lucha','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Machamp','tipo1':'Lucha','tipo2':' ','Evolucion':3,'gen':1},
  {'nombre':'Bellsprout','tipo1':'Planta','tipo2':'Veneno','Evolucion':1,'gen':1},
  {'nombre':'Weepinbell','tipo1':'Planta','tipo2':'Veneno','Evolucion':2,'gen':1},
  {'nombre':'Victreebel','tipo1':'Planta','tipo2':'Veneno','Evolucion':3,'gen':1},
  {'nombre':'Tentacool','tipo1':'Agua','tipo2':'Veneno','Evolucion':1,'gen':1},
  {'nombre':'Tentacruel','tipo1':'Agua','tipo2':'Veneno','Evolucion':2,'gen':1},
  {'nombre':'Geodude','tipo1':'Roca','tipo2':'Tierra','Evolucion':1,'gen':1},
  {'nombre':'Graveler','tipo1':'Roca','tipo2':'Tierra','Evolucion':2,'gen':1},
  {'nombre':'Golem','tipo1':'Roca','tipo2':'Tierra','Evolucion':3,'gen':1},
  {'nombre':'Ponyta','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Rapidash','tipo1':'Fuego','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Slowpoke','tipo1':'Agua','tipo2':'Psíquico','Evolucion':1,'gen':1},
  {'nombre':'Slowbro','tipo1':'Agua','tipo2':'Psíquico','Evolucion':2,'gen':1},
  {'nombre':'Magnemite','tipo1':'Eléctrico','tipo2':'Acero','Evolucion':1,'gen':1},
  {'nombre':'Magneton','tipo1':'Eléctrico','tipo2':'Acero','Evolucion':2,'gen':1},
  {'nombre':'Farfetchd','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Doduo','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Dodrio','tipo1':'Normal','tipo2':'Volador','Evolucion':2,'gen':1},
  {'nombre':'Seel','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Dewgong','tipo1':'Agua','tipo2':'Hielo','Evolucion':2,'gen':1},
  {'nombre':'Grimer','tipo1':'Veneno','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Muk','tipo1':'Veneno','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Cloyster','tipo1':'Agua','tipo2':'Hielo','Evolucion':2,'gen':1},
  {'nombre':'Gastly','tipo1':'Fantasma','tipo2':'Veneno','Evolucion':1,'gen':1},
  {'nombre':'Haunter','tipo1':'Fantasma','tipo2':'Veneno','Evolucion':2,'gen':1},
  {'nombre':'Gengar','tipo1':'Fantasma','tipo2':'Veneno','Evolucion':3,'gen':1},
  {'nombre':'Onix','tipo1':'Roca','tipo2':'Tierra','Evolucion':1,'gen':1},
  {'nombre':'Drowzee','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Hypno','tipo1':'Psíquico','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Krabby','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Kingler','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Voltorb','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Electrode','tipo1':'Eléctrico','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Exeggcute','tipo1':'Planta','tipo2':'Psíquico','Evolucion':1,'gen':1},
  {'nombre':'Exeggutor','tipo1':'Planta','tipo2':'Psíquico','Evolucion':2,'gen':1},
  {'nombre':'Cubone','tipo1':'Tierra','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Marowak','tipo1':'Tierra','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Hitmonlee','tipo1':'Lucha','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Hitmonchan','tipo1':'Lucha','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Kofing','tipo1':'Veneno','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Weezing','tipo1':'Veneno','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Rhyhorn','tipo1':'Tierra','tipo2':'Roca','Evolucion':1,'gen':1},
  {'nombre':'Rhydon','tipo1':'Tierra','tipo2':'Roca','Evolucion':2,'gen':1},
  {'nombre':'Chansey','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Tangela','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Kangaskhan','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Horsea','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Seadra','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Goldeen','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Seaking','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Staryu','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Starmine','tipo1':'Agua','tipo2':'Psíquico','Evolucion':2,'gen':1},
  {'nombre':'Mr. Mime','tipo1':'Psíquico','tipo2':'Hada','Evolucion':1,'gen':1},
  {'nombre':'Scyther','tipo1':'Bicho','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Jynx','tipo1':'Hielo','tipo2':'Psíquico','Evolucion':1,'gen':1},
  {'nombre':'Electabuzz','tipo1':'Eléctrico','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Magmar','tipo1':'Fuego','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Pinsir','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Tauros','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Magikarp','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Gyarados','tipo1':'Agua','tipo2':'Volador','Evolucion':2,'gen':1},
  {'nombre':'Lapras','tipo1':'Agua','tipo2':'Hielo','Evolucion':1,'gen':1},
  {'nombre':'Ditto','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Eevee','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Vaporeon','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Jolteon','tipo1':'Eléctrico','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Flareon','tipo1':'Fuego','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Porygon','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Omanyte','tipo1':'Roca','tipo2':'Agua','Evolucion':1,'gen':1},
  {'nombre':'Omastar','tipo1':'Roca','tipo2':'Agua','Evolucion':2,'gen':1},
  {'nombre':'Kabuto','tipo1':'Roca','tipo2':'Agua','Evolucion':1,'gen':1},
  {'nombre':'Kabutops','tipo1':'Roca','tipo2':'Agua','Evolucion':2,'gen':1},
  {'nombre':'Aerodactyl','tipo1':'Roca','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Snorlax','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Articuno','tipo1':'Hielo','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Zapdos','tipo1':'Eléctrico','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Moltres','tipo1':'Fuego','tipo2':'Volador','Evolucion':1,'gen':1},
  {'nombre':'Dratini','tipo1':'Dragón','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Dragonair','tipo1':'Dragón','tipo2':' ','Evolucion':2,'gen':1},
  {'nombre':'Dragonite','tipo1':'Dragón','tipo2':'Volaor','Evolucion':3,'gen':1},
  {'nombre':'Mewtwo','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Mew','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Lickitung','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':1},
  {'nombre':'Chikorita','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Bayleef','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Meganium','tipo1':'Planta','tipo2':' ','Evolucion':3,'gen':2},
  {'nombre':'Cyndaquil','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Quilava','tipo1':'Fuego','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Typhlosion','tipo1':'Fuego','tipo2':' ','Evolucion':3,'gen':2},
  {'nombre':'Totodile','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Croconaw','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Feraligatr','tipo1':'Agua','tipo2':' ','Evolucion':3,'gen':2},
  {'nombre':'Sentret','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Furret','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Hoothoot','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Noctowl','tipo1':'Normal','tipo2':'Volador','Evolucion':2,'gen':2},
  {'nombre':'Ledyba','tipo1':'Bicho','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Ledian','tipo1':'Bicho','tipo2':'Volador','Evolucion':2,'gen':2},
  {'nombre':'Spinarak','tipo1':'Bicho','tipo2':'Veneno','Evolucion':1,'gen':2},
  {'nombre':'Ariados','tipo1':'Bicho','tipo2':'Veneno','Evolucion':2,'gen':2},
  {'nombre':'Crobat','tipo1':'Veneno','tipo2':'Volador','Evolucion':3,'gen':2},
  {'nombre':'Chinchou','tipo1':'Agua','tipo2':'Eléctrico','Evolucion':1,'gen':2},
  {'nombre':'Lanturn','tipo1':'Agua','tipo2':'Eléctrico','Evolucion':2,'gen':2},
  {'nombre':'Pichu','tipo1':'ELéctrico','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Cleffa','tipo1':'Hada','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Igglybuff','tipo1':'Normal','tipo2':'Hada','Evolucion':1,'gen':2},
  {'nombre':'Togepi','tipo1':'Hada','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Togetic','tipo1':'Hada','tipo2':'Volador','Evolucion':2,'gen':2},
  {'nombre':'Natu','tipo1':'Psíquico','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Xatu','tipo1':'Psíquico','tipo2':'Volador','Evolucion':2,'gen':2},
  {'nombre':'Mareep','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Flaaffy','tipo1':'Eléctrico','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Ampharos','tipo1':'Eléctrico','tipo2':' ','Evolucion':3,'gen':2},
  {'nombre':'Bellossom','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Marill','tipo1':'Agua','tipo2':'Hada','Evolucion':1,'gen':2},
  {'nombre':'Azumarill','tipo1':'Agua','tipo2':'Hada','Evolucion':2,'gen':2},
  {'nombre':'Sudowoodo','tipo1':'Roca','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Politoed','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Hoppip','tipo1':'Planta','tipo2':'Volaor','Evolucion':1,'gen':2},
  {'nombre':'Skiploom','tipo1':'Planta','tipo2':'Volador','Evolucion':2,'gen':2},
  {'nombre':'Jumpluff','tipo1':'Planta','tipo2':'Volador','Evolucion':3,'gen':2},
  {'nombre':'Aipom','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Sunkern','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Sunflora','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Yanma','tipo1':'Bicho','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Wooper','tipo1':'Agua','tipo2':'Tierra','Evolucion':1,'gen':2},
  {'nombre':'Quagsire','tipo1':'Agua','tipo2':'Tierra','Evolucion':2,'gen':2},
  {'nombre':'Espeon','tipo1':'Psíquico','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Umbreon','tipo1':'Siniestro','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Murkrow','tipo1':'Sinestro','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Slowking','tipo1':'Agua','tipo2':'Psíquico','Evolucion':3,'gen':2},
  {'nombre':'Misdreavus','tipo1':'Fantasma','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Unown','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Wobbuffet','tipo1':'Psíqico','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Girafarig','tipo1':'Normal','tipo2':'Psíquico','Evolucion':1,'gen':2},
  {'nombre':'Pineco','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Forretress','tipo1':'Bicho','tipo2':'Acero','Evolucion':2,'gen':2},
  {'nombre':'Dunsparce','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Gligar','tipo1':'Tierra','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Steelix','tipo1':'Acero','tipo2':'Tierra','Evolucion':2,'gen':2},
  {'nombre':'Snubbull','tipo1':'Hada','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Granbull','tipo1':'Hada','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Qwilfish','tipo1':'Agua','tipo2':'Veneno','Evolucion':1,'gen':2},
  {'nombre':'Scizor','tipo1':'Bicho','tipo2':'Acero','Evolucion':2,'gen':2},
  {'nombre':'Shuckle','tipo1':'Bicho','tipo2':'Roca','Evolucion':1,'gen':2},
  {'nombre':'Heracross','tipo1':'Bicho','tipo2':'Lucha','Evolucion':1,'gen':2},
  {'nombre':'Sneasel','tipo1':'Siniestro','tipo2':'Hielo','Evolucion':1,'gen':2},
  {'nombre':'Teddiursa','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Ursaring','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Slugma','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Magcargo','tipo1':'Fuego','tipo2':'Roca','Evolucion':2,'gen':2},
  {'nombre':'Swinub','tipo1':'Hielo','tipo2':'Tierra','Evolucion':1,'gen':2},
  {'nombre':'Piloswine','tipo1':'Hielo','tipo2':'Tierra','Evolucion':2,'gen':2},
  {'nombre':'Corsola','tipo1':'Agua','tipo2':'Roca','Evolucion':1,'gen':2},
  {'nombre':'Remoraid','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Octillery','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Delibird','tipo1':'Hielo','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Mantine','tipo1':'Agua','tipo2':'Volador','Evolucion':2,'gen':2},
  {'nombre':'Skarmory','tipo1':'Acero','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Houndour','tipo1':'Siniestro','tipo2':'Fuego','Evolucion':1,'gen':2},
  {'nombre':'Houndoom','tipo1':'Siniestro','tipo2':'Fuego','Evolucion':2,'gen':2},
  {'nombre':'Kingdra','tipo1':'Agua','tipo2':'Dragón','Evolucion':3,'gen':2},
  {'nombre':'Phanpy','tipo1':'Tierra','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Donphan','tipo1':'Tierra','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Porygon2','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Stantler','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Smeargle','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Tyrogue','tipo1':'Lucha','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Hitmontop','tipo1':'Lucha','tipo2':' ','Evolucion':2,'gen':2},
  {'nombre':'Smoochum','tipo1':'Hielo','tipo2':'Psíquico','Evolucion':1,'gen':2},
  {'nombre':'Elekid','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Magby','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Miltank','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Blissey','tipo1':'Normal','tipo2':' ','Evolucion':3,'gen':2},
  {'nombre':'Raikou','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Entei','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Suicune','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':2},
  {'nombre':'Larvitar','tipo1':'Roca','tipo2':'Tierra','Evolucion':1,'gen':2},
  {'nombre':'Pupitar','tipo1':'Roca','tipo2':'Tierra','Evolucion':2,'gen':2},
  {'nombre':'Tyranitar','tipo1':'Roca','tipo2':'Siniestro','Evolucion':3,'gen':2},
  {'nombre':'Lugia','tipo1':'Psíquico','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Ho-Oh','tipo1':'Fuego','tipo2':'Volador','Evolucion':1,'gen':2},
  {'nombre':'Celebi','tipo1':'Psíquico','tipo2':'Planta','Evolucion':1,'gen':2},
  {'nombre':'Treecko','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Grovyle','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Sceptile','tipo1':'Planta','tipo2':' ','Evolucion':3,'gen':3},
  {'nombre':'Torchic','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Combusken','tipo1':'Fuego','tipo2':'Lucha','Evolucion':2,'gen':3},
  {'nombre':'Blaziken','tipo1':'Fuego','tipo2':'Lucha','Evolucion':3,'gen':3},
  {'nombre':'Mudkip','tipo1':'Agua','tipo2':'Tierra','Evolucion':1,'gen':3},
  {'nombre':'Marshtomp','tipo1':'Agua','tipo2':'Tierra','Evolucion':2,'gen':3},
  {'nombre':'Swampert','tipo1':'Agua','tipo2':'Tierra','Evolucion':3,'gen':3},
  {'nombre':'Poochyena','tipo1':'Siniestro','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Mightyena','tipo1':'Siniestro','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Zigzagoon','tipo1':'Siniestro','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Linoone','tipo1':'Siniestro','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Wurmmple','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Silcoon','tipo1':'Biccho','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Beautifly','tipo1':'Bicho','tipo2':'Volador','Evolucion':3,'gen':3},
  {'nombre':'Cascoon','tipo1':'Bicho','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Dustox','tipo1':'Bicho','tipo2':'Veneno','Evolucion':3,'gen':3},
  {'nombre':'Lotad','tipo1':'Agua','tipo2':'Planta','Evolucion':1,'gen':3},
  {'nombre':'Lombre','tipo1':'Agua','tipo2':'Planta','Evolucion':2,'gen':3},
  {'nombre':'Ludicolo','tipo1':'Agua','tipo2':'Planta','Evolucion':3,'gen':3},
  {'nombre':'Seedot','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Nuzleaf','tipo1':'Planta','tipo2':'Siniestro','Evolucion':2,'gen':3},
  {'nombre':'Shiftry','tipo1':'Planta','tipo2':'Siniestro','Evolucion':3,'gen':3},
  {'nombre':'Taillow','tipo1':'Normal','tipo2':'Volador','Evolucion':2,'gen':3},
  {'nombre':'Swellow','tipo1':'Normal','tipo2':'Volador','Evolucion':2,'gen':3},
  {'nombre':'Wingull','tipo1':'Agua','tipo2':'Volador','Evolucion':1,'gen':3},
  {'nombre':'Pelipper','tipo1':'Agua','tipo2':'Volador','Evolucion':2,'gen':3},
  {'nombre':'Ralts','tipo1':'Psíquico','tipo2':'Hada','Evolucion':1,'gen':3},
  {'nombre':'Kirlia','tipo1':'Psíquico','tipo2':'Hada','Evolucion':2,'gen':3},
  {'nombre':'Gardevoir','tipo1':'Psíquico','tipo2':'Hada','Evolucion':3,'gen':3},
  {'nombre':'Surskit','tipo1':'Bicho','tipo2':'Agua','Evolucion':1,'gen':3},
  {'nombre':'Masquerain','tipo1':'Bicho','tipo2':'Volador','Evolucion':2,'gen':3},
  {'nombre':'Shroomish','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Breelom','tipo1':'Planta','tipo2':'Lucha','Evolucion':2,'gen':3},
  {'nombre':'Slakoth','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Vigoroth','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Slaking','tipo1':'Normal','tipo2':' ','Evolucion':3,'gen':3},
  {'nombre':'Nincada','tipo1':'Bicho','tipo2':'Tierra','Evolucion':1,'gen':3},
  {'nombre':'Ninjask','tipo1':'Bicho','tipo2':'Volador','Evolucion':2,'gen':3},
  {'nombre':'Shediinja','tipo1':'Bicho','tipo2':'Fantasma','Evolucion':2,'gen':3},
  {'nombre':'Whismur','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Loudred','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Exploud','tipo1':'Normal','tipo2':' ','Evolucion':3,'gen':3},
  {'nombre':'Makuhita','tipo1':'Lucha','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Hariyama','tipo1':'Lucha','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Azurill','tipo1':'Normal','tipo2':'Hada','Evolucion':1,'gen':3},
  {'nombre':'Nosepass','tipo1':'Roca','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Skitty','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Delcatty','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Sableye','tipo1':'Siniestro','tipo2':'Fantasma','Evolucion':1,'gen':3},
  {'nombre':'Mawile','tipo1':'Acero','tipo2':'Hada','Evolucion':1,'gen':3},
  {'nombre':'Aron','tipo1':'Acero','tipo2':'Roca','Evolucion':1,'gen':3},
  {'nombre':'Lairon','tipo1':'Acero','tipo2':'Roca','Evolucion':2,'gen':3},
  {'nombre':'Aggronn','tipo1':'Acero','tipo2':'Roca','Evolucion':3,'gen':3},
  {'nombre':'Meditite','tipo1':'Lucha','tipo2':'Psíquico','Evolucion':1,'gen':3},
  {'nombre':'Medicham','tipo1':'Lucha','tipo2':'Psíquico','Evolucion':2,'gen':3},
  {'nombre':'Electrike','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Manectric','tipo1':'Eléctrico','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Plusle','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Minun','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Volbeat','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Illumise','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Roselia','tipo1':'Planta','tipo2':'Veneno','Evolucion':1,'gen':3},
  {'nombre':'Gulpin','tipo1':'Veneno','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Swalot','tipo1':'Veneno','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Carvanha','tipo1':'Agua','tipo2':'Siniestro','Evolucion':1,'gen':3},
  {'nombre':'Sharpedo','tipo1':'Agua','tipo2':'Siniestro','Evolucion':2,'gen':3},
  {'nombre':'Wailmer','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Wailord','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Numel','tipo1':'Fuego','tipo2':'Tierra','Evolucion':1,'gen':3},
  {'nombre':'Camerupt','tipo1':'Fuego','tipo2':'Tierra','Evolucion':2,'gen':3},
  {'nombre':'Torkoal','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Spoink','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Grumpig','tipo1':'Psíquico','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Spinda','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Trapinch','tipo1':'Tierra','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Vibrava','tipo1':'Tierra','tipo2':'Dragón','Evolucion':2,'gen':3},
  {'nombre':'Flygon','tipo1':'Tierra','tipo2':'Dragón','Evolucion':3,'gen':3},
  {'nombre':'Cacnea','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Cacturne','tipo1':'Siniestro','tipo2':'Planta','Evolucion':2,'gen':3},
  {'nombre':'Swablu','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':3},
  {'nombre':'Altaria','tipo1':'Dragón','tipo2':'Volador','Evolucion':2,'gen':3},
  {'nombre':'Zangoose','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Seviper','tipo1':'Veneno','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Lunatone','tipo1':'Roca','tipo2':'Psíquico','Evolucion':1,'gen':3},
  {'nombre':'Solrock','tipo1':'Roca','tipo2':'Psíquico','Evolucion':1,'gen':3},
  {'nombre':'Barboach','tipo1':'Agua','tipo2':'Tierra','Evolucion':1,'gen':3},
  {'nombre':'Whiscash','tipo1':'Agua','tipo2':'Tierra','Evolucion':2,'gen':3},
  {'nombre':'Corphish','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Crawdaunt','tipo1':'Agua','tipo2':'Siniestro','Evolucion':2,'gen':3},
  {'nombre':'Baltoy','tipo1':'Tierra','tipo2':'Psíquico','Evolucion':1,'gen':3},
  {'nombre':'Claydol','tipo1':'Tierra','tipo2':'Psíquico','Evolucion':2,'gen':3},
  {'nombre':'Lileep','tipo1':'Roca','tipo2':'Planta','Evolucion':1,'gen':3},
  {'nombre':'Cradly','tipo1':'Roca','tipo2':'Planta','Evolucion':2,'gen':3},
  {'nombre':'Anorith','tipo1':'Roca','tipo2':'Bicho','Evolucion':1,'gen':3},
  {'nombre':'Armaldo','tipo1':'Roca','tipo2':'Bicho','Evolucion':2,'gen':3},
  {'nombre':'Feebas','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Milotic','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Castform','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Keckleon','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Shuppet','tipo1':'Fantasma','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Banette','tipo1':'Fantasma','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Duskull','tipo1':'Fantasma','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Dusclops','tipo1':'Fantasma','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Tropius','tipo1':'Planta','tipo2':'Volador','Evolucion':1,'gen':3},
  {'nombre':'Chimecho','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Absol','tipo1':'Siniestro','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Wynaut','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Snorunt','tipo1':'Hielo','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Glalie','tipo1':'Hielo','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Spheal','tipo1':'Hielo','tipo2':'Agua','Evolucion':1,'gen':3},
  {'nombre':'Sealeo','tipo1':'Hielo','tipo2':'Agua','Evolucion':2,'gen':3},
  {'nombre':'Walrein','tipo1':'Hielo','tipo2':'Agua','Evolucion':3,'gen':3},
  {'nombre':'Clamperl','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Huntail','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Gorebyss','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Relicanth','tipo1':'Agua','tipo2':'Roca','Evolucion':1,'gen':3},
  {'nombre':'Luvdisc','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Bagon','tipo1':'Dragón','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Shelgon','tipo1':'Dragón','tipo2':' ','Evolucion':2,'gen':3},
  {'nombre':'Salamence','tipo1':'Dragón','tipo2':'Volador','Evolucion':3,'gen':3},
  {'nombre':'Beldum','tipo1':'Acero','tipo2':'Psíquicoo','Evolucion':1,'gen':3},
  {'nombre':'Metang','tipo1':'Acero','tipo2':'Psíquico','Evolucion':2,'gen':3},
  {'nombre':'Metagross','tipo1':'Acero','tipo2':'Psíquico','Evolucion':3,'gen':3},
  {'nombre':'Regirock','tipo1':'Roca','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Regice','tipo1':'Hielo','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Registeel','tipo1':'Acero','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Latias','tipo1':'Dragón','tipo2':'Psíquico','Evolucion':1,'gen':3},
  {'nombre':'Latios','tipo1':'Dragón','tipo2':'Psíquico','Evolucion':1,'gen':3},
  {'nombre':'Kyogre','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Groudon','tipo1':'Tierra','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Rayquaza','tipo1':'Dragón','tipo2':'Volador','Evolucion':1,'gen':3},
  {'nombre':'Jirachi','tipo1':'Acero','tipo2':'Psíquico','Evolucion':1,'gen':3},
  {'nombre':'Deoxys','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':3},
  {'nombre':'Turtwig','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Grotle','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Torterra','tipo1':'Planta','tipo2':'Tierra','Evolucion':3,'gen':4},
  {'nombre':'Chimchar','tipo1':'Fuego','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Monferno','tipo1':'Fuego','tipo2':'Lucha','Evolucion':2,'gen':4},
  {'nombre':'Infernape','tipo1':'Fuego','tipo2':'Lucha','Evolucion':3,'gen':4},
  {'nombre':'Piplup','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Prinplup','tipo1':'Agua','tipo2':'','Evolucion':2,'gen':4},
  {'nombre':'Empoleon','tipo1':'Agua','tipo2':'Acero','Evolucion':3,'gen':4},
  {'nombre':'Starly','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':4},
  {'nombre':'Staravia','tipo1':'Normal','tipo2':'Volador','Evolucion':2,'gen':4},
  {'nombre':'Staraptor','tipo1':'Normal','tipo2':'Volador','Evolucion':3,'gen':4},
  {'nombre':'Bidoof','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Bibarel','tipo1':'Normal','tipo2':'Agua','Evolucion':2,'gen':4},
  {'nombre':'Kricketot','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Kricketune','tipo1':'Bicho','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Shinx','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Luxio','tipo1':'Eléctrico','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Luxray','tipo1':'Eléctrico','tipo2':' ','Evolucion':3,'gen':4},
  {'nombre':'Budew','tipo1':'Planta','tipo2':'Veneno','Evolucion':1,'gen':4},
  {'nombre':'Roserade','tipo1':'Planta','tipo2':'Veneno','Evolucion':3,'gen':4},
  {'nombre':'Cranidos','tipo1':'Roca','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Rampardos','tipo1':'Roca','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Shieldon','tipo1':'Roca','tipo2':'Acero','Evolucion':1,'gen':4},
  {'nombre':'Bastiodon','tipo1':'Roca','tipo2':'Acero','Evolucion':2,'gen':4},
  {'nombre':'Burmy','tipo1':'Bicho','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Wormadam(verde)','tipo1':'Bicho','tipo2':'Planta','Evolucion':2,'gen':4},
  {'nombre':'Wormadam(marron)','tipo1':'Bicho','tipo2':'Tierra','Evolucion':2,'gen':4},
  {'nombre':'Wormadam(rosa)','tipo1':'Bicho','tipo2':'Acero','Evolucion':2,'gen':4},
  {'nombre':'Mothim','tipo1':'Bicho','tipo2':'Volador','Evolucion':3,'gen':4},
  {'nombre':'Combee','tipo1':'Bicho','tipo2':'Volador','Evolucion':1,'gen':4},
  {'nombre':'Vespiquen','tipo1':'Bicho','tipo2':'Volador','Evolucion':2,'gen':4},
  {'nombre':'Pachirisu','tipo1':'Eléctrico','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Buizel','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Floatzel','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Cherubi','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Cherrim','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Shellos','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Gastrodon','tipo1':'Agua','tipo2':'Tierra','Evolucion':2,'gen':4},
  {'nombre':'Ambipom','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Drifloon','tipo1':'Fantasma','tipo2':'Volador','Evolucion':1,'gen':4},
  {'nombre':'Drifblim','tipo1':'Fantasma','tipo2':'Volador','Evolucion':2,'gen':4},
  {'nombre':'Buneary','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Lopunny','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Mismagius','tipo1':'Fantasma','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Honchkrow','tipo1':'Siniestro','tipo2':'Volador','Evolucion':2,'gen':4},
  {'nombre':'Glameow','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Purugly','tipo1':'Normal','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Chingling','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Stunky','tipo1':'Veneno','tipo2':'Siniestro','Evolucion':1,'gen':4},
  {'nombre':'Skuntank','tipo1':'Veneno','tipo2':'Siniestro','Evolucion':2,'gen':4},
  {'nombre':'Bronzor','tipo1':'Acero','tipo2':'Psíquico','Evolucion':1,'gen':4},
  {'nombre':'Bronzong','tipo1':'Acero','tipo2':'Psíquico','Evolucion':2,'gen':4},
  {'nombre':'Bonsly','tipo1':'Roca','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Mime Jr','tipo1':'Psíquico','tipo2':'Hada','Evolucion':1,'gen':4},
  {'nombre':'Happiny','tipo1':'Normal','tipo2':' ','Evolucion':1 ,'gen':4},
  {'nombre':'Chatot','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':4},
  {'nombre':'Spiritomb','tipo1':'Fantasma','tipo2':'Siniestro','Evolucion':1,'gen':4},
  {'nombre':'Gible','tipo1':'Dragón','tipo2':'Tierra','Evolucion':1,'gen':4},
  {'nombre':'Gabite','tipo1':'Dragón','tipo2':'Tierra','Evolucion':2,'gen':4},
  {'nombre':'Garchomp','tipo1':'Dragón','tipo2':'Tierra','Evolucion':3,'gen':4},
  {'nombre':'Munchlax','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Riolu','tipo1':'Lucha','tipo2':'Acero','Evolucion':1,'gen':4},
  {'nombre':'Lucario','tipo1':'Lucha','tipo2':'Acero','Evolucion':2,'gen':4},
  {'nombre':'Hippopotas','tipo1':'Tierra','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Hippowdon','tipo1':'Tierra','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Skorupi','tipo1':'Veneno','tipo2':'Bicho','Evolucion':1,'gen':4},
  {'nombre':'Drapion','tipo1':'Veneno','tipo2':'Siniestro','Evolucion':2,'gen':4},
  {'nombre':'Croagunk','tipo1':'Veneno','tipo2':'Lucha','Evolucion':1,'gen':4},
  {'nombre':'Toxicroak','tipo1':'Veneno','tipo2':'Lucha','Evolucion':2,'gen':4},
  {'nombre':'Carnivine','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Finneon','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Lumineon','tipo1':'Agua','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Mantyke','tipo1':'Agua','tipo2':'Volador','Evolucion':1,'gen':4},
  {'nombre':'Snover','tipo1':'Planta','tipo2':'Hielo','Evolucion':1,'gen':4},
  {'nombre':'Abomasnow','tipo1':'Planta','tipo2':'Hielo','Evolucion':2,'gen':4},
  {'nombre':'Weavile','tipo1':'Siniestro','tipo2':'Hielo','Evolucion':2,'gen':4},
  {'nombre':'Magnezone','tipo1':'Eléctrico','tipo2':'Acero','Evolucion':3,'gen':4},
  {'nombre':'Lickilicky','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Rhyperior','tipo1':'Tierra','tipo2':'Roca','Evolucion':3,'gen':4},
  {'nombre':'Tangrowth','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Electivire','tipo1':'Eléctrico','tipo2':' ','Evolucion':3,'gen':4},
  {'nombre':'Magmortar','tipo1':'Fuego','tipo2':' ','Evolucion':3,'gen':4},
  {'nombre':'Togekiss','tipo1':'Hada','tipo2':'Volador','Evolucion':3,'gen':4},
  {'nombre':'Yanmega','tipo1':'Bicho','tipo2':'Volador','Evolucion':2,'gen':4},
  {'nombre':'Leafeon','tipo1':'Planta','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Glaceon','tipo1':'Hielo','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Gliscor','tipo1':'Tierra','tipo2':'Volador','Evolucion':2,'gen':4},
  {'nombre':'Mamoswine','tipo1':'Hielo','tipo2':'Tierra','Evolucion':3,'gen':4},
  {'nombre':'Porygon-Z','tipo1':'Normal','tipo2':' ','Evolucion':3,'gen':4},
  {'nombre':'Gallade','tipo1':'Psíquico','tipo2':'Lucha','Evolucion':3,'gen':4},
  {'nombre':'Probopass','tipo1':'Roca','tipo2':'Acero','Evolucion':2,'gen':4},
  {'nombre':'Dusknoir','tipo1':'Fantasma','tipo2':' ','Evolucion':2,'gen':4},
  {'nombre':'Froslass','tipo1':'Hielo','tipo2':'Fantasma','Evolucion':2,'gen':4},
  {'nombre':'Rotom','tipo1':'Eléctrico','tipo2':'Fantasma','Evolucion':1,'gen':4},
  {'nombre':'Rotom_Horno','tipo1':'Eléctrico','tipo2':'Fuego','Evolucion':1,'gen':4},
  {'nombre':'Rotom_Lavadora','tipo1':'Eléctrico','tipo2':'Agua','Evolucion':1,'gen':4},
  {'nombre':'Rotom_Nevera','tipo1':'Eléctrico','tipo2':'Hielo','Evolucion':1,'gen':4},
  {'nombre':'Rotom_Ventilador','tipo1':'Eléctrico','tipo2':'Volador','Evolucion':1,'gen':4},
  {'nombre':'Rotom_Cortacesped','tipo1':'Eléctrico','tipo2':'Planta','Evolucion':1,'gen':4},
  {'nombre':'Uxie','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Mesprit','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Azelf','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Dialga','tipo1':'Acero','tipo2':'Dragón','Evolucion':1,'gen':4},
  {'nombre':'Palkia','tipo1':'Agua','tipo2':'Dragón','Evolucion':1,'gen':4},
  {'nombre':'Heatran','tipo1':'Fuego','tipo2':'Acero','Evolucion':1,'gen':4},
  {'nombre':'Regigigas','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Giratina','tipo1':'Fantasma','tipo2':'Dragón','Evolucion':1,'gen':4},
  {'nombre':'Cresselia','tipo1':'Psíquico','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Phione','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Manaphy','tipo1':'Agua','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Darkrai','tipo1':'Siniestro','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Shaymin_Base','tipo1':'Planta','tipo2':' ','Evolucion':1,'gen':4},
  {'nombre':'Shaymin','tipo1':'Normal','tipo2':'Volador','Evolucion':1,'gen':4},
  {'nombre':'Arceus','tipo1':'Normal','tipo2':' ','Evolucion':1,'gen':4},
]


lista_tipos = ['Agua','Fuego','Planta','Tierra','Roca','Psíquico','Siniestro','Lucha','Fantasma','Veneno','Acero', 'Volador','Bicho','Normal','Hada','Dragón','Hielo','Eléctrico']

def mostrar_lista_pokemons():
  lista_pokemons = []
  for pokemon in pokemon_gen1_2_3_4:
    lista_pokemons.append(pokemon['nombre'])
  return lista_pokemons

def jugar_Pokedle():
  numero_pokemon = random.randint(0,len(pokemon_gen1_2_3_4)+1)
  pokemon_a_adivinar = []
  pokemon_a_adivinar.append(pokemon_gen1_2_3_4[int(numero_pokemon)])
  respuesta = False
  while respuesta != True:
    pokemon_intento = []
    print('Si quieres saber la respuesta correcta escribe: Repuesta')
    intento = input('Dime un pokemon: ')
    if intento == 'Respuesta':
      print(pokemon_a_adivinar[0])
      respuesta = True
    else:
      if intento in mostrar_lista_pokemons():
        for pokemon in pokemon_gen1_2_3_4:
          if pokemon['nombre'] == intento:
            pokemon_intento.append(pokemon['nombre'])
            pokemon_intento.append(pokemon['tipo1'])
            pokemon_intento.append(pokemon['tipo2'])
            pokemon_intento.append(str(pokemon['Evolucion']))
            pokemon_intento.append(str(pokemon['gen']))
                
            if pokemon_intento[0] == pokemon_a_adivinar[0]['nombre']:
              print('Has acertado')
              respuesta = True
            else:
              print('No has acertado')
              respuesta = False
              if pokemon_intento[1] == pokemon_a_adivinar[0]['tipo1']:
                print('El tipo del pokemon es correcto, es tipo ' + pokemon_intento[1])
              else:
                print('El tipo del pokemon no es correcto')
              
              if pokemon_a_adivinar[0]['tipo2'] == ' ':
                print('El pokemon no tiene doble tipo')
              else:
                if pokemon_intento[2] == pokemon_a_adivinar[0]['tipo2']:
                  print('El tipo secundario del pokemon es correcto, es tipo ' + pokemon_intento[2])
                else:
                  print('El tipo secundario del pokemon no es correcto')
              if pokemon_a_adivinar[0]['Evolucion'] == int(pokemon_intento[3]):
                print('La evolucion del pokemon es correcta, es una evolución número '+ pokemon_intento[3])
              else:
                print('La evolución del pokemon no es correcta')
              if pokemon_a_adivinar[0]['gen'] == int(pokemon_intento[4]):
                print('La generación a la que pertenece el pokemon es correcta, pertenece a la generacion '+pokemon_intento[4])
              else:
                print('La generación a la que pertenece el pokemon no es correcta')
      else:
        respuesta = False
        print('El pokemon introducido no existe, está mal escrito o no pertenece a ninguna de las generaciones incluias en la base de datos')
    
def listar_pokemon_de_X_tipo():
  
  tipo_correcto = False
  while tipo_correcto == False:
    tipo = input('Dime el tipo de los pokemon que quieras buscar: ')
    if tipo in lista_tipos:
      lista_pokemon_tipo = []
      for pokemon in pokemon_gen1_2_3_4:
        if pokemon['tipo1'] == tipo or pokemon['tipo2'] == tipo:
          lista_pokemon_tipo.append(pokemon['nombre'])
          tipo_correcto = True
      return lista_pokemon_tipo
    else:
      print('El ipo introducido no existe o está mal escrito, por favor diga alguno de los siguientes tipos')
      i=0
      for tipo in lista_tipos:
        i += 1
        print(f'{i}.{tipo}')

def buscar_pokemon_por_nombre():
  pokemon_encontrados = 0
  pokemon_busqueda = ''
  while pokemon_encontrados == 0:
    busqueda = input('Dime el nombre del pokemon del que quieras ver su información: ')
    for pokemon in pokemon_gen1_2_3_4:
      if pokemon['nombre'] == busqueda:
        pokemon_encontrados += 1
        pokemon_busqueda = pokemon
    if pokemon_encontrados != 0:
      return pokemon_busqueda
    else:
      print('El pokemon introducido no existe o pertenece a una generación que no se ha incluido')

def listar_pokemon_doble_tipo():
  tipo_uno = False
  while tipo_uno == False:
    tipo1 = input('Dime uno de los tipos del pokemon: ')
    if tipo1 in lista_tipos:
      tipo_uno = True
    else:
      print('El tipo introducido no existe o no está bien escrito. Porfavor elija uno de los siguientes tipos')
      i = 0
      for tipo in lista_tipos:
        i += 1
        print(f'{i}.{tipo}')

  tipo_dos = False
  while tipo_dos == False:
    tipo2 = input('Dime el otro tipo del pokemon: ')
    if tipo2 in lista_tipos:
      tipo_dos = True
    else:
      print('El tipo introducido no existe o no está bien escrito. Porfavor elija uno de los siguientes tipos')
      i = 0
      for tipo in lista_tipos:
        i += 1
        print(f'{i}.{tipo}')
        
  lista_pokemon_doble_tipo = []
  for pokemon in pokemon_gen1_2_3_4:
    if pokemon['tipo1'] == tipo1 and pokemon['tipo2'] == tipo2 or pokemon['tipo1'] == tipo2 and pokemon['tipo2'] == tipo1:
      lista_pokemon_doble_tipo.append(pokemon['nombre'])
  return lista_pokemon_doble_tipo


def listar_pokemon_por_generacion():
  accion = False
  while accion == False:
    generacion = int(input('Dime la generación de la que quieres ver sus pokemon: '))
    
    if generacion == 1:
      lista_gen1 = []
      for pokemon in pokemon_gen1_2_3_4:
        if pokemon['gen'] == generacion:
          lista_gen1.append(pokemon['nombre'])
      accion = True
      return lista_gen1
    elif generacion == 2:
      int(generacion)
      lista_gen2 = []
      for pokemon in pokemon_gen1_2_3_4:
        if pokemon['gen'] == generacion:
          lista_gen2.append(pokemon['nombre'])
      accion = True
      return lista_gen2
    elif generacion == 3:
      lista_gen3 = []
      for pokemon in pokemon_gen1_2_3_4:
        if pokemon['gen'] == generacion:
          lista_gen3.append(pokemon['nombre'])
      accion = True
    elif generacion == 4:
      lista_gen4 = []
      for pokemon in pokemon_gen1_2_3_4:
        if pokemon['gen'] == generacion:
          lista_gen4.append(pokemon['nombre'])
      return lista_gen4
    else:
      print('Los datos introducidos no son correctos, porfavor introduzc un numero comprendido entre las generaciones incluidas  en la base de datos')
        
def listar_generaciones_específicas():
  lista_generaciones = []
  generacion_correcta = False
  while generacion_correcta == False:
    generaciones = int(input('¿Cuantas generaciones quieres jugar?: '))
    if generaciones < 0 or generaciones >4:
      print('La cantidad de generaciones introducida es mayor a las que contiene la base de datos en su memoria, si quieres jugar a Pokedle con todas las generaciones de la mmoria prueba la opción 2 del menú, "Jugar Pokedle"')
    elif generaciones <5 and generaciones > 0:
      i = 0
      while i < generaciones:
        generacion = int(input('¿Qué generación quieres jugar?: '))
        if generacion <5 and generacion >0:
          for pokemon in pokemon_gen1_2_3_4:
            if pokemon['gen'] == generacion:
              lista_generaciones.append(pokemon)
          i += 1
        else:
          print('La generación introucida no existe, no está bien escrita o no ha sido introducida aún en la base de datos')
           
      generacion_correcta = True
    else:
      print('El valor introducido no es correcto, no está bien escrito o no es compatible con el tipo de información que se le solicita, ingrese un número comprendido entre 1 y 4')
  return lista_generaciones

  
def jugar_pokedle_generaciones_especificas():
  lista = listar_generaciones_específicas()
  numero_pokemon = random.randint(0,len(lista)+1)
  pokemon_a_adivinar = []
  pokemon_a_adivinar.append(lista[int(numero_pokemon)])
  respuesta = False
  while respuesta != True:
    pokemon_intento = []
    print('Si quieres saber la respuesta correcta escribe: Repuesta')
    intento = input('Dime un pokemon: ')
    if intento == 'Respuesta':
      print(pokemon_a_adivinar[0])
      respuesta = True
    else:
      if intento in mostrar_lista_pokemons():
        for pokemon in lista:
          if pokemon['nombre'] == intento:
            pokemon_intento.append(pokemon['nombre'])
            pokemon_intento.append(pokemon['tipo1'])
            pokemon_intento.append(pokemon['tipo2'])
            pokemon_intento.append(str(pokemon['Evolucion']))
            pokemon_intento.append(str(pokemon['gen']))

            if pokemon_intento[0] == pokemon_a_adivinar[0]['nombre']:
              print('Has acertado')
              respuesta = True
            else:
              print('No has acertado')
              respuesta = False
              if pokemon_intento[1] == pokemon_a_adivinar[0]['tipo1']:
                print('El tipo del pokemon es correcto, es tipo ' + pokemon_intento[1])
              else:
                print('El tipo del pokemon no es correcto')

              if pokemon_a_adivinar[0]['tipo2'] == ' ':
                print('El pokemon no tiene doble tipo')
              else:
                if pokemon_intento[2] == pokemon_a_adivinar[0]['tipo2']:
                  print('El tipo secundario del pokemon es correcto, es tipo ' + pokemon_intento[2])
                else:
                  print('El tipo secundario del pokemon no es correcto')
              if pokemon_a_adivinar[0]['Evolucion'] == int(pokemon_intento[3]):
                print('La evolucion del pokemon es correcta, es una evolución número '+ pokemon_intento[3])
              else:
                print('La evolución del pokemon no es correcta')
              if pokemon_a_adivinar[0]['gen'] == int(pokemon_intento[4]):
                print('La generación a la que pertenece el pokemon es correcta, pertenece a la generacion '+pokemon_intento[4])
              else:
                print('La generación a la que pertenece el pokemon no es correcta')
      else:
        respuesta = False
        print('El pokemon introducido no existe, está mal escrito o no pertenece a ninguna de las generaciones incluias en la base de datos')


def mostrar_menu_de_opciones():
  seguir = True
  while seguir == True:
    print("1. Mostrar Pokemones")
    print('2. Jugar Pokedle')
    print('3. Listar pokemon de X tipo')
    print('4. Buscar pokemon por nombre')
    print('5. Buscar pokemon por doble tipo')
    print('6. Listar pokemon por generación')
    print('7. Jugar Pokedle con generaciones a elegir')
    print('8. Salir')
    opcion = int(input('Ingrese una opcion: '))
    if opcion >0 and opcion <9:
      match opcion:
        case 1:
          print(mostrar_lista_pokemons())
        case 2:
          jugar_Pokedle()
        case 3:
          print(listar_pokemon_de_X_tipo())
        case 4:
          print(buscar_pokemon_por_nombre())
        case 5:
          print(listar_pokemon_doble_tipo())
        case 6:
          print(listar_pokemon_por_generacion())
        case 7:
          print(jugar_pokedle_generaciones_especificas())
        case 8:
          seguir = False
    else:
      print('La opción introducida no es válida')

mostrar_menu_de_opciones()
