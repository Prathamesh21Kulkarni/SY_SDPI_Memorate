def Verse2(input_text):
    # -------------Defining Functions --------------#
    def distance(index_list, center, after_center):
      diff_list = []
     # diff_list0 = []
      if after_center == True:
         for each_key in index_list:
              diff = abs(center - int(each_key))
              diff_list.append(diff)
      else:
         for each_key in index_list:
             diff = center - int(each_key)
             diff_list.append(diff)
         for each_diff in diff_list:
             if each_diff < 0:
                 index_each_diff = diff_list.index(each_diff)
                 each_diff = max(diff_list)
                 diff_list[index_each_diff] = each_diff
      index = diff_list.index(min(diff_list))
      return index


    def nearest_letter(consonants, word, index, return_index):
     conso_list = []
     for each_consonant in consonants:
         if each_consonant in word:
             conso_index = word.rfind(each_consonant)
             conso_list.append(conso_index)
     nearest_conso_index = distance(conso_list, index, False)
     nearest_conso = word[int(conso_list[nearest_conso_index])]
     if return_index == True:
         return int(conso_list[nearest_conso_index])
     else:
         return nearest_conso


    import re

    input = input_text
# input = input.replace(',','.')
# input = input.replace(';','.')
# input = input.replace(':','.')
    input = re.sub(r'\[\d+\]', '', input)
    text = input.split()
    lines_0 = []
    rhyme_list = []
    lines = []
# for i in range(len(text)):
#     lines.append(text[i].split(','))
# print(lines[0])
    start = 0
    for i in range(len(text)):
        if text[i].find('.') != -1:
            if i - start >= 8:
                line = text[start:i + 1]
                lines_0.append(line)
                start = i + 1
    for each_line in lines_0:
        new_line = str(each_line)
        new_line = new_line.replace('[', '')
        new_line = new_line.replace(']', '')
        new_line = new_line.replace("'", '')
        new_line = new_line.replace(',', '')
        new_line = new_line.replace('.', '')
        lines.append(new_line)

