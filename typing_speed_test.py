# Typing Speed Test - 1 Minute Timed with Live WPM Chart
# Uses a mix of easy, medium, and complex words
# Measures WPM and accuracy for 1 minute
# Updates live plot after each input for a visual graph

import random
import time
import matplotlib.pyplot as plt


# Word lists

easy_words = ["cat", "dog", "sun", "tree", "book", "milk", "fish", "red", "blue", "car"]
medium_words = ["apple", "orange", "window", "garden", "bottle", "keyboard", "python", "holiday", "student", "random"]
complex_words = ["encyclopedia", "philosophy", "algorithm", "xylophone", "metamorphosis", "juxtaposition", "quizzical", "pneumonia", "substantial", "baccalaureate"]

all_words = easy_words + medium_words + complex_words


# Generate random text

def generate_text(word_count=10):
    return ' '.join(random.choice(all_words) for _ in range(word_count))


# Timed Typing Test with Live Plot

def typing_test_live():
    print("=== 1 Minute Typing Test with Live WPM Chart ===\n")
    print("Type as many words as you can in 1 minute.\n")
    input("Press Enter to start...")

    start_time = time.time()
    elapsed = 0
    typed_words = []
    target_words = []

    wpm_history = []
    times = []

    while elapsed < 60:
        # Generate random words to type
        words_to_type = generate_text(10)
        target_words.extend(words_to_type.split())
        print(f"\n{words_to_type}\n")

        typed = input("Type here: ")
        typed_words.extend(typed.split())

        # Record WPM after each input
        elapsed = time.time() - start_time
        wpm = len(typed_words) / (elapsed / 60)
        wpm_history.append(wpm)
        times.append(int(elapsed))

        remaining = max(0, 60 - int(elapsed))
        print(f"Time remaining: {remaining} seconds")

    
    # Final WPM and Accuracy
    
    total_typed = len(typed_words)
    correct = sum(1 for a, b in zip(typed_words, target_words) if a == b)
    final_wpm = total_typed  # 1-minute test, total words = WPM
    accuracy = (correct / total_typed * 100) if total_typed > 0 else 0

    print("\n=== Results ===")
    print(f"Total words typed: {total_typed}")
    print(f"Correct words: {correct}")
    print(f"Final WPM: {final_wpm}")
    print(f"Accuracy: {accuracy:.2f}%")

    
    # Plot WPM over time
    
    if wpm_history:
        plt.figure(figsize=(10,4))
        plt.plot(times, wpm_history, marker='o', color='blue')
        plt.xlabel("Time (seconds)")
        plt.ylabel("WPM")
        plt.title("Typing Speed Progress Over 1 Minute")
        plt.xticks(range(0, 61, 10))
        plt.ylim(0, max(wpm_history) + 5)
        plt.grid(True)
        plt.show()

    return final_wpm, accuracy


# Main Program

if __name__ == "__main__":
    typing_test_live()
