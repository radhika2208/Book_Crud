MESSAGE_1 = "complete update"
MESSAGE_2 = 'partial data updated'
MESSAGE_3 = 'data deleted'

"""
validation errors
"""
BOOK_VALIDATION_ERROR = {
  'name_of_book': {
        "blank": "name_of_book_BLANK",
        "required": "name_of_book_REQUIRED",
    },
  'book_price': {
        "blank": "book_price_BLANK",
        "invalid": "book_price_INVALID",
        "required": "book_price_REQUIRED",
    },
   'authors_name': {
        "blank": "authors_name_BLANK",
        "required": "authors_name_REQUIRED"
    },
  'author_phone': {
        "blank": "author_phone_BLANK",
        "invalid": "author_phone_INVALID",
        "required": "author_phone_REQUIRED"
    }
}
