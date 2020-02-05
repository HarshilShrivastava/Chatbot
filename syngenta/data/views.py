from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from .serializers import queryserializer,answerSerializer
from rest_framework.response import Response
from django.db.models import Q
from .utils import levenshtein_ratio_and_distance

from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
from .models import Data
from rest_framework.permissions import AllowAny
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import nltk
from nltk.stem.porter import *

@permission_classes((AllowAny,))
@api_view(['POST',])
def process(request):
    data={}
    if request.method=="POST":
        serializer=queryserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            query=serializer.validated_data['query']
            a=remove_stop_word(query)
            data['result']=filter1(a)
            # b=remove_stemming(a)
            data['sucess']=True
            data['message']="sucessfull"
            data['query']=query
            # data['stop']=b

        else:
            data=serializer.errors
    return Response(data)

def remove_stop_word(a):
    nlp=spacy.load("en")
    doc = nlp(a)
    filtered_sentence =[]
    token_list = []
    for token in doc:
        token_list.append(token.text)
    for token in token_list:
        lexeme = nlp.vocab[token]
        if lexeme.is_stop == False:
            filtered_sentence.append(token) 
    query=''
    a=query.join(filtered_sentence)
    return a
def filter1(words):
    query=''
    result={}
    a=query.join(words)
    print(a)
    qs=Data.objects.all()
    for instance in qs:
        result[instance.id]=[fuzz.token_sort_ratio(a,remove_stop_word(instance.ThreatName+' '+instance.WhatItIs) ) ]
    Keymax = max(result, key=result.get)
    print(result)
    print(type(Keymax))
    print(Keymax)
    return get_object(int(Keymax))

def get_object(id):
    obj=get_object_or_404(Data,id=id)
    serializer=answerSerializer(obj)
    return (serializer.data)
    