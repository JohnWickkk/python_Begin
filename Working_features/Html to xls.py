import json
import pandas as pd

def convert_to_table(html_text):
  # Assuming the HTML-like text is already in a string format
  data = json.loads(html_text)

  # Extract main data into a DataFrame
  main_data = []
  for result in data['results']:
    main_data.append({
      'weight_g': result['weight_g'],
      'tracking_number': result['tracking_number'],
      'ship_to_country': result['ship_to_country'],
      'carrier': result['carrier']
    })
  main_df = pd.DataFrame(main_data)

  # Extract events data into a DataFrame
  events_data = []
  for result in data['results']:
    for event in result['events']:
      event.update({'tracking_number': result['tracking_number']})
      events_data.append(event)
  events_df = pd.DataFrame(events_data)

  return main_df, events_df

# Example usage
html_text = """
"""

main_table, events_table = convert_to_table(html_text)
print(main_table)
print(events_table)
