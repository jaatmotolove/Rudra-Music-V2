from Rudra.core.bot import Rudra
from Rudra.core.dir import dirr
from Rudra.core.git import git
from Rudra.core.userbot import Userbot
from Rudra.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Rudra()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