# updated_lines_list = []
# updated_line_index_start = 0
# lines_for_rhyme = []
    lines_for_rhyme_dict = {}
    final_rhyme_sentences = []
    for i in range(len(lines)):

        words = lines[i].split()

        tot_len = len(words)

        words_to_work = {}
        for j in range(len(words)):
            if len(words[j]) > 4:
                if any(char.isdigit() for char in words[j]) == False:
                    words_to_work[j] = words[j]
        keys = list(words_to_work.keys())
        first_index = 0
        second_list = []
        first_list = []
        lines_for_rhyme = []
        for k in range(tot_len // 4):
            second_index = distance(keys, first_index + 4, True)
            second_index_line = keys[second_index]
            second_list.append(second_index_line)
            rhyme_line = words[first_index:second_index_line + 1]
            first_index = second_index_line + 1
            first_list.append(first_index)
            lines_for_rhyme.append(rhyme_line)
        lines_for_rhyme_dict[i] = lines_for_rhyme
    final_text_list = []
    for l in range(len(lines_for_rhyme_dict)):
        rhyme_sentences = []
        rhyme_sentences = lines_for_rhyme_dict[l]
    # print(len(rhyme_sentences))
    # print(words)
        for i in range(len(rhyme_sentences)):
        # print(len(rhyme_sentences[i]))
            if len(rhyme_sentences[i]) == 0:
                rhyme_sentences.pop(i)

            elif len(rhyme_sentences[i]) <= 2:
            # print("hi")
            # prev_sentence = []
                that_sentence = str(rhyme_sentences[i])
                that_sentence = that_sentence.replace('[', '')
                that_sentence = that_sentence.replace(']', '')
                that_sentence = that_sentence.replace(',', '')
                that_sentence = that_sentence.replace("'", '')
                prev_sentence = rhyme_sentences[i - 1]
                prev_sentence.append(that_sentence)
                rhyme_sentences.insert(i, prev_sentence)
            # rhyme_sentences.pop(i+1)
                rhyme_sentences.pop(i - 1)
            # rhyme_sentences.pop(i+1)

        prev_sentence = []
        if len(rhyme_sentences[-1]) <= 2:
            rhyme_sentences.pop(-1)
        final_rhyme_sentences.append(rhyme_sentences)
        words_for_rhyme = []
        for elem in rhyme_sentences:
            words_for_rhyme.append(elem[-1])
        # conso_list = []
        vowels = ('a', 'e', 'i', 'o', 'u')
        consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
        suffix_list = []
        finished_rhyme_words = []
    # ------------------------------------------------------------------------
    # Finding the suffix for the largest word
    # ------------------------------------------------------------------------
        max_rhyme_word = max(words_for_rhyme, key=len)

        nearest_vowel_max_rhyme = nearest_letter(vowels, max_rhyme_word, len(max_rhyme_word) - 1,
                                             False)  # Getting the last vowel
        nearest_vowel_max_rhyme_index = nearest_letter(vowels, max_rhyme_word, len(max_rhyme_word) - 1,
                                                   True)  # Getting last vowel's index
        nearest_consonent_to_nearest_vowel_max_rhyme = nearest_letter(consonants, max_rhyme_word,
                                                                  nearest_vowel_max_rhyme_index,
                                                                  False)  # Getting the consonant nearest to the last vowel
        nearest_consonent_to_nearest_vowel_max_rhyme_index = nearest_letter(consonants, max_rhyme_word,
                                                                        nearest_vowel_max_rhyme_index,
                                                                        True)  # Getting the index of consonant nearest to the last vowel
        suffix_max_rhyme = max_rhyme_word[
                       nearest_consonent_to_nearest_vowel_max_rhyme_index:]  # no_of_lines = len(words_for_rhyme)//2
        suffix_list.append(suffix_max_rhyme)
        max_rhyme_index = words_for_rhyme.index(max(words_for_rhyme, key=len))
        words_for_rhyme.pop(max_rhyme_index)
        finished_rhyme_words.insert(max_rhyme_index, max_rhyme_word)
        for i in range(len(
                words_for_rhyme)):  # Finding last vowel and it's previous consonent for the other words(i.e all words_for_rhyme except the biggest word)
            rhyme_word = words_for_rhyme[i]
            rhyme_word_index = i
            nearest_vowel_rhyme_word = nearest_letter(vowels, rhyme_word, len(rhyme_word) - 1,
                                                  False)  # Getting the last vowel
            nearest_vowel_rhyme_word_index = nearest_letter(vowels, rhyme_word, len(rhyme_word) - 1,
                                                        True)  # Getting last vowel's index
            nearest_consonent_to_nearest_vowel_rhyme_word = nearest_letter(consonants, rhyme_word,
                                                                       nearest_vowel_rhyme_word_index,
                                                                       False)  # Getting the consonant nearest to the last vowel
            nearest_consonent_to_nearest_vowel_rhyme_word_index = nearest_letter(consonants, rhyme_word,
                                                                             nearest_vowel_rhyme_word_index,
                                                                             True)  # Getting the index of consonant nearest to the last vowel
            suffix = '-' + suffix_max_rhyme
            if nearest_vowel_rhyme_word_index == len(rhyme_word) - 1:
                rhyme_word = rhyme_word
            else:
                rhyme_word = rhyme_word[:nearest_vowel_rhyme_word_index - len(rhyme_word) + 1]
            rhyme_word = rhyme_word + suffix
            finished_rhyme_words.insert(i, rhyme_word)
        for i in range(len(rhyme_sentences)):
            rhyme_sentences[i].insert(-1, finished_rhyme_words[i])
            rhyme_sentences[i].pop(-1)
        for i in range(len(rhyme_sentences)):
            if i == len(rhyme_sentences) - 1:
                each_verse = str(rhyme_sentences[i]) + '||' + str(l + 1) + '||'
                final_text_list.append(each_verse)
            else:
                each_verse = str(rhyme_sentences[i]) + '|'
                final_text_list.append(each_verse)
    return final_text_list