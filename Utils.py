class Utils:
    @staticmethod
    def reversed(number):
        if number < 0:
            return -int(str(-number)[::-1])
        else:
            return int(str(number)[::-1])

    @staticmethod
    def formatter(number):
        
        binary_num = bin(number)
        octal_num = oct(number)
        
        return binary_num, octal_num
