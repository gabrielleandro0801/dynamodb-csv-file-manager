import csv


def read(file):
    content = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            content.append(row)

        return content


def write(file, headers, content):
    with open(file, mode='w') as new_file:
        writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(headers)
        writer.writerows(content)
