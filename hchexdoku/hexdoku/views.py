from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

import json
import numpy as np
from os import getenv
from math import sqrt

SEED=int(getenv('DJANGO_SEED'))


if SEED == 4:
    DICTIONARY = ["1", "2", "3", "4"]
    LIMIT1 = 2
    LIMIT2 = None
    LIMIT3 = None
    HR_WIDTH = 244
elif SEED == 9:
    DICTIONARY = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    LIMIT1 = 3
    LIMIT2 = 6
    LIMIT3 = None
    HR_WIDTH = 548
else:
    DICTIONARY = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    LIMIT1 = 4
    LIMIT2 = 8
    LIMIT3 = 12
    HR_WIDTH = 972

CONSTRAINTS = json.loads(getenv('DJANGO_CONSTRAINS'))
CONSTRAINTS_MATRIX = []

SEED_SPLIT = int(sqrt(SEED))

for i in range(SEED):
    CONSTRAINTS_MATRIX.append([""]*SEED)

for i in range(0, SEED):
    for j in range(0, SEED):
        if str(i*SEED+j) in CONSTRAINTS.keys():
            CONSTRAINTS_MATRIX[i][j] = CONSTRAINTS[str(i*SEED+j)]

def home(request):
    if request.method == 'GET':
        context = {
            'seed_range': range(SEED), 
            'constraints': CONSTRAINTS_MATRIX,
            'dictionary': json.dumps(DICTIONARY),
            'limit1': LIMIT1, 
            'limit2': LIMIT2, 
            'limit3': LIMIT3, 
            'hrwidth': HR_WIDTH
        }
        return render(request, 'hexdoku/home.html', context)
    else:
        return HttpResponseNotAllowed(['GET'])

def check_answer(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        try:
            body_data = json.loads(body_unicode)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'The object is not a valid JSON.'})
        if 'answer' in body_data.keys():
            answer = body_data['answer']
            if not check_size(answer):
                return JsonResponse({'message': 'You did not fill all the hexdoku.'})
            if not check_format(answer):
                return JsonResponse({'message': 'The answer should contain single string characters. Valid characters are ' + str(DICTIONARY)})
            if not check_constraints(answer):
                return JsonResponse({'message': 'Are you attempting to modify the constrains?'})
            if not check_rows(answer):
                return JsonResponse({'message': 'At least one of the rows have repeated values.'})
            if not check_columns(answer):
                return JsonResponse({'message': 'At least one of the columns have repeated values.'})
            if not check_pods(answer):
                return JsonResponse({'message': 'At least one of the pods have repeated values.'})
            return JsonResponse({'message': 'You solved the hexdoku! The flag is ' + getenv('DJANGO_FLAG')})
        else:
            return JsonResponse({'error': 'No answer provided.'})
    else:
        return HttpResponseNotAllowed(['POST'])
    
def check_size(answer):
    if len(answer) != SEED * SEED:
        return False
    return True

def check_format(answer):
    for c in answer:
        if type(c) is not str:
            return False
        if len(c) != 1:
            return False
        if c not in DICTIONARY:
            return False
    return True

def check_rows(answer):
    for i in range(0, SEED * SEED, SEED):
        row = answer[i:i + SEED]
        if len(row) > len(set(row)):
            return False
    return True

def check_columns(answer):
    for i in range(0, SEED):
        col = answer[i::SEED]
        if len(col) > len(set(col)):
            return False
    return True

def check_pods(answer):
    arr=np.array(answer)
    matrix=np.reshape(arr,(SEED,SEED))

    for i in range(0, SEED_SPLIT):
        for j in range(0, SEED_SPLIT):
            pod = matrix[SEED_SPLIT*i:SEED_SPLIT*(1+i),SEED_SPLIT*j:SEED_SPLIT*(1+j)].tolist()
            pod = [x for xs in pod for x in xs]
            if len(pod) > len(set(pod)):
                return False
    return True

def check_constraints(answer):
    for k,v in CONSTRAINTS.items():
        if answer[int(k)] != v:
            return False        
    return True
