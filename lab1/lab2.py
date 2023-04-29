# =====================================1=================================

def remove_duplicate(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicate([1,2,3,3]))

# =====================================2=================================
# ///////////////////////a //////////////////////////


string = input("Enter a string: ")
length = len(string)
middle_index = length // 2

front_half = string[:middle_index]
back_half = string[middle_index:]
print("Front half:", front_half)
print("Back half:", back_half)


# /////////////////////////////////b///////////////////////////////////////////

a = input("Enter string a: ")
b = input("Enter string b: ")

a_length = len(a)
b_length = len(b)

a_middle_index = (a_length + 1) // 2
b_middle_index = (b_length + 1) // 2

a_front_half = a[:a_middle_index]
a_back_half = a[a_middle_index:]

b_front_half = b[:b_middle_index]
b_back_half = b[b_middle_index:]

result = (a_front_half + b_front_half) + (a_back_half + b_back_half)

print("Result:", result)
# =====================================3=================================
def are_different(numbers):
    return len(set(numbers)) == len(numbers)

nums1 = [1,5,7,9]
nums2 = [2,4,5,5,7,9]
print(nums1, "are different: ", are_different(nums1))
print(nums2, "are different: ", are_different(nums2))
# =====================================4=================================
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [20, 10, 25, 9, 1, 3]
bubble_sort(arr)
print("Sorted array:", arr)

# =====================================5=================================
def play_game():
    random_number = random.randint(1, 100)
    num_tries = 10
    guessed_numbers = set()

    while num_tries > 0:
        user_input = input("Guess a number between 1 and 100: ")

        if not user_input.isdigit() or int(user_input) <= 0 or int(user_input) > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        if int(user_input) in guessed_numbers:
            print("You already guessed this number. Please try another number.")
            continue

        guessed_numbers.add(int(user_input))
        num_tries -= 1

        if int(user_input) == random_number:
            print("Congratulations! You guessed the correct number in", 10 - num_tries, "tries.")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                play_game()
            else:
                print("Thanks for playing!")
            return

        elif int(user_input) < random_number:
            print("The secret number is larger than", user_input)
        else:
            print("The secret number is smaller than", user_input)

    play_again = input("You ran out of tries.\nDo you want to play again? (y/n): ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")


play_game()