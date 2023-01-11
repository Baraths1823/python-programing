def findAllCombinations(keypad, keys):
    if not keypad or not keys:
        return set()
    combinations = {str(ch) for ch in keypad[keys[0]]} 
    for i in range(1, len(keys)):
        prevList = combinations.copy()
        combinations = {s + ch for ch in keypad[keys[i]] for s in prevList}
    return combinations
if __name__ == '__main__':
    keypad = {
        
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z']
    }
    keys = [2,3,4] 
    combinations = findAllCombinations(keypad, keys)
    print(combinations)
