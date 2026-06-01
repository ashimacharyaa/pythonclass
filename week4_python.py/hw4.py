def word_text(text):

    punctuation = [".", "!", "?", "'", "\n"]
    cleaned_text = text

    frequency_dict = {}   # here i store words

    # remove punctuation if occurs [".", "!", "?", "'", "\n"]
    for char in punctuation:
        cleaned_text = cleaned_text.replace(char, "")

    # convert to lowercase as well as split into words
    words = cleaned_text.lower().split()

    # count frequency
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    # sort by frequency (descending)
    sorted_words = sorted(
        frequency_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_words[:3]


# === test execution ===
text = ''' Nepal is Beautiful Country. Nepal Has Mount Everest and Gautam Buddha 
Birthplace and Ashim too was borned in Nepal and is pride of nepal. Many tourist visit 
nepal for its beautiful place like pokhara, chitwan, Ghale Gaun etc'''

top_3 = word_text(text)

output_string = "Top 3 words: " + str(top_3)

print(output_string)