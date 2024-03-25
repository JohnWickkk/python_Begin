# You have a list ['Hillel', 'AQA', 'TEST'], convert that list to a string and then back to a list

m_list = ['Hillel', 'AQA', 'TEST']
new_m_string = ',' .join(m_list)
print(new_m_string)
new_m_list = new_m_string.split()
print(new_m_list)
