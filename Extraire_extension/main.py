# Exercice : extraire les extensions")
print()
print("##### Exercice : extraire les extensions")

fichiers = ("notepad.exe", "nom.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

# lower/upper
# in / index / for
# split
# -1

def extract_extension(nom_fichier):
    fichier_split = nom_fichier.split(sep=".")
    # print(fichier_split)
    if len(fichier_split) > 1:
        return fichier_split[-1]
    return None

def get_extension_defintion(extention, definition):
    for i in definition_extensions:
        if i[0].lower() == extention.lower():
            return i[1]
    return None

print(fichiers)
print(definition_extensions)

for fichier in fichiers:
    extract = extract_extension(fichier)
    if extract:
        definition = get_extension_defintion(extract, definition_extensions)
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"

    print(fichier, "(" + definition + ")")