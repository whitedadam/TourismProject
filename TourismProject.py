# This program will be a tourism reccomendation application coded in Python. It is built on requirements and guidelines from Codecademy. 

# Defining list variables. One for travel destination. One for a test case traveler.
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = []

# Using a for loop to populate the attractions list.
for destination in destinations:
  attractions.append([])

# Defining a function to retrieve the destination index for locations in the 'destinations' array.
def get_destination_index(destination):
      destination_index = destinations.index(destination)
      return destination_index

# Defining a function to retriveve the traveler location/destination with a parameter of traveler
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
    
test_destination_index = get_traveler_location(test_traveler)

# Defining a function to add attractions to the attractions list.
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    print("Error caught!")
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

# Adding Standard attractions that are associated with the desinations in the destinations list with the newly defined add_attraction function.
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Defining a function 'find_attractions' that will help travelers find the most interesting places within a city for them.
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  
  return attractions_with_interest

# Defining a function 'get_attractions_for_traveler' that will connect travelers with the attractions that match their interest profiles.
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  
  interests_string = "Hi " + traveler[0] + ", we think you'll likse these places around " + traveler_destination + ": " 
  
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += "the " + traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
      
  return interests_string
    
# Print functions for testing current program output.
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
