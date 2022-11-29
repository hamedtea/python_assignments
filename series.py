"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Read a predefined file and initialize a new data structure for genres and TV series
    :param filename: a predefined file of TV series and genres
    :return: dic, key is the name of genre and value is a list of TV series
    """

    # TODO initialize a new data structure
    series_index = {}
    try:
        file = open(filename, mode="r")

        for row in file:
            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            # TODO add the name and genres data to the data structure
            for i in genres:
                if i not in series_index:
                    series_index[i] = [name]
                else:
                    series_index[i].append(name)
        file.close()
        return series_index # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)
    # TODO print the genres
    print("Available genres are: ", end="")
    s = sorted(genre_data)
    print(', '.join(s))
    while True:
        genre = input("> ")
        if genre == "exit":
            return
        try:
            for i in sorted(genre_data[genre]):
                print(i)
        except:
            pass

        # TODO print the series belonging to a genre.


if __name__ == "__main__":
    main()
