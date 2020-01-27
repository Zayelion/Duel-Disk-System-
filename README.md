# Duel Disk System 
 Mixed Reality Card Game Controller based on NFC Identifiers
 
## How does this work
There are basically 3 parts in the project:
* **The Cards with NFC stickers inside their sleeves:** That contain the CardID inside the block 4 of the Mifare (4 byte UID)
* **The Reader/Field:** Which scans the NFC Card and send the info of it along with the placement of the card in the field to the main program. 
* **The Virtual Field:** This is the main program that connects to the Reader and displays info about the scanned card in a virtual environment, in this case a web browser on full screen mode.

Once a played wants to play a card, the card has to be scanned in the NFC scan zone. If the card is supposed to be face-down a button should be pressed during scanning. Once the scan is successful a beep sound will be produced, this gives the player an alert for placing the card. From this point the player has 2 seconds for plaing the card in a field zone. The card orientation is detected via 3 light sensors on the field. Then serial data from Card ID, position and Orientation will be sent to the Virtual Field.

The virtual field will determine which card is detected via a json file in the framework and will download necessary data if not available, such as card images. Relevant information will be displayed in the Virtual Field such as ATK/DEF, Level, Pendulum, etc. 

Only link Monsters are not accounted for in this project yet. 

## Built With
* [Selenium](https://selenium-python.readthedocs.io/) - For controlling the Browser
