#given input 'north', 'west', or 'central', return 'RPCC', 'Keeton', and 'anywhere but Okenshields' respectively
def where_to_eat(location):
    if location == 'north':
        return 'RPCC'
    elif location == 'west':
        return 'Keeton'
    elif location == 'central':
        return  'anywhere but Okenshields'
