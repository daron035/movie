from modeltranslation.translator import register, translator, TranslationOptions
from .models import *

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title',)

# translator.register(Movie, MovieTranslationOptions)