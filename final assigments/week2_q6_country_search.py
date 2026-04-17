'''
Function to search for a country in a list
Returns the index if found, otherwise returns "Not Found in List"
'''

# Function to search country
def search_country(countries, target):
    for index, country in enumerate(countries):
        if country.lower() == target.lower():
            return index
    return "Not Found in List"

# Main program
print("="*50)
print("COUNTRY SEARCH")
print("="*50)

# Sample countries list
countries = ["USA", "India", "Canada", "Australia", "Japan", "Germany", "France"]

print("\nAvailable countries:")
for i, country in enumerate(countries):
    print(f"  {i+1}. {country}")

# Get search input
search_query = input("\nEnter country name to search: ")

# Search
result = search_country(countries, search_query)

# Display result
print("\n" + "-"*50)
if isinstance(result, int):
    print(f"✓ '{search_query}' found at index {result}")
    print(f"  Position: {result + 1}")
else:
    print(f"✗ {result}")
print("-"*50)
