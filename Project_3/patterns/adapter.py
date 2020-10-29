import abc
from googletrans import Translator
class French_adapter_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def adapt(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def avoir_nom(self):
        raise NotImplementedError

    @abc.abstractmethod
    def avoir_qualite(self):
        raise NotImplementedError

    @abc.abstractmethod
    def avoir_vendre_dans(self):
        raise NotImplementedError

class French_adapter(French_adapter_interface):

    def __init__(self, adaptee=None):
        self.adaptee = adaptee
        self.translator = Translator()

    def adapt(self, adaptee):
        self.adaptee = adaptee

    def avoir_nom(self):
        if self.adaptee:
            return self.translator.translate(self.adaptee.name, dest="fr").text
        else:
            raise NotImplementedError(" Adapter must have an item")

    def avoir_qualite(self):
        return self.adaptee.get_quality()

    def avoir_vendre_dans(self):
        return self.adaptee.get_sell_in()

class French_client_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def avoir_nom(self):
        raise NotImplementedError

    @abc.abstractmethod
    def avoir_qualite(self):
        raise NotImplementedError

    @abc.abstractmethod
    def avoir_vendre_dans(self):
        raise NotImplementedError

    @abc.abstractmethod
    def le_set_article(self):
        raise NotImplementedError

class French_client():
    def __init__(self, article=None):
        self.article = article

    def avoir_nom(self):
        return self.article.avoir_nom()

    def avoir_qualite(self):
        return self.article.avoir_qualite()

    def avoir_vendre_dans(self):
        return self.article.avoir_vendre_dans()

    def le_set_article(self, article):
        self.article = article
    

