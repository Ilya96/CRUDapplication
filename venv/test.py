from PyQt5 import Qt
from data_provider import CRUDService
class Widget(Qt.QWidget):

    def __init__(self):
        super().__init__()
        layout = Qt.QVBoxLayout(self)

        btn_layout = Qt.QHBoxLayout()

        btn1 = Qt.QPushButton("Button 1")
        btn2 = Qt.QPushButton("Button 2")
        btn3 = Qt.QPushButton("Button 3")

        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        btn_layout.addWidget(btn3)

        table = Qt.QTableWidget()
        table.setRowCount(10)
        table.setColumnCount(10)
        layout.addWidget(table)
        layout.addLayout(btn_layout)


if __name__ == '__main__':
    '''app = Qt.QApplication([])
    w = Widget()
    w.show()
    app.exec()'''
    quote = CRUDService()
    quote.post("Kevin Kelly", "The business plans of the next 10,000 startups are easy to forecast: " +
                 "Take X and add AI.")
    quote.post("Stephen Hawking", "The development of full artificial intelligence could " +
               "spell the end of the human race… " +
               "It would take off on its own, and re-design " +
               "itself at an ever increasing rate. " +
               "Humans, who are limited by slow biological evolution, " +
               "couldn't compete, and would be superseded.")
    quote.post("Claude Shannon", "I visualize a time when we will be to robots what " +
                 "dogs are to humans, " +
                 "and I’m rooting for the machines.")
    quote.post("Elon Musk", "The pace of progress in artificial intelligence " +
                 "(I’m not referring to narrow AI) " +
                 "is incredibly fast. Unless you have direct " +
                 "exposure to groups like Deepmind, " +
                 "you have no idea how fast — it is growing " +
                 "at a pace close to exponential. " +
                 "The risk of something seriously dangerous " +
                 "happening is in the five-year timeframe." +
                 "10 years at most.")
    quote.post("Geoffrey Hinton", "I have always been convinced that the only way " +
                 "to get artificial intelligence to work " +
                 "is to do the computation in a way similar to the human brain. " +
                 "That is the goal I have been pursuing. We are making progress, " +
                 "though we still have lots to learn about " +
                 "how the brain actually works.")
    quote.post("Pedro Domingos", "People worry that computers will " +
                 "get too smart and take over the world, " +
                 "but the real problem is that they're too stupid " +
                 "and they've already taken over the world.")
    quote.post("Alan Turing", "It seems probable that once the machine thinking " +
                 "method had started, it would not take long " +
                 "to outstrip our feeble powers… " +
                 "They would be able to converse " +
                 "with each other to sharpen their wits. " +
                 "At some stage therefore, we should " +
                 "have to expect the machines to take control." +
                 "Take X and add AI.")
    quote.post("Ray Kurzweil", "Artificial intelligence will reach " +
                 "human levels by around 2029. " +
                 "Follow that out further to, say, 2045, " +
                 "we will have multiplied the intelligence, " +
                 "the human biological machine intelligence " +
                 "of our civilization a billion-fold.")
    quote.post("Sebastian Thrun", "Nobody phrases it this way, but I think " +
                 "that artificial intelligence " +
                 "is almost a humanities discipline. It's really an attempt " +
                 "to understand human intelligence and human cognition.")
    quote.post("Andrew Ng", "We're making this analogy that AI is the new electricity." +
                 "Electricity transformed industries: agriculture, " +
                 "transportation, communication, manufacturing.")