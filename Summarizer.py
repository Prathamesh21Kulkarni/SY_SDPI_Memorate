import re
import heapq
def summary(user_input):
# text = ''' Artificial intelligence (AI), is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[3] Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".[4]'''
    text = user_input
    text = re.sub(r'\[\d+\]', '', text)
    sentences = text.split('.')
    clean_text = text.lower()
    word_tokenize = clean_text.split()
    # english stopwords
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                  "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                  "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                  "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    word2count = {}
    for word in word_tokenize:
        if word not in stop_words:
            if word not in word2count.keys():
                word2count[word] = 1
            else:
                word2count[word] += 1
    sent2score = {}
    for sentence in sentences:
        for word in sentence.split():
            if word in word2count.keys():
                if len(sentence.split(' ')) < 28 and len(sentence.split(' ')) > 9:
                    if sentence not in sent2score.keys():
                        sent2score[sentence] = word2count[word]
                    else:
                        sent2score[sentence] += word2count[word]
    # weighted histogram
    for key in word2count.keys():
        word2count[key] = word2count[key] / max(word2count.values())
    best_sentences = heapq.nlargest(5, sent2score, key=sent2score.get)
    best_sentences = ".".join(best_sentences)
    final_para = str(best_sentences)
    # Cleaning the final text
    final_para = final_para.replace('[', '')
    final_para = final_para.replace(']', '')
    final_para = final_para.replace("'", '')
    final_para = final_para.replace(',', '')
    final_para = final_para.replace('''"''', '')
    # Verse.verse(final_para)
    return final_para

# def get_len(text):
#     length = 0
#     for elem in text.split():
#         new_word = elem
#         length += 1
#     print(length)
