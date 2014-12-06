__author__ = 'Nickolas'



class SS:
    class InvalidSocial(ValueError):
        pass
    def __init__(self,ss=None):
        if ss is None:
            self.getsocial()
        else:
            self.ss = ss

    def __str__(self):
        return self.ss

    def validatess(self):
        try:
            area, group, serial = self.ss.split("-")
            if len(area) != (3) or len(group) != 2 or len(serial)!=4:
                raise self.InvalidSocial
            elif self.ss=="078-05-1120":
                raise self.InvalidSocial
            elif "666" == area:
                raise self.InvalidSocial
            elif int(area)>=900:
                raise self.InvalidSocial
            elif area=="000" or group=="00" or serial=="0000":
                raise self.InvalidSocial
            int(area)
            int(group)
            int(serial)
        except ValueError:
            raise self.InvalidSocial

    def getsocial(self):
        self.ss = input("Social Security Number:")
        try:
            self.validatess()
        except self.InvalidSocial:
            print("Invalid SS, please try again\n")
            self.getsocial()