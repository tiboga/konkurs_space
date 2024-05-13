import csv
import os
into_path = input()
paths = []
for root, dirs, files in os.walk(into_path):
    for file in files:
        if file != 'result.csv':
            if file.endswith('.csv'):
                paths.append(os.path.join(root, file))
all_sp = []
for elem in paths:
    with open(elem) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='#')
        for row in reader:
            all_sp.append({"id": row['id'], 'name': row['name'], 'surname': row['surname'], 'age': int(row['age']),
                           'height': int(row['height']), 'weight': int(row['weight']),
                           'eyesight': float(row['eyesight']),
                           'education': row['education'], 'english_language': row['english_language']})

out_sp = list(filter(lambda x: (20 <= x['age'] <= 59 and 150 <= x['height'] <= 190 and 50 <= x['weight'] <= 90 and x[
    'eyesight'] == 1.0 and (x['education'] == 'Master' or x['education'] == 'PhD') and x[
                                    'english_language'].lower() == 'true'), all_sp))
into_age_range = sorted(list(filter(lambda x: 27 <= x['age'] <= 37, out_sp)), key=lambda x: (x['name'], x['surname']))
outro_age_range = sorted(list(filter(lambda x: 27 > x['age'] or x['age'] > 37, out_sp)),
                         key=lambda x: (x['name'], x['surname']))
good_out_sp = into_age_range + outro_age_range
with open(f'{into_path}/result.csv', 'w', newline='') as f:
    fieldnames = ['id', 'name', 'surname', 'height', 'weight', 'education']
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='#')
    i = 1
    for elem in good_out_sp:
        writed_row = {'id': i, 'name': elem['name'], 'surname': elem['surname'], 'height': elem['height'],
                      'weight': elem['weight'], 'education': elem['education'].rstrip('\n')}
        writer.writerow(writed_row)
        i += 1
