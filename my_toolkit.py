def calculate_average(numbers):
    """"Calculate the average of a list of numbers. Return 0 if empty."""
    if not numbers:
        return 0

    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)
    return average

def find_max_and_min(numbers):
    """Find the maximum and minimum values using a loop."""
    if not numbers:
        return None, None

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number

    return max_value, min_value


def count_occurrences(items, target):
    """Count how many times the target appears in a list."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """Check if text reads the same forward and backward, ignoring spaces and case."""
    cleaned_text = ""

    for character in text:
        if character != " ":
            cleaned_text += character.lower()

    left = 0
    right = len(cleaned_text) - 1

    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False

        left += 1
        right -= 1

    return True

def create_report (title, scores):
    """Create and return a formatted report using other functions."""
    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)

    report = (
        f"{title}\n"
        f"Scores: {scores}\n"
        f"Average: {average:.2f}\n"
        f"Maximum: {max_value}\n"
        f"Minimum: {min_value}\n"
    )
    return report

if __name__ == "__main__":

 test_scores = [85, 92, 78, 95, 88, 70, 93]

 print(f" Average: {calculate_average(test_scores):.2f}")
 print(f"Max/Min: {find_max_and_min(test_scores)}")
 print(f"Count of 85: {count_occurrences(test_scores, 85)}")
 print(f"'racecar' palindrome: {is_palindrome('racecar')}")
 print(f"'hello' palindrome: {is_palindrome('hello')}") 

 print()

 print(create_report("Class Scores",  test_scores))

 print("Edge Case Tests:")

 print(f"Empty average: {calculate_average([])}")
 print(f"Empty Max/Min: {find_max_and_min([])}")

 print(f"Count of 85: {count_occurrences([85, 85, 90, 85], 85)}")

 print(f"Phrase palindrome: {is_palindrome('nurses run')}")
 print(f"Single character palindrome: {is_palindrome('a')}")
 print(f"Mixed case palindrome: {is_palindrome('Racecar')}")