#!/usr/bin/python3


class Graph:

    def __init__(self, data):
        self.data = data[:]    # ссылка на список числовых данных
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]
        
    def show_table(self):
        print("Data in string form:\t", " ".join(self.data))
    
    def show_graph(self):
        if self.is_show == False:
            print("Data display is closed.")
        else:
            print("Graphical display of data:")
            print(" ".join(self.data))
        
    def show_bar(self):
        if self.is_show == False:
            print("Data display is closed.")
        else:
            print("Bar chart:")
            print(" ".join(self.data))
        
    def set_show(self, is_show):
        self.fl_show = is_show


def data_check(data):
    if all(map(lambda x: x.isdigit(), data)):
        return True
    else:
        return False


# считывание списка из входного потока
data_graph = list(map(str, input("Введите ряд цифровых данных:\t").split()))
if not data_check(data_graph):
    while not data_check(data_graph):
        data_graph = list(map(str, input("Повторите ввод ТОЛЬКО цифровых данных:\t").split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_graph()
gr.show_table()

