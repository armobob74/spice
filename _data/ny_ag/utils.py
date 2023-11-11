def parseFloat(s):
    try:
        return float(s)
    except ValueError:
        return 'None detected'
