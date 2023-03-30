'''
6 kyu

Emotional Sort ( ︶︿︶)
You'll have a function called "sortEmotions" that will return an array of emotions sorted. It has two parameters, the first parameter called "arr" will expect an array of emotions where an emotion will be one of the following:

:D -> Super Happy
:) -> Happy
:| -> Normal
:( -> Sad
T_T -> Super Sad
Example of the array:[ 'T_T', ':D', ':|', ':)', ':(' ]

And the second parameter is called "order", if this parameter is true then the order of the emotions will be descending (from Super Happy to Super Sad) if it's false then it will be ascending (from Super Sad to Super Happy)

Example if order is true with the above array: [ ':D', ':)', ':|', ':(', 'T_T' ]

Super Happy -> Happy -> Normal -> Sad -> Super Sad
If order is false: [ 'T_T', ':(', ':|', ':)', ':D' ]

Super Sad -> Sad -> Normal -> Happy -> Super Happy
Example:

arr = [':D', ':|', ':)', ':(', ':D']
sortEmotions(arr, true) // [ ':D', ':D', ':)', ':|', ':(' ]
sortEmotions(arr, false) // [ ':(', ':|', ':)', ':D', ':D' ]
More in test cases!

Notes:

The array could be empty, in that case return the same empty array ¯\_( ツ )_/¯
All emotions will be valid
Enjoy! (づ｡◕‿‿◕｡)づ
'''

emojis = {
    ":D":0,
    ":)":1,
    ":|":2,
    ":(":3,
    "T_T":4
}


def sort_emotions(arr, order):
    new_list = []
    result = []
    if len(arr)==0:
        return new_list

    for e in arr:
        new_list.append(emojis[e])

    if not order:
        new_list.sort(reverse=True)
    else:
        new_list.sort()

    for index in new_list:
        result += [e for (e, i) in emojis.items() if i==index]
    
    return result

# def sort_emotions(arr, order):
#     return sorted(arr, key=[':D',':)',':|',':(','T_T'].index, reverse=not order)

print(
    sort_emotions([ ':D', 'T_T', ':D', ':(' ], True),
    sort_emotions([ 'T_T', ':D', ':(', ':(' ], False),
    sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], False),
    sort_emotions([], False),
    sort_emotions([], True)
)
