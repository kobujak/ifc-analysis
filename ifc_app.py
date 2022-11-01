
import ifcopenshell.util.element
import pprint as pp

model = ifcopenshell.open('Duplex_A.ifc')

print("1 - Windows 2 - Walls 3 - IfcSpaces")
choice = input('I select: ')

if int(choice) == 1:
    pp.pprint(model.by_type('IfcWindow'))
elif int(choice) == 2:
    pp.pprint(model.by_type('IfcWall'))
elif int(choice) == 3:
    pp.pprint(model.by_type('IfcSpace'))


Walls = model.by_type('IfcWall')
ext_walls = []
wall_num = 0
volume = 0

for w in Walls:
    psets = ifcopenshell.util.element.get_psets(w)
    if psets.get("Pset_WallCommon"):
        if bool(psets.get("Pset_WallCommon").get("IsExternal")):
            ext_walls.append(w)

for wall in ext_walls:
    psets = ifcopenshell.util.element.get_psets(wall)
    wall_num = wall_num + 1
    for psetname, pset_dict in psets.items():
        for name, value in pset_dict.items():
            # print (f'{name}:{value}')
            if name == 'Volume':
                volume += float(value)


print('\n___________________________________________________________________________________________\n')

rooms = model.by_type("IfcSpace")
r = rooms[2]
print("Definicja użytych psetów w pliku ifc dla pomieszczenia o GUID == 0BTBFw6f90Nfh9rP1dl_3P")
print()
pp.pprint(ifcopenshell.util.element.get_psets(r))
pp.pprint(r.get_info())

print('\n___________________________________________________________________________________________\n')

print(f'Liczba ścian w pliku Duplex_A.ifc wynosi {wall_num}, a ich powierzchnia to {volume:.2f}')
