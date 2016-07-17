# Bach_AI
LSTM Neural Network (python 2.7) that writes piano melodies similar to Bach's.

Here's an example: https://www.noteflight.com/scores/view/c89c26b9f26aaab8aa3aff178b09c762e8722d44

# Dependencies

It all runs on python 2.7


You'll need pybrainv

    pip install pybrain
and midiutil

    http://www.emergentmusics.org/midiutil


# What the different files do
Chorales.lisp, parsemusic.py, and musicnetwork.py all need to be in the same directory.

Chorales.lisp is the song data

parsemusic.py turns Chorales.lisp into a dataset

musicnetwork.py uses that dataset to write melodies, it is the neural network.

parse midi.py is what turns the output of the neural network into a MID file.

# How to use

With everything set up in the same directory, it will be fairly easy. Simply run musicnetwork.py and it will print the dataset it's using, followed by the songs it produces at various epochs. The network will train on the dataset for one epoch, and then print a song. It does this forever, so you can just let it run for a while and then turn the latest song into a MID file. To do this, you will need to copy and paste. musicnetwork.py will output something like this:

    [[5, 2, 1, 1, 0], [7, 8, 1, 1, 0], [27, 4, 0, 2, 0], [26, 11, 0, 2, 0], [19, 3, 0, 1, 0], [16, 4, 0, 1, 0], [16, 1, 1, 1, 0], [15, 3, 1, 1, 0], [13, 2, 2, 1, 0], [14, 4, 2, 1, 0], [11, 2, 2, 0, 0], [7, 3, 2, 0, 0], [5, 5, 1, 0, 0], [8, 4, 1, 0, 0], [5, 5, 0, 1, 0], [6, 6, 0, 1, 0], [6, 0, 3, 1, 0], [10, 6, 3, 1, 0], [11, 2, 2, 1, 0], [14, 5, 2, 1, 0], [-3, 3, 2, 0, 0], [-2, 1, 2, 0, 0], [9, 2, 2, 0, 0], [2, -1, 2, 0, 0], [9, 3, 1, 0, 0], [4, 1, 1, 0, 0], [2, 3, 0, 0, 0], [-4, -3, 0, 0, 0], [-1, 10, 0, 0, 0], [-8, 0, 0, 0, 0], [-2, 1, 1, 0, 0], [-12, 1, 1, 0, 0], [4, 3, 2, 0, 0], [-5, 9, 2, 0, 0], [3, 0, 3, 0, 0], [-1, 4, 3, 0, 0], [0, 0, 2, 0, 0], [-2, 6, 2, 0, 0], [-3, 2, 1, 0, 0], [-8, 0, 1, 0, 0], [-4, 6, 0, 0, 0], [-7, 1, 0, 0, 0], [-4, 4, 1, 0, 0], [2, 3, 1, 0, 0], [1, 0, 3, 0, 0], [12, 1, 3, 0, 0], [6, -1, 4, 0, 0], [14, 4, 4, 0, 0], [7, -1, 5, 0, 0], [19, 1, 5, 0, 0], [7, -1, 3, 0, 0], [13, 5, 3, 0, 0], [5, -2, 2, 0, 0], [10, 6, 2, 0, 0], [0, 2, 2, 0, 0], [9, -1, 2, 0, 0], [-2, 3, 1, 0, 0], [10, 5, 1, 0, 0], [1, 7, 1, 0, 0], [14, 3, 1, 0, 0], [-8, 0, 2, 0, 0], [12, 6, 2, 0, 0], [-1, -1, 0, 0, 0], [14, 6, 0, 0, 0], [-1, -2, 3, 0, 0], [17, 7, 3, 0, 0], [-3, 0, 1, 0, 0], [3, 8, 1, 0, 0], [-8, 10, 0, 0, 0], [1, 9, 0, 0, 0], [2, 3, 0, 0, 0], [-1, 4, 0, 0, 0], [0, 10, 0, 0, 0], [1, 6, 0, 0, 0], [3, 2, 1, 0, 0], [3, 4, 1, 0, 0], [5, 5, 0, 0, 0], [3, 1, 0, 0, 0], [-3, 2, 1, 0, 0], [8, 1, 1, 0, 0], [-5, 3, 1, 0, 0], [6, 2, 1, 0, 0], [-4, 3, 1, 0, 0], [5, 4, 1, 0, 0], [-2, 0, 2, 0, 0], [4, 0, 2, 0, 0], [0, 1, 1, 0, 0], [9, 3, 1, 0, 0], [5, -1, 3, 0, 0], [13, 1, 3, 0, 0], [4, 0, 2, 0, 0], [10, 0, 2, 0, 0], [5, 0, 2, 0, 0], [12, 3, 2, 0, 0], [3, 3, 3, 0, 0], [6, 8, 3, 0, 0], [15, 6, 1, 0, 0], [10, 6, 1, 0, 0], [18, 7, 0, 0, 0], [13, 9, 0, 0, 0]]

