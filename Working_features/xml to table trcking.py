import xml.etree.ElementTree as ET
import pandas as pd
import os


def get_desktop_path():
    """
    Obtains the path to the user's desktop.
    """
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Desktop')
    elif os.name == 'posix':  # Linux, macOS
        return os.path.join(os.path.expanduser('~'), 'Desktop')


def parse_xml_to_dataframe(xml_data):
    """
    Parses XML data and returns a pandas DataFrame.

    Args:
        xml_data: XML data as a string.

    Returns:
        pandas.DataFrame: DataFrame containing the parsed XML data.
    """

    root = ET.fromstring(xml_data)
    result = root.find('result')
    events = result.findall('events')

    data = []
    for event in events:
        row = {
            'tracking_number': event.find('tracking_number').text,
            'event_date': event.find('event_date').text,
            'zip': event.find('zip').text if event.find('zip') is not None else '',
            'state': event.find('state').text if event.find('state') is not None else '',
            'city': event.find('city').text if event.find('city') is not None else '',
            'country': event.find('country').text if event.find('country') is not None else '',
            'address': event.find('address').text if event.find('address') is not None else '',
            'description': event.find('description').text,
            'code': event.find('code').text,
            'carrier': event.find('carrier').text
        }
        data.append(row)

    df = pd.DataFrame(data)
    df['event_date'] = pd.to_datetime(df['event_date'])
    df = df.set_index('event_date')
    df = df.sort_index()

    return df


if __name__ == "__main__":
    # Get desktop path
    desktop_path = get_desktop_path()
    file_path = os.path.join(desktop_path, 'log_man.txt')

    # Check if file exists
    if os.path.isfile(file_path):
        # Open and read file
        with open(file_path, 'r') as f:
            xml_data = f.read()
            # Parse XML and convert to DataFrame
            df = parse_xml_to_dataframe(xml_data)
            print(df)
    else:
        print("Файл log_man не знайдено на робочому столі.")