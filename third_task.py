# Third Task
import csv

class WorkWithNotes():
    def __init__(self, csv_file):

        self.csv_file = csv_file

    def read(self):
        with open(self.csv_file, mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)

    def add(self, add_note):

        self.add_note = add_note

        if self.add_note[2] in range(1, 6):
            with open(self.csv_file, mode='a') as file:
                file.write("\n"+",".join(str(x) for x in self.add_note))
        

    def remove(self, row_num):
        with open(self.csv_file, "r+") as f:
            d = f.readlines()
            f.seek(0)
            g = 0
            for i in d:
                if g != row_num:
                    f.write(i)
                g+=1
            f.truncate()

    def print_to_console(self):
        with open(self.csv_file, mode='r') as file:
            csv_data = csv.reader(file)
            data_lines = list(csv_data)

            print(data_lines)

    def get_highest_rating_films(self):
        with open(self.csv_file, mode='r') as file:
            csv_data = csv.reader(file)
            data_lines = list(csv_data)

            rating = []
            films = []

            for line in data_lines[1:]:
                rating.append(line[2])

            max_rating = max(rating)

            for line in data_lines[1:]:
                if line[2] == max_rating:
                    films.append(line[0])

            return films

    def get_lowest_rating_films(self):
        with open(self.csv_file, mode='r') as file:
            csv_data = csv.reader(file)
            data_lines = list(csv_data)

            rating = []
            films = []

            for line in data_lines[1:]:
                rating.append(line[2])

            min_rating = min(rating)

            for line in data_lines[1:]:
                if line[2] == min_rating:
                    films.append(line[0])

            return films

    def get_avg_rating(self):
        with open(self.csv_file, mode='r') as file:
            csv_data = csv.reader(file)
            data_lines = list(csv_data)

            rating = []

            for line in data_lines[1:]:
                rating.append(int(line[2]))
            return sum(rating) / len(rating)


my_film = WorkWithNotes("file.csv")
print(my_film.read())
my_film.add(["Interstellar", "Cool Film", 5])
my_film.remove(2)
my_film.print_to_console()
print(my_film.get_highest_rating_films())
print(my_film.get_lowest_rating_films())
print(my_film.get_avg_rating())