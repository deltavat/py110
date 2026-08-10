# Practice Problem 1

lst1 = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst1))
#[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort

print(sorted(lst1, reverse=True))
#[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort


# Practice Problem 2

lst2 = [10, 9, -6, 11, 7, -16, 50, 8]

lst2.sort()
print(lst2)
#[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort

lst2.sort(reverse=True)
print(lst2)
#[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort


# Practice Problem 3

lst3 = [10, 9, -6, 11, 7, -16, 50, 8]

lst3.sort(key=str)
print(lst3)
#[-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort

lst3.sort(key=str, reverse=True)
print(lst3)
#[9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort


# Practice Problem 4

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def year_published(book):
    return int(book['published'])

print(sorted(books, key=year_published))

# Pretty printed for clarity
#[
#   {
#       'title': 'The Book of Kells',
#       'author': 'Multiple Authors',
#       'published': '800'
#   },
#   {
#       'title': 'War and Peace',
#       'author': 'Leo Tolstoy',
#       'published': '1869'
#   },
#   {
#       'title': 'One Hundred Years of Solitude',
#       'author': 'Gabriel Garcia Marquez',
#       'published': '1967'
#   }
#]