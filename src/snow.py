# Snow falls unevenly on Cornell's campus.
# Your objective is, given a dictionary of Cornell
# buildings and their respective snowfall in inches,
# return the building that experienced the most snowfall
# Example input: {Uris: 5, Gates: 3.4, Philips: 7.9}
# Example output: Philips

def snow(buildings):
    max_num = 0
    max_building = ""
    for k,v in buildings.items():
      if v > max_num:
        max_building = k
        max_num = v
    return max_building
