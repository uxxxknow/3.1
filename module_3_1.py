calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(calls):
    print((len(calls), calls.upper(), calls.lower()))
    count_calls()
string_info('Capybara')
string_info('Armageddon')


def is_contains(calls, list_to_search):
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if calls.lower() in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)