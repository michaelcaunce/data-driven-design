import apache_log_parser
from csv import DictReader
from pandas import DataFrame
import seaborn

from collections import Counter
pages = []
with open('cleaned_log.csv') as in_f:
    reader = DictReader(in_f)
    for line in reader:
        pages.append(line['request_url_path'])

counts = Counter(pages)
print(counts)

selected_pages = [page for page, _ in counts.most_common(30)]
print(selected_pages)

graph_pages = [page for page in pages if page in selected_pages]
data = DataFrame({'pages': graph_pages})
print(data)

plot = seaborn.countplot(data=data, y='pages', order=selected_pages)
plot.figure.set_size_inches(30,20)
plot.get_figure().savefig('page_analysis_plot.png')
