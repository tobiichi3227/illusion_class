# Load packages
import pyllusion
from psychopy import visual, event

# Create parameters

# delboeuf = pyllusion.Delboeuf(illusion_strength=1, difference=1)
#ebbinghaus = pyllusion.Ebbinghaus(illusion_strength=10)
#mullerlyer = pyllusion.MullerLyer(illusion_strength=300)
ponzo = pyllusion.Ponzo(illusion_strength=20)

# Initiate Window
window = visual.Window(color='white')

# Display illusion
ponzo.to_psychopy(window)

# Refresh and close window
window.flip()
ponzo.to_image()
# useful if you want to save the output for sharing...
#window.getMovieFrame('front')
#window.saveMovieFrames('delboeuf.png')

event.waitKeys()  # Press any key to close
window.close()