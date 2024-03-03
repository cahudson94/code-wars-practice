"""
Johnny is working as an intern for a publishing company, and was tasked with cleaning up old code.
He is working on a program that determines how many digits are in all of the page numbers in a book with pages from 1 to n (inclusive).

For example, a book with 4 pages has 4 digits (one for each page), while a 12 page book has 15 (9 for 1-9, plus 2 each for 10, 11, 12).

Johnny's boss, looking to futureproof, demanded that the new program be able to handle books up to 400,000,000,000,000,000 pages.
"""

def page_digits(pages):
    page_digits = len(str(pages))
    count = sum([9 * int(str(i + 1) + "0" * i) for i in range(page_digits)])
    return count - ((int("9" * page_digits) - pages) * page_digits)
