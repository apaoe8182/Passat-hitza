import os
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# Prevent Matplotlib's parser from breaking when processing dollar symbols.
mpl.rcParams['text.parse_math'] = False

def generate_df(cnt, grand_total, limit = 30):
    df = pd.DataFrame(columns = ["desc", "value", "total"])

    items = cnt.most_common(limit)
    if not items:
        return

    for i in cnt.most_common(limit):
        df = pd.concat([df, pd.DataFrame([{"desc" : i[0], "value": i[1], "total": grand_total}])], ignore_index=True)

    return df

def generate_barchart(df, title, x, y, x_label = None, y_label = None, palette = None, bar_label = False):

    plot = plt.figure()

    plot = sns.barplot(x = x, y = y, data = df, hue=df[x], legend=False, palette=palette)

    plot.set(title=title)

    if x_label is None:
        plot.xlabel(x)
        plot.ylabel(y)
    else:
        plot.set_xlabel(x_label)
        plot.set_ylabel(y_label)

    if bar_label:
        for index, row in df.iterrows():
            plot.text(row.value, row.desc, row.value,
                    color='white', ha='right')
            
    fig = plot.figure

    return fig

def export(fig, title, output_path = "images"):

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    fig.savefig(str(output_path + "/" + title + ".png"), bbox_inches='tight')