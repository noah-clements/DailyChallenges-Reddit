import timeit
import copy


def lettersum(text:str):  
    return sum(ord(c) - 96 for c in text.lower())


def sum_from_input():
    line = input("Enter a string to sum (only alphabetic characters count): ")
    summed_alphas = lettersum(line)
    print(f"the sum of the alphabetic characters is {summed_alphas}")


def get_word_set(): 
    with open("enable1.txt") as f:
        return set(f.read().splitlines())
        # return f.readlines()


def find_words_w_sum(words:iter, num:int): 
    # words = get_word_set()
    for word in words:
        # print(f"checking {word}, sum= {lettersum(word)}")
        if lettersum(word) == num:
            print(word)


def count_odd_sums(words:iter):
    return sum(1 for word in words if lettersum(word) % 2)
   

# sum_from_input()
start_time = timeit.default_timer()
words = get_word_set()
print(len(words))
print(f'get_word_set() took {timeit.default_timer() - start_time}')

# Bonus 1
# print("Bonus 1")
# start_time = timeit.default_timer()
# find_words_w_sum(words, 319)
# print(timeit.default_timer() - start_time)

# Bonus 2
# print('Bonus 2')
# start_time = timeit.default_timer()
# print(count_odd_sums(words))
# print(timeit.default_timer() - start_time)


word_sum_dict = {word:lettersum(word) for word in words}
words_by_sum = {}
for word in words:
    words_by_sum.setdefault(word_sum_dict[word], []).append(word)

# Bonus 3
# print("Bonus 3")
# start_time = timeit.default_timer()
# s = max(words_by_sum, key=lambda d: len(words_by_sum[d]))
# print(f'The most common sum is {s} with {len(words_by_sum[s])} words')
# print(timeit.default_timer() - start_time)

# Bonus 4
# print("Bonus 4")
# start_time = timeit.default_timer()
# words_by_len_sum = {(len(word), word_sum_dict[word]): word for word in words}
# for l, s in words_by_len_sum:
#     same_sum = words_by_len_sum.get((l + 11, s), '')
#     if same_sum:
#         print(f'{words_by_len_sum[(l, s)]} and {same_sum} have the same lettersum')
# print(timeit.default_timer() - start_time)

# Bonus 5
print("Bonus 5")


def find_unique_char_words(word_list:list[str]):
    identified_words = set()
    for w1 in word_list: 
        for w2 in word_list:
            if set(w1).isdisjoint(set(w2)):
            # if set(w1) & set(w2) == set():
                print(f"{w1} and {w2} share no letters")
                identified_words.add(frozenset({w1, w2}))
        # print(f"checked {w1} against all others with lettersum {s}")                    # print(f'Removing {w1}')
        # word_list.remove(w1)
    # print(identified_words)
    return identified_words

def write_words_to_file(lettersum):
    with open(f"words_{lettersum}.txt", "w") as f:
        f.writelines("\n".join(words_by_sum[lettersum]))

def get_word_list(lettersum):
    return copy.deepcopy(words_by_sum[lettersum])

def find_unique_char_words_by_sum(lettersum):
    # just checking if still there
    # if lettersum == 188:
    #     print(f'cytotoxicity there? {"cytotoxicity" in words_by_sum[lettersum]}')
    #     print(f'unreservedness there? {"unreservedness" in words_by_sum[lettersum]}')
    #     write_words_to_file(lettersum=lettersum) 
    # elif lettersum == 194:
    #     print(f'defenselessnesses there? {"defenselessnesses" in words_by_sum[lettersum]}')
    #     print(f'photomicrographic there? {"photomicrographic" in words_by_sum[lettersum]}')
    #     print(f'microphotographic there? {"microphotographic" in words_by_sum[lettersum]}')
    #     write_words_to_file(lettersum=lettersum) 

    word_list = get_word_list(lettersum)
    identified_words = find_unique_char_words(word_list) 
    if len(identified_words) > 0:
        print(f'returning from find_unique_char_words_by_sum({lettersum})')
        print(identified_words)
    return identified_words   
    

def words_samesum_noletters(start_sum):
    identified_words = []
    # print(f'defenselessnesses there? {"defenselessnesses" in words_by_sum[194]}')
    # print(f'photomicrographic there? {"photomicrographic" in words_by_sum[194]}')
    # print(f'microphotographic there? {"microphotographic" in words_by_sum[194]}')

    # for s, word_list in words_by_sum.items():
    for s in words_by_sum:
        if s >= start_sum:
            unique_char_words = find_unique_char_words_by_sum(s)
            if len(unique_char_words) > 0:
                print(f'For lettersum: {s}, {unique_char_words} share no letters.')
                identified_words += list(unique_char_words)
    return identified_words


# print(words_samesum_noletters(188))
# print(timeit.timeit(words_samesum_noletters))