Simply copy and paste that single line into "parse midi.py" so it's equal to the variable "songdata", like so:

    songdata = [[5, 2, 1, 1, 0], [7, 8, 1, 1, 0], [27, 4, 0, 2, 0], [26, 11, 0, 2, 0], [19, 3, 0, 1, 0], [16, 4, 0, 1, 0], [16, 1, 1, 1, 0], [15, 3, 1, 1, 0], [13, 2, 2, 1, 0], [14, 4, 2, 1, 0], [11, 2, 2, 0, 0], [7, 3, 2, 0, 0], [5, 5, 1, 0, 0], [8, 4, 1, 0, 0], [5, 5, 0, 1, 0], [6, 6, 0, 1, 0], [6, 0, 3, 1, 0], [10, 6, 3, 1, 0], [11, 2, 2, 1, 0], [14, 5, 2, 1, 0], [-3, 3, 2, 0, 0], [-2, 1, 2, 0, 0], [9, 2, 2, 0, 0], [2, -1, 2, 0, 0], [9, 3, 1, 0, 0], [4, 1, 1, 0, 0], [2, 3, 0, 0, 0], [-4, -3, 0, 0, 0], [-1, 10, 0, 0, 0], [-8, 0, 0, 0, 0], [-2, 1, 1, 0, 0], [-12, 1, 1, 0, 0], [4, 3, 2, 0, 0], [-5, 9, 2, 0, 0], [3, 0, 3, 0, 0], [-1, 4, 3, 0, 0], [0, 0, 2, 0, 0], [-2, 6, 2, 0, 0], [-3, 2, 1, 0, 0], [-8, 0, 1, 0, 0], [-4, 6, 0, 0, 0], [-7, 1, 0, 0, 0], [-4, 4, 1, 0, 0], [2, 3, 1, 0, 0], [1, 0, 3, 0, 0], [12, 1, 3, 0, 0], [6, -1, 4, 0, 0], [14, 4, 4, 0, 0], [7, -1, 5, 0, 0], [19, 1, 5, 0, 0], [7, -1, 3, 0, 0], [13, 5, 3, 0, 0], [5, -2, 2, 0, 0], [10, 6, 2, 0, 0], [0, 2, 2, 0, 0], [9, -1, 2, 0, 0], [-2, 3, 1, 0, 0], [10, 5, 1, 0, 0], [1, 7, 1, 0, 0], [14, 3, 1, 0, 0], [-8, 0, 2, 0, 0], [12, 6, 2, 0, 0], [-1, -1, 0, 0, 0], [14, 6, 0, 0, 0], [-1, -2, 3, 0, 0], [17, 7, 3, 0, 0], [-3, 0, 1, 0, 0], [3, 8, 1, 0, 0], [-8, 10, 0, 0, 0], [1, 9, 0, 0, 0], [2, 3, 0, 0, 0], [-1, 4, 0, 0, 0], [0, 10, 0, 0, 0], [1, 6, 0, 0, 0], [3, 2, 1, 0, 0], [3, 4, 1, 0, 0], [5, 5, 0, 0, 0], [3, 1, 0, 0, 0], [-3, 2, 1, 0, 0], [8, 1, 1, 0, 0], [-5, 3, 1, 0, 0], [6, 2, 1, 0, 0], [-4, 3, 1, 0, 0], [5, 4, 1, 0, 0], [-2, 0, 2, 0, 0], [4, 0, 2, 0, 0], [0, 1, 1, 0, 0], [9, 3, 1, 0, 0], [5, -1, 3, 0, 0], [13, 1, 3, 0, 0], [4, 0, 2, 0, 0], [10, 0, 2, 0, 0], [5, 0, 2, 0, 0], [12, 3, 2, 0, 0], [3, 3, 3, 0, 0], [6, 8, 3, 0, 0], [15, 6, 1, 0, 0], [10, 6, 1, 0, 0], [18, 7, 0, 0, 0], [13, 9, 0, 0, 0]]

After this, just run "parse midi.py" and it will output "song.mid", which contains the melody. Sometimes these files aren't playable as is. To turn this into an actual playable MIDI file, I uploaded it to https://onlinesequencer.net/ (through the "import midi" function), and then exported it as a playable midi file which I then downloaded. 


# How it works

I trained my neural network on a dataset of hundreds of melodies by Bach. It looks at each melody 2 notes at a time (that is, the dataset it trains on has an sample of two notes, and then the expected output is the next two notes). It has 30 LSTM layers of 30 neurons each. To generate a song, it first starts with two random notes, then it runs these through the network to get the next two 'expected' notes. It repeats this process and feeds the network the 'expected notes' while appending everything to a list of notes (each list contains ~100 notes), which is then turned into a MID file with "parse midi.py".
