import elixir
from elixir import Entity

class Card(Entity):
    name = Field(UnicodeText)
    cardtype =  Field(UnicodeText)
    cost = Field(UnicodeText)
    text = Field(UnicodeText)
    flavor_text = Field(UnicodeText)
    legalities = Field(UnicodeText)
    rulings = Field(UnicodeText)
    power = Field(UnicodeText)
    toughness = Field(UnicodeText)
    artist = Field(UnicodeText)
    rarity = Field(UnicodeText)
    edition = Field(UnicodeText)
    cardnum = Field(UnicodeText)
    image = Field(UnicodeText)
    otherpart = Field(UnicodeText)
