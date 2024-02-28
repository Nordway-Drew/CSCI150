def main():
    TOLKIEN = 1
    DICKENS = 2
    DOSTOEVSKY = 3

    selectAgain = 'y'

    while selectAgain == 'y':

        menu()

        author = int(input())

        if author == TOLKIEN:
            tolkien()
        elif author == DICKENS:
            dickens()
        elif author == DOSTOEVSKY:
            dostoevsky()
        else:
            print("\nSorry, there are no quotes for that author.")

        selectAgain = input("\nSelect y to read another quote or q to quit.")

    print("\nCome back again!")


def menu():
    print("\nSelect an author and reveal a quote:\n")
    print("1.Tolkien")
    print("2.Dickens")
    print("3.Dostoevsky")


def tolkien():
    print("\nNot all those who wander are lost.")
    print("\t\t\t\t\t J.R.R Tolkien")


def dickens():
    print("\nIt was the best of times,")
    print("it was the worst of times,")
    print("it was the age of wisdom,")
    print("it was the age of foolishness...")
    print("\t\t\t\t\t Charles Dickens")


def dostoevsky():
    print("\nThe mystery of human existence lies")
    print("not in just staying alive, but in")
    print("finding something to live for.")
    print("\t\t\t\t\t Dostoevsky")

main()