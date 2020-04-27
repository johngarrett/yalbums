# use ffmpeg to split an mp3 according to a set list
from __future__ import print_function
import subprocess as sp

# NB: add -copy if from mp3 -> mp3; else no -copy
setfile = './Ray Wylie Hubbard in Concert -  December 17, 2010 at Tennessee State Museum.set'
mp3file = './Ray Wylie Hubbard full concert - DASH.m4a'
outdir = './Ray Wylie Hubbard in Concert -  December 17, 2010 at Tennessee State Museum'
meta_src = 'https://www.youtube.com/watch?v=y9_xBIuV9nE'
do_copy = False
print('splitting \'%s\' according to sets in \'%s\' into directory \'%s\'' % (mp3file, setfile, outdir))

metas = {'artist':'Ray Wylie Hubbard', 'album':'Acoustic Live in Concert December 17 2010 at Tennessee State Museum / Hippie Jacks'}
metastring = ' '.join([ '-metadata %s="%s"' % (k,v) for k,v in metas.iteritems()])

songs = []
with open(setfile) as f:
  for line in f:
    start, title = line.strip().split(' ', 1)
    songs.append((start, title))

print('read %d lines' % len(songs))

# set id3 tags ala http://jonhall.info/how_to/create_id3_tags_using_ffmpeg
cmds = []
for i in range(len(songs) - 1):
  cmd = (songs[i][0], songs[i+1][0], songs[i][1])
  cmds.append(cmd)

  run = 'ffmpeg -i \"%s\" -acodec %s -ss %s -to %s ' % (mp3file, 'copy' if do_copy else 'libmp3lame -qscale:a 2', cmd[0], cmd[1])
  run += '%s -metadata title="%s" -metadata track="%d/%d" -metadata publisher="%s" ' % (metastring, cmd[2], i+1, len(songs) - 1, meta_src)
  run += '"%s/%02d.mp3"' % (outdir, i + 1)
  # print("\tcmd: %s" % run)
  sp.call(run, shell=True)
