friends = {'Abdulaziz': 13, 'Saidkhoja': 13, 'Umarbek': 11, 'Anonimus': 101010001}

print(friends)

friends['Umarbek'] = 12
print(friends)

friends.pop('Anonimus')
print(friends)

friend = {'Diyor' : 12}
friends.update(friend)
print(friends)