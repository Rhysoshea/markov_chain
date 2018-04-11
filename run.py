"""
Script for running the project and outputting data
"""

from markov_python.cc_markov import MarkovChain
import fetch_data


"""

"""
# fetch_data.get_text()
open_text = open('concatenated.txt')
base_text = open_text.read()
# base_text = fetch_data.set_text()
# base_text = open('concatenated.txt')
# print (base_text)
# base_text.close()

mc = MarkovChain()
mc.add_string(base_text)

mctext = mc.generate_text()

print (mctext)
