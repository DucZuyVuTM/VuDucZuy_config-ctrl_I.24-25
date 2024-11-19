# Изучить основы языка утилиты make

Создать приведенный ниже Makefile и проверить его работоспособность:
```
dress: trousers shoes jacket
	  @echo "All done. Let's go outside!"

trousers: underpants
	  @echo "Putting on trousers."

underpants:
	  @echo "Putting on underpants."

shoes: socks
	  @echo "Putting on shoes."

socks: pullover
	  @echo "Putting on socks."

pullover: shirt
	@echo "Putting on pullover."

shirt:
	  @echo "Putting on shirt."

jacket: pullover
	  @echo "Putting on jacket."
```

![Screenshot 2024-11-19 194050](https://github.com/user-attachments/assets/b34b0a07-c5df-4997-b16b-46eac9078f64)

# Визуализировать граф civgraph.txt

Скрипт на Python:
```py
from graphviz import Source

file_path = 'civgraph.txt'

with open(file_path, 'r') as f:
    dot_data = f.read()

src = Source(dot_data)
src.render('civgraph', format='png')
```

Файл Makefile:
```bash
run:
    python3 graph.py
```

![image](https://github.com/user-attachments/assets/710debf4-e7cb-4b4f-980c-8651c585e555)

![image](https://github.com/user-attachments/assets/56f0bda2-e8f1-458f-95c0-05810d1a1c7e)

# Задача №1

Файл graph_Ex1.py:
```py
import json

def generate_makefile(graph):
    with open('Makefile', 'w') as f:
        for target, deps in graph.items():
            deps_str = ' '.join(deps)
            f.write(f'{target}: {deps_str}\n')
            f.write(f'\t@echo "Building {target}"\n\n')

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    generate_makefile(graph)
    print("Makefile created.")
```

Файл civgraph.json:
```json
{"pottery": [], "irrigation": ["pottery"], "writing": ["pottery"], "animal_husbandry": [], "archery": ["animal_husbandry"], "mining": [], "masonry": ["mining"], "bronze_working": ["mining"], "the_wheel": ["mining"], "apprenticeship": ["mining", "currency", "horseback_riding"], "sailing": [], "celestial_navigation": ["sailing", "astrology"], "shipbuilding": ["sailing"], "astrology": [], "drama_poetry": ["astrology", "irrigation", "masonry", "early_empire", "mysticism"], "theology": ["astrology", "mysticism", "drama_poetry"], "horseback_riding": ["archery"], "machinery": ["archery", "iron_working", "engineering"], "currency": ["writing", "foreign_trade"], "state_workforce": ["writing", "bronze_working", "craftsmanship"], "recorded_history": ["writing", "political_philosophy", "drama_poetry"], "construction": ["masonry", "the_wheel", "horseback_riding"], "engineering": ["masonry", "the_wheel"], "iron_working": ["bronze_working"], "mathematics": ["bronze_working", "celestial_navigation", "currency", "drama_poetry"], "military_training": ["bronze_working", "military_tradition", "games_recreation"], "cartography": ["celestial_navigation", "shipbuilding"], "medieval_faires": ["currency", "feudalism"], "guilds": ["currency", "feudalism", "civil_service"], "mercantilism": ["currency", "humanism"], "stirrups": ["horseback_riding", "feudalism"], "mass_production": ["shipbuilding", "machinery", "education"], "naval_tradition": ["shipbuilding", "defensive_tactics"], "military_tactics": ["mathematics"], "education": ["mathematics", "apprenticeship"], "military_engineering": ["construction", "engineering"], "castles": ["construction", "divine_right", "exploration"], "games_recreation": ["construction", "state_workforce"], "gunpowder": ["apprenticeship", "stirrups", "military_engineering"], "printing": ["machinery", "education"], "metal_casting": ["machinery", "gunpowder"], "banking": ["education", "stirrups", "guilds"], "astronomy": ["education"], "military_science": ["stirrups", "printing", "siege_tactics"], "siege_tactics": ["castles", "metal_casting"], "square_rigging": ["cartography", "gunpowder"], "exploration": ["cartography", "mercenaries", "medieval_faires"], "industrialization": ["mass_production", "square_rigging"], "scientific_theory": ["banking", "astronomy", "the_enlightenment"], "colonialism": ["astronomy", "mercantilism"], "ballistics": ["metal_casting", "siege_tactics"], "economics": ["metal_casting", "scientific_theory"], "scorched_earth": ["metal_casting", "nationalism"], "steam_power": ["industrialization"], "flight": ["industrialization", "scientific_theory", "economics"], "steel": ["industrialization", "rifling"], "class_struggle": ["industrialization", "ideology"], "sanitation": ["scientific_theory", "urbanization"], "rifling": ["ballistics", "military_science"], "totalitarianism": ["military_science", "ideology"], "electricity": ["steam_power", "mercantilism"], "radio": ["steam_power", "flight", "conservation"], "chemistry": ["sanitation"], "suffrage": ["sanitation", "ideology"], "replaceable_parts": ["economics"], "capitalism": ["economics", "mass_media"], "combined_arms": ["flight", "combustion"], "synthetic_materials": ["flight", "plastics"], "rapid_deployment": ["flight", "cold_war"], "advanced_ballistics": ["replaceable_parts", "steel", "electricity"], "combustion": ["steel", "natural_history"], "computers": ["electricity", "radio", "suffrage", "totalitarianism", "class_struggle"], "advanced_flight": ["radio"], "rocketry": ["radio", "chemistry"], "nanotechnology": ["radio", "composites"], "mass_media": ["radio", "urbanization"], "nuclear_program": ["chemistry", "ideology"], "plastics": ["combustion"], "satellites": ["advanced_flight", "rocketry"], "globalization": ["advanced_flight", "rapid_deployment", "space_race"], "guidance_systems": ["rocketry", "advanced_ballistics"], "space_race": ["rocketry", "cold_war"], "nuclear_fission": ["advanced_ballistics", "combined_arms"], "telecommunications": ["computers"], "robotics": ["computers", "globalization"], "lasers": ["nuclear_fission"], "cold_war": ["nuclear_fission", "ideology"], "composites": ["synthetic_materials"], "stealth_technology": ["synthetic_materials"], "social_media": ["telecommunications", "professional_sports", "space_race"], "nuclear_fusion": ["lasers"], "code_of_laws": [], "craftsmanship": ["code_of_laws"], "foreign_trade": ["code_of_laws"], "military_tradition": ["craftsmanship"], "early_empire": ["foreign_trade"], "mysticism": ["foreign_trade"], "political_philosophy": ["state_workforce", "early_empire"], "defensive_tactics": ["games_recreation", "political_philosophy"], "humanism": ["drama_poetry", "medieval_faires"], "mercenaries": ["military_training", "feudalism"], "feudalism": ["defensive_tactics"], "civil_service": ["defensive_tactics", "recorded_history"], "divine_right": ["theology", "civil_service"], "diplomatic_service": ["guilds"], "reformed_church": ["guilds", "divine_right"], "the_enlightenment": ["humanism", "diplomatic_service"], "civil_engineering": ["mercantilism"], "nationalism": ["the_enlightenment"], "opera_ballet": ["the_enlightenment"], "natural_history": ["colonialism"], "urbanization": ["civil_engineering", "nationalism"], "conservation": ["natural_history", "urbanization"], "mobilization": ["urbanization"], "cultural_heritage": ["conservation"], "ideology": ["mass_media", "mobilization"], "professional_sports": ["ideology"]}
```

![civgraph_json](https://github.com/user-attachments/assets/215ddd11-b470-4ad8-98f5-be73f779b9bb)

![image](https://github.com/user-attachments/assets/ab87634b-a6cd-4068-970f-fbd9547a59bb)

Файл Makefile:

![civgraph_makefile](https://github.com/user-attachments/assets/59001d9c-bda1-4a59-8776-60334d50fb50)

# Задача №2

Файл graph_Ex2.py:
```
import json
import os

completed_tasks_file = "task.txt"

def get_all_depends(graph, targetTech):
    depends = set(graph[targetTech])
    for depend in graph[targetTech]:
        for i in get_all_depends(graph, depend):
            depends.add(i)
    return depends


def generate_makefile(graph, targetTech):
    tasks = load_tasks()
    depends = get_all_depends(graph, targetTech)
    tasks.add(targetTech)
    with open('Makefile', 'w') as f:
        result_string = ""
        for target in depends:
            if target not in tasks:
                tasks.add(target)
                result_string += f'\t@echo "Building {target}"\n'
        if result_string != "":
            f.write(f'{target}:\n')
            f.write(result_string)
    save_tasks(tasks)

def load_tasks():
    if os.path.exists(completed_tasks_file):
        with open(completed_tasks_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_tasks(tasks):
    with open(completed_tasks_file, 'w') as f:
        f.write('\n'.join(tasks))

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    target = input('Enter target: ')
    generate_makefile(graph, target)
    print("Makefile created.")
```

![image](https://github.com/user-attachments/assets/27c1eaee-1cb0-473a-85bc-686720efd16c)

# Задача №3

Файл graph_Ex3.py:
```
import json
import os

completed_tasks_file = "task.txt"

def get_all_depends(graph, targetTech):
    depends = set(graph[targetTech])
    for depend in graph[targetTech]:
        for i in get_all_depends(graph, depend):
            depends.add(i)
    return depends


def generate_makefile(graph, targetTech):
    tasks = load_tasks()
    depends = get_all_depends(graph, targetTech)
    tasks.add(targetTech)
    with open('Makefile', 'w') as f:
        result_string = ""
        for target in depends:
            if target not in tasks:
                tasks.add(target)
                result_string += f'\t@echo "Building {target}"\n'
        if result_string != "":
            f.write(f'{target}:\n')
            f.write(result_string)
    save_tasks(tasks)

def load_tasks():
    if os.path.exists(completed_tasks_file):
        with open(completed_tasks_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_tasks(tasks):
    with open(completed_tasks_file, 'w') as f:
        f.write('\n'.join(tasks))

def clean():
    if os.path.exists(completed_tasks_file):
        os.remove(completed_tasks_file)
        print("Cleaned completed tasks.")

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    target = input('Enter target: ')
    if target == "clean":
        clean()
    else:
        generate_makefile(graph, target)
        print("Makefile created.")
```

![image](https://github.com/user-attachments/assets/51acb3ca-e9e4-4070-a24b-431686fb629f)

Файл task.txt удален с помощью цели clean:

![image](https://github.com/user-attachments/assets/119e26d9-2041-47c5-b5a9-7deba408fdd3)

# Задача №4

Файл prog.c:
```c
#include <stdio.h>
#include "data.h"

int main() {
    printf("Hello, World!\n");
    print_data();
    return 0;
}
```

Файл data.c:
```c
#include <stdio.h>

void print_data() {
    printf("This is data from data.c\n");
}
```

Файл data.h:
```c
#ifndef DATA_H
#define DATA_H

void print_data();

#endif
```

Файл Makefile:
```
CC = gcc

TARGET = prog

SOURCES = prog.c data.c
OBJECTS = $(SOURCES:.c=.o)

all: $(TARGET) files.lst archive

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@

files.lst:
	ls > files.lst

archive: files.lst
	zip distr.zip *.*

%.o: %.c
	$(CC) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJECTS) files.lst distr.zip
```

![image](https://github.com/user-attachments/assets/11c69d97-eb84-4647-a1bc-0139820435a2)
![image](https://github.com/user-attachments/assets/4f901376-8085-48f3-9c91-db4035aa605e)
