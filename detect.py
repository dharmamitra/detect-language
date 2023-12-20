import sentencepiece as spm

eng_model_path = "models/eng.model"
skt_model_path = "models/skt.model"

eng_model = spm.SentencePieceProcessor()
eng_model.load(eng_model_path)

skt_model = spm.SentencePieceProcessor()
skt_model.load(skt_model_path)

def detect_language(sentence):
    encoded_sentence_eng = eng_model.encode_as_pieces(sentence)
    encoded_sentence_skt = skt_model.encode_as_pieces(sentence)
    length_eng = len(encoded_sentence_eng)
    length_skt = len(encoded_sentence_skt)
    print("Length of English encoder: ", length_eng)
    print("Length of Sanskrit encoder: ", length_skt)
    if length_eng < length_skt:
        return "en"
    else:
        return "sa"
    
sentence = "yena yena vikalpena yadyad vastu vikalpyate"
detect_language(sentence)
sentence = "I am going to the forest to see the Buddha. yad na vikalpyate"
detect_language(sentence)

