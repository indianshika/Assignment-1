d = {'Student': ['Rahul', 'Kishore', 'Vidhya','Raakhi'],'Marks': [57,87,67,79]}
students = d['Student']
marks = d['Marks']
maxm = max(marks)
i = marks.index(maxm)
print("person obtained highest marks is- ", students[i])
