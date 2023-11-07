Word=input('Type your word:')
Set1={'Belize','Cambodge','Mexique','Mozambique','Zaïre','Zimbabwe'}
Set2={'A','a','E','e','I','i','O','o','U','u'}
Set3={'Etats-Unis','Pays-Bas'}
if Word in Set1:
    print('le ',Word)
elif Word in Set3:
    print('les',Word)
elif Word[len(Word)-1]=='e':
    print('la ',Word)
elif Word[0] in Set2:
    print("l'",Word)
else:
    print('le',Word)
