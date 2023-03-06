import sys
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

class GraphGenerator:
    def __init__(self, dataset_name) -> None:
        self.__data_dir = os.getenv("DRT_PROCESSING_OBJECT_ARTIFACTS_PATH")
        if self.__data_dir == None:
            self.__data_dir = os.path.dirname(os.path.realpath(__file__))
        self.dataset_name = dataset_name

    
    def create_graph(self):
        batch_num = []
        lookups = []
        inserts = []
        operations = []

        try:
            # Read the existing data
            with open('{}.csv'.format(self.dataset_name), 'r',) as file:
                reader = csv.reader(file, delimiter = ',')
                next(reader, None)
                for row in reader:
                    batch_num.append(row[0])
                    lookups.append(float(row[1]))
                    inserts.append(float(row[2]))
                    operations.append(float(row[3]))
        except IOError:
            print("Error trying to read file" + str(IOError.__class__))

        fig, ax = plt.subplots()

        ax.set_title("Throughput for {} dataset".format(self.dataset_name), fontsize="small")
        plt.xlabel("Batches", fontsize="small")
        plt.ylabel("Throughput/Second", fontsize="small")

        ax.plot(batch_num, lookups, linestyle="-",  linewidth='0.25', color="blue",)
        ax.plot(batch_num, inserts, linestyle="-", linewidth='0.25', color="green",)
        ax.plot(batch_num, operations, linestyle="-", linewidth='0.25', color="red",)

        batch_bar = np.arange(len(batch_num))

        ax.bar(batch_bar-0.1, lookups, 0.1, color="b",label="Lookups",)
        ax.bar(batch_bar, inserts, 0.1, color="g",label="Inserts",)
        ax.bar(batch_bar+0.1, operations, 0.1, color="r",label="Operations",)
        ax.legend(ncol=3, loc="upper right", fontsize="small")

        hist_file = os.path.join(self.__data_dir + "/hist_{}.png".format(self.dataset_name))
        fig.savefig(hist_file, dpi=250)

if __name__ == "__main__":
    if sys.argv[1]:
        graph_generator = GraphGenerator(sys.argv[1])
        graph_generator.create_graph()
    else:
        print("No filename given")
