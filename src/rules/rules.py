class rules():
    def __init__(self) -> None:
        pass

    def delete(self, character, file):
        result = (file[0], file[1].replace(character, ''))
        return result

    # [1]
    def addNumberBehind(self, number, file):
        filename = file[1].split('.')
        filename = filename[0]+str(number)+'.'+filename[1]
        result = (file[0], filename)
        return result

    # [2]
    def addNumberAhead(self, number, file):
        result = (file[0], str(number)+file[1])
        return result

    # [3]
    def addBehind(self, character, file):
        filename = file[1].split('.')
        filename = filename[0]+character+'.'+filename[1]
        result = (file[0], filename)
        return result

    # [4]
    def addAhead(self, character, file):
        result = (file[0], character+file[1])
        return result


rules = rules()

if __name__ == '__main__':
    file = ('C:/Users/Seewo/Desktop/BukehiWeb/power point', 'en1.pptx')
    dst = rules.delete('en', file)
    print(dst)
