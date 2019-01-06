class PatternBuilder:
    @staticmethod
    def build(set):
        pattern = ''
        keyList = []
        for key in set:
            keyList.append(key)

        keyList.sort()
        
        for key in keyList:
            if len(pattern) > 0:
                pattern = pattern + "|"
            pattern = pattern + key
        return pattern

