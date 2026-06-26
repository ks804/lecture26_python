from .figure import Figure

class FigureService:
    figureId_seq = 1

    def __init__(self, figure_dao):
        self.__dao = figure_dao

    def get_all_figures(self):
        return self.__dao.select_all_figures()

    def get_figure_detail(self, figureId):
        return self.__dao.select_figure_by_id(figureId)

    def add_figure(self, name, character, price, stock):
        new_figure = Figure(str(FigureService.figureId_seq), name, character, price, stock)
        FigureService.figureId_seq += 1
        return self.__dao.insert_figure(new_figure)

    def edit_figure(self, figureId, figure):
        editing = self.__dao.select_figure_by_id(figureId)
        if editing:
            return self.__dao.update_figure(figureId, figure)
        return False

    def remove_figure(self, figureId):
        return self.__dao.delete_figure(figureId)
