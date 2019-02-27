# Module 8 - Skill Building Exercise No. 1 Solution
# Author: Bruce Elgort
# Date: July 22, 2017
# Update: February 25, 2019

# Define the Player class
class Player:
    # this gets called anytime we create a new player
    def __init__(self,playerName,playerColor):
        # set objects property values
        self.__playerName = playerName
        self.__playerColor = playerColor
        self.__playerStatus = "Alive"
        self.__playerTools = []

    # getTools method
    def getTools(self):
        return self.__playerTools

    # addTool method
    def addTool(self,tool):
        tools = self.__playerTools
        tools.append(tool)

    # removeTool method
    def removeTool(self,tool):
        # get list of tools
        tools = self.__playerTools
        # remove tool from list
        tools.remove(tool)

    # getStatus method
    def getStatus(self):
        return self.__playerStatus

    # setStatus method
    def setStatus(self,status):
        self.__playerStatus = status

    # getPlayer method
    def getPlayerName(self):
        return self.__playerName

def main():
    # create a Player named 'Bruce Elgort' and set his color to 'Blue'
    bruce = Player("Bruce Elgort","Blue")

    # call the newly created object and display it's playerName property
    print(bruce.getPlayerName())

    # call the getTools method to get the list of tools the user has and assign to a variable
    theTools = bruce.getTools()
    print("Current list of tools for",bruce.getPlayerName() + ":",theTools)

    # call the addTool method and give player a 'Hammer'
    bruce.addTool("Hammer")

    # print out the tools within the print function
    print("Current list of tools for",bruce.getPlayerName() + ":",theTools)

    # add another tool
    bruce.addTool("Bow and Arrow")

    # display list of tools
    # print out the tools within the print function
    print("Current list of tools for",bruce.getPlayerName() + ":",theTools)

    # now lets remove the hammer by calling the removeTool method
    bruce.removeTool('Hammer')

    # print out the tools within the print function
    print("Current list of tools for",bruce.getPlayerName() + ":",theTools)

    # set the status of the player to Dead
    bruce.setStatus("Dead")

    # display player status
    print("The current status of",bruce.getPlayerName() + ":",bruce.getStatus())


main()