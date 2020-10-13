from summarizer import Summarizer
model = Summarizer()

import pickle
pickle_out=open('bert.pkl','wb')
pickle.dump(model,pickle_out)
pickle_out.close()
