from textblob import TextBlob
i=TextBlob('heloi ym naem is abullha')
print(i.correct())
print(i.translate(from_lang=u'auto',to=u'es'))