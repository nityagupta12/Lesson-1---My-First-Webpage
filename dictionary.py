student_date = {'id1':
    {'name': ['Nitya'],
     'class': ['9'],
     'subject_integration': ['english, math, science']
     },
    'id2':
        {'name': ['Nitya'],
     'class': ['9'],
     'subject_integration': ['english, math, science']
     },
        
    'id3':
        {'name': ['Nitya'],
     'class': ['9'],
     'subject_integration': ['english, math, science']
     },
        
    'id4':
        {'name': ['Nitya'],
     'class': ['9'],
     'subject_integration': ['english, math, science']
     },
}

result = {}
    
for key, value in student_date.items():
    if value not in result.values():
        result[key] = value
          
print(result)