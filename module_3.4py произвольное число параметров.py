def single_root_woords(root_woord, *other_woords):
    same_woords = []
    root_woord_up = root_woord.upper()
    other_woords_up = [i.upper() for i in other_woords]
    for j in range(len(other_woords)):
        if str(root_woord_up) in str(other_woords_up[j]) or str(other_woords_up[j]) in root_woord_up:
            same_woords.append(other_woords[j])
    return same_woords

result1 = single_root_woords('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_woords('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)