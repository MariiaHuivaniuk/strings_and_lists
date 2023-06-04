print('task1')
def is_plural (word):
    words = str(word)
    if words.endswith('s'):
        return True
    else:
        return False


print(is_plural("fvfdv"))

print('task2')
def stutter (word):
    if len(word) < 2:
        return word
    stuttered_word = word[:2] + "..." + word[:2] + "..." + word + "?"
    return stuttered_word


input_word = input("Введіть слово ")
stutterd_word = stutter(input_word.lower())
print(stutterd_word)

print('task3')
def index_of_caps(word):
    indices = []
    for i in range(len(word)):
        if word[i].isupper():
            indices.append(i)
    return indices


print(index_of_caps("HelLo"))

print('task4')
def filter_list(list_with_str_int):
    return [x for x in list_with_str_int if isinstance(x,int)]

print('task5')
def alphabet_soup(word):
    return ''.join(sorted(word))


print(alphabet_soup("hello"))

print('task6')
def probability(numbers_list, number):
    count = sum(1 for num in numbers_list if num >= number)
    return round(100 * count / len(numbers_list), 1)

print('task7')
def chatroom_status(chatroom):
    user_list=len(chatroom)
    if user_list == 0:
        return "no one online"
    elif user_list== 1:
        return f"{chatroom[0]} online"
    elif user_list == 2:
        return f"{chatroom[0]} and {chatroom[1]} online"
    else:
        return f"{chatroom[0]}, {chatroom[1]} and {user_list - 2} more online"

print('task8')
def nth_smallest(list_numbers, ind_num):
    if ind_num < 1 or ind_num > len(list_numbers):
        return None
    else:
        list_numbers.sort()
        return list_numbers[ind_num- 1]

print('task9')
def format_date(date):
    date = date.split('/')
    date.reverse()
    c = '-'.join(date)
    return c
print('task10')


def mineral_formation(stones):
    if stones[0].count(1) > 0 and stones[len(stones) - 1].count(1) > 0:
        return "both"
    elif stones[0].count(1) > 0:
        return "stalactites"
    elif stones[len(stones) - 1].count(1) > 0:
        return "stalagmites"


def mineral_formation(stones):
    if 1 in stones[0] and 1 in stones[-1]:
        return "both"
    elif 1 in stones[0]:
        return "stalactites"
    elif 1 in stones[-1]:
        return "stalagmites"

print('task11')
def pops(pop_list):
    if pop_list == [0]:
        return pop_list
    pivot_index = (len(pop_list)) // 2  # center
    pivot_value = pop_list[pivot_index]
    for i in range(1, pivot_value):
        pop_list[i] = i
        pop_list[pivot_value - i + pivot_value] = i
    return pop_list


print('task12')
def count_overlapping(list_intervals, point):
    count = 0
    for interval in list_intervals:
        if (interval[0] <= point <= interval[1]):
            count += 1
        elif (interval[0] == point or interval[1] == point):
            count += 1
    return count

print('task13')
def tallest_skyscraper(sky_list):
    max_height = 0
    for col in range(len(sky_list[0])):
        count = 0
        for row in range(len(sky_list)):
            if sky_list[row][col] == 1:
                count += 1
        if count > max_height:
            max_height = count
    return max_height

print('task14')
def sum_primes(list_numbers):
    if not list_numbers:
        return None
    primes = []
    for number in list_numbers:
        if number >= 2 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)) and number <= 101:
            primes.append(number)
    return sum(primes)

print('task15')
def show_the_love(share_list):
    smallest = min(share_list)
    total_removed = 0
    for i in range(len(share_list)):
        if share_list[i] != smallest:
            removed = share_list[i] * 1 / 4
            total_removed += removed
            share_list[i] = (share_list[i] - removed)
    share_list[share_list.index(smallest)] += total_removed
    return (share_list)

