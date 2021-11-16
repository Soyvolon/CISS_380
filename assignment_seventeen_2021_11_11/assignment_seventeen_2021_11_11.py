# Projects 4, 5 and 6 at the end of chapter 8 in the textbook. 
# You need to submit just one Python program (with many modules) 
# that includes the requirements from projects 4, 5 and 6. 

from market_model import MarketModel

def main():
    sim = MarketModel(100, 5, .75, 4)
    
    sim.runSimulation()

if __name__ == "__main__":
    main()