import spacy
from neuroner import NeuroNER
import load_parameters

model_folder = '../trained_models/conll_2003_en'
init_dataset_folder = '../data/example_unannotated_texts'

arguments = load_parameters.parse_arguments(pretrained_model_folder = model_folder, init_dataset = init_dataset_folder)

nn = NeuroNER(**arguments)
spacy_nlp = spacy.load('en')

#this function can be repeated several times to depoy as a service without loading the model and core_nlp again 
def predict(text):
    return nn.new_predict(text, spacy_nlp)