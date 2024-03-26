class rules():
    def __init__(self) -> None:
        pass

    def delete(self, character, file):
        result = (file[0], file[1].replace(character, ''))
        return result

    # [5]
    def addBehind(self, character, file):
        result = (file[0], file[1]+character)
        return result

    # [6]
    def addAhead(self, character, file):
        result = (file[0], character+file[1])
        return result


rules = rules()

if __name__ == '__main__':
    file = ('C:/Users/Seewo/Desktop/BukehiWeb/power point', 'en1.pptx')
    dst = rules.delete('en', file)
    print(dst)
