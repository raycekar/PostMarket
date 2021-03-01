class MarketPoster:
    def __init__(self, browser_driver, MarketFile):
        self.bd = browser_driver
        self.parser = self.MarketFileParser(MarketFile)
    
    def start(self):
        pass

    class MarketFileParser:
        def __init__(self, MarketFile):
            with open(MarketFile, 'r') as f:
                self.cmds = f.readlines()      
            self.linesLeft = len(self.cmds)

        def readLine(self):
            if self.linesLeft < 1:
                return None
            self.linesLeft -= 1
            return self.cmds[len(self.cmds) - self.linesLeft + 1]