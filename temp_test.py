from string import ascii_letters

class Person: 
    S_RUS = 'йцукенгшщзхъфывапролджэячсмитьбю'
    S_RUS_UPPER = S_RUS.upper()
    
    def __init__(self, fio, old, ps, weight): 
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old 
        self.__passport = ps 
        self.__weight = weight 

    @classmethod 
    def verify_fio(cls, fio):
        if type(fio) != str: 
            raise TypeError("ФИО должно быть строкой")
        
        f = fio.split()
        for s in f:
            if not s.isalpha():
                raise TypeError("Неверный формат ФИО")
        
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f: 
            if len(s) < 1:
                raise TypeError('В ФИО lолжен быть хотя бы один символ')
            if len(s.strip(letters)) != 0: 
                raise TypeError('В ФИО должны быть допустимые символы')
            
    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целым числом в диапозоне [14; 120]')
        
    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Вес должен быть вещественным числом больше 20')
        
    @classmethod 
    def verify_ps(cls, ps):
        if type(ps) != str: 
            raise TypeError('Паспорт должен быть строкой')
        
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6: 
            raise TypeError('Неверный формат паспорта')

        for p in s: 
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @property
    def fio(self):
        return self.__fio 
    
    @property
    def old(self):
        return self.__old 
    
    @old.setter 
    def old(self, old):
        self.verify_old(old)
        self.__old = old 

    @property
    def weight(self):
        return self.__weight 
    
    @weight.setter 
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight 

    @property
    def passport(self):
        return self.__passport 
    
    @passport.setter 
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps 
    

p = Person("Иванов Иван Иванович", 30, '1234 123442', 80.0)
p.old = 100 
p.passport = '4567 123456'
p.weight = 70.0
print(p.__dict__)