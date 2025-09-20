import time
from pypresence import Presence

client_id = "your_client_id"
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(state="In Game", details="Playing Level 1", large_image="game_image", small_image="level1_icon", start=time.time())
    time.sleep(15)