student_data = {'id1':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id2':
{'name': ['Aizaz'],
'class': ['IX'],
'subject_integration': ['english, math, science']
},
'id3':
{'name': ['Sana'],
'class': ['X'],
'subject_integration': ['english, math, science']
},
'id4':
{'name': ['Sofia'],
'class': ['VI'],
'subject_integration': ['english, math, science']
},
}


result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)