from temporal_network import TemporalNetwork
import tacoma
from tacoma.interactive import visualize

# Comment this part if you already generated .taco file #
tn = TemporalNetwork("mail.xlsx")                       #
tn.parser_to_taco()                                     #
#########################################################

tn = tacoma.load_json_taco("temporal_graph.taco")
print("Number of mistakes:", tacoma.verify(tn))
#TODO: Check for duplicates edges