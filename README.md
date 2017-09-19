#NeuroNER

For installation and instruction please see NeuroNER.md

## My work

### Predicting speed
The predicting speed is quite slow due to loading the core nlp for preprocessing each input. This is a problem if you want to deploy this as a service with thounsands of request. 

I have rewrited the predict function so that it pre-load the spacy_nlp in when initializing. The predicting speed now is 0.4s for a document with 700 vietnamese word instead of 4.5s before.

### Ram utilization
The code uses disk for interact with the text, this is not good for thousands of request per hour, the disk either can be full or overloaded. My code make the code interact with text in ram when predicting.

### Further goal
I'm working on batching the dataset so that it don't have to be fully loaded on memory to be trained. This is helpful for training with large dataset.