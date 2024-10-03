import spacy
import json
import os

nlp = spacy.load(os.getenv("SPACY_MODEL_PATH"))

def lambda_handler(event, context):
    def word_similarity(word1, word2):
        token1 = nlp(word1)
        token2 = nlp(word2)
        similarity = token1.similarity(token2)

        result = {
            "word1": word1,
            "word2": word2,
            "similarity": similarity
        }
        return result

    body = json.loads(event['body'])
    word1 = body['word1']
    word2 = body['word2']
    
    result = word_similarity(word1, word2)
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
