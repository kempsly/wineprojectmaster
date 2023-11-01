from django.core.cache import cache
import pickle
import pandas

model_cache_key = 'model_cache'

model = cache.get(model_cache_key)

if model is None:
    # Set it to the cache
    model = pickle.load(open('classificator/svc_clf_wquality2.pkl', 'rb'))
    cache.set(model_cache_key, model, None)