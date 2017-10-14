# Max Wagner - HW9
import pandas as pd
import re

# clean it first, requires the epa file, and another file named 'epa-http-clean.txt'
with open('epa-http.txt', 'r') as dirty:
    with open('epa-http-clean.txt', 'w') as clean:
        for line in dirty:
            newline = re.sub('="', '=', line) # get rid of inner quotes
            newline = re.sub('-$', '0', newline) # get rid of dashes in filesizes
            newline = re.sub(r'\[\d{2}:(\d{2}):\d{2}:\d{2}]', r'\1', newline) # take in hour only
            clean.write(newline)
    clean.close()
dirty.close()

# pull out a gif name from a longer name
def giffy(text):
    text = re.sub(' HTTP/1.0', '', text)
    text = re.sub('GET ', '', text)
    return text

# read it in
df = pd.read_csv('epa-http-clean.txt', sep = '\s+', escapechar = "=", header = None, names = ['host','time','request','code','bytes'])

print "Which hostname or IP address made the most requests?"
print df['host'].value_counts().idxmax() + " with " + str(df['host'].value_counts()[0]) + " requests.\n"

print "Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive?"
print df.groupby('host', as_index = False)['bytes'].sum().max()

print "\nDuring what hour was the server the busiest in terms of requests?"
print str(df['time'].value_counts().idxmax()) + " to " + str(df['time'].value_counts().idxmax() + 1)

print "\nWhich .gif image was downloaded the most during the day?"
df_gif = df[df['request'].str.contains(".gif")]['request'].apply(giffy)
print df_gif.value_counts().idxmax() + " a total of " + str(df_gif.value_counts()[0]) + " times.\n"

print "What HTTP reply codes were sent other than 200?"
print df['code'][df['code'] != 200].unique()