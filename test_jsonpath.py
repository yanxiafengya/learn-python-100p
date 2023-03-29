import json
import jsonpath
import certifi
import pygame


data = '''{
  "store": {
    "book":[
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}'''

data = json.loads(data)



# print(data)

print(jsonpath.jsonpath(data,'$..color'))
print(jsonpath.jsonpath(data,'$..price'))

