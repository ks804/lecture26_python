from .figure import Figure

class FigureDAO:
    def __init__(self):
        self.__figureDB = {}  # 피규어번호 : Figure 객체

    def insert_figure(self, figure):
        figureId = figure.get_figureId()
        if not self.select_figure_by_id(figureId):
            self.__figureDB[figureId] = figure
            return True
        else:
            return False

    def select_figure_by_id(self, figureId):
        if figureId in self.__figureDB:
            return self.__figureDB[figureId]
        else:
            return None

    def select_all_figures(self):
        figure_list = list(self.__figureDB.values())
        if len(figure_list):
            return figure_list
        else:
            return None

    def update_figure(self, figureId, figure):
        if figureId in self.__figureDB:
            self.__figureDB[figureId] = figure
            return True
        else:
            return False

    def update_stock(self, figureId, stock):
        if figureId in self.__figureDB:
            self.__figureDB[figureId].set_stock(stock)
            return True
        else:
            return False

    def delete_figure(self, figureId):
        if figureId in self.__figureDB:
            self.__figureDB.pop(figureId)
            return True
        else:
            return False
