import nltk


def text_preprocessing(text):
    # do some pre-processing. I have none to do for now
    return text


def tokenize_sentences(text):
    return nltk.sent_tokenize(text)


def tokenize_words(formatted_text):
    return nltk.word_tokenize(formatted_text)


def word_frequencies(formatted_text):
    stop_words = nltk.corpus.stopwords.words('english')
    word_freq = dict()

    for word in tokenize_words(formatted_text):
        if word not in stop_words:
            if word not in word_freq.keys():
                word_freq[word] = 1
            else:
                word_freq[word] += 1

    return word_freq


def weighted_frequencies(formatted_text):
    word_freq = word_frequencies(formatted_text)
    maximum_frequency = max(word_freq.values())

    weighted_freq = dict()

    for word in word_freq.keys():
        weighted_freq[word] = (word_freq[word]/maximum_frequency)

    return weighted_freq


def sentence_scores(formatted_text):
    weighted_freq = weighted_frequencies(formatted_text)
    tokenized_sentences = tokenize_sentences(formatted_text)

    sentence_scores_table = dict()

    for sentence in tokenized_sentences:
        if sentence not in sentence_scores_table.keys():
            sentence_scores_table[sentence] = 0
        for word in nltk.word_tokenize(sentence):
            if word in weighted_freq.keys():
                if len(sentence.split(' ')) < 30:
                    sentence_scores_table[sentence] += weighted_freq[word]

    return sentence_scores_table


def sample_text():
    text = """
    Amina was born in the middle of the sixteenth century CE to King Nikatau, the 22nd ruler of Zazzau, and Queen Bakwa Turunku (r. 1536–c. 1566).
     She had a younger sister named Zaria for whom the modern city of Zaria (Kaduna State) was renamed by the British in the early twentieth century.
      According to oral legends collected by anthropologist David E. Jones, Amina grew up in her grandfather’s court and was favored by him. 
      He carried her around court and instructed her carefully in political and military matters.
      At age sixteen, Amina was named Magajiya (heir apparent), and was given forty female slaves (kuyanga). 
      From an early age, Amina had a number of suitors attempt to marry her. 
      Attempts to gain her hand included “a daily offer of ten slaves” from Makama and “fifty male slaves and fifty female slaves as well as fifty bags of white and blue cloth” from the Emir of Kano.
      After the death of her parents in or around 1566, Amina’s brother became king of Zazzau. At this point, Amina had distinguished herself as a “leading warrior in her brother's cavalry” and gained notoriety for her military skills.
       She is still celebrated today in traditional Hausa praise songs as “Amina daughter of Nikatau, a woman as capable as a man.”
       After the death of her brother Karama in 1576, Amina ascended to the position of queen. Zazzau was one of the original seven Hausa States (Hausa Bakwai), the others being Daura, Kano, Gobir, Katsina, Rano, and Garun Gabas. 
       Before Amina assumed the throne, Zazzua was one of the largest of these states. It was also the primary source of slaves that would be sold at the slave markets of Kano and Katsina by Arab merchants.
       Only three months after being crowned queen, Amina waged a 34-year campaign against her neighbors, meant to expand Zazzua territory.
       Her army, consisting of 20,000 foot soldiers and 1,000 cavalry troops, was well trained and fearsome.
       In fact, one of her first announcements to her people was a call for them to “resharpen their weapons.” 
       She conquered large tracts of land as far as Kwararafa and Nupe.
       Legends cited by Sidney John Hogben say that she took a new lover in every town she went through, each of whom was said to meet the same unfortunate fate in the morning: “her brief bridegroom was beheaded so that none should live to tell the tale.”
       Under Amina, Zazzua controlled more territory than ever before. To mark and protect her new lands, Amina had her cities surrounded by earthen walls. These walls became commonplace across the nation until the British conquest of Zazzua in 1904, and many of them survive today, known as ganuwar Amina (Amina's walls).
    """
    return text
