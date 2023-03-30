#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This script will use challenge.json to generate README.md
# for the repository. It will compare the challenge list
# with all solutions present in the repository to calculate
# progress and fill up links.
#
# To get an up-to-date version of challenges.json, run
# 'update-challenge-list.py'.

import json
import os.path
import datetime

def anchor_from_title(title):
  return '-'.join(title.lower().split())

with open(os.path.realpath(os.path.dirname(__file__)) + '/../challenges.json', 'r') as file_challenges, open(os.path.realpath(os.path.dirname(__file__)) + '/../README.md', 'w', encoding='utf-8') as fout:
  json_root = json.loads(file_challenges.read())

  # count finished challenges and prepare rows
  difficulty = {'Easy': 0, 'Medium': 0, 'Hard': 0, 'Advanced': 0, 'Expert': 0}
  for track in json_root['tracks']:
    track['finish-count'] = 0
    track['count'] = 0
    for chapter in track['chapters']:
      chapter['finish-count'] = 0
      chapter['count'] = 0
      for i, challenge in enumerate(chapter['challenges']):
        path_to_challenge = 'solution/practice/%s/%s/%s' % (track['name'], chapter['name'], challenge['name'])
        challenge['table-row'] = [str(i + 1),
                                  '[%s](https://www.hackerrank.com/challenges/%s)' % (challenge['title'], challenge['name']),
                                  challenge['difficulty'],
                                  str(challenge['point']),
                                  "{0:.2f}%".format(challenge['rate'] * 100),
                                  ]
        track['count'] += 1
        chapter['count'] += 1
        path = os.path.realpath(os.path.dirname(__file__)) + '/../' + path_to_challenge + '/solution.py'
        if os.path.exists(path):
          track['finish-count'] += 1
          chapter['finish-count'] += 1
          challenge['table-row'].append('[Solution](%s/solution.py)' % path_to_challenge)
          difficulty[challenge['difficulty']] += 1
          with open(path, 'r') as f:
            timespace = eval(f.readline()[2:])
          challenge['table-row'] += ['*' + timespace['time'] + '*',
                                     '*' + timespace['space'] + '*',
                                    ]
        else:
          challenge['table-row'].append('WIP')


  # write to README.md
  blank = '&nbsp;' * 7
  date = "{:%d_%b_%Y}".format(datetime.date.today())
  fout.write('<p align="center">\n')
  fout.write('\t<a href="https://www.hackerrank.com/sudokux"><img height=120 src="https://d3keuzeb2crhkn.cloudfront.net/hackerrank/assets/styleguide/logo_wordmark-f5c5eb61ab0a154c3ed9eda24d0b9e31.svg"></a>\n')
  fout.write('</p>\n\n')
#  fout.write('---\n')
  fout.write('<p align="center">\n')
  fout.write('\t<img src="https://img.shields.io/badge/Problems_Solved-' + str(sum(difficulty.values())) + '-brightgreen.svg">' + blank + '\n')
  fout.write('\t<img src="https://img.shields.io/badge/Language-Python_3-blue.svg">' + blank + '\n')
  fout.write('\t<img src="https://img.shields.io/badge/Latest%20Update-' + date + '-ff69b4.svg">\n')
  fout.write('</p>\n\n')
#  fout.write('---\n')
  fout.write('<p align="center">\n')
  fout.write('\tMy solutions to problems on HackerRank.\n')
  fout.write('</p>\n')
  fout.write('<p align="center">\n')
  fout.write('\t<img src="https://img.shields.io/badge/Easy-' + str(difficulty['Easy']) + '-green.svg">' + blank + '\n')
  fout.write('\t<img src="https://img.shields.io/badge/Medium-' + str(difficulty['Medium']) + '-yellowgreen.svg">' + blank + '\n')
  fout.write('\t<img src="https://img.shields.io/badge/Hard-' + str(difficulty['Hard']) + '-yellow.svg">' + blank + '\n')
  fout.write('\t<img src="https://img.shields.io/badge/Advanced-' + str(difficulty['Advanced']) + '-orange.svg">' + blank + '\n')
  fout.write('\t<img src="https://img.shields.io/badge/Expert-' + str(difficulty['Expert']) + '-red.svg">\n')
  fout.write('</p>\n\n')

  fout.write('<p align="center">\n')
  fout.write('\tIf you are interested in helping or have a solution in a different language, please do not hestitate to make a pull request.\n')
  fout.write('</p>\n\n')
  fout.write('---\n\n')
  fout.write('HackerRank Solutions in Python3\n======\n\n')
  fout.write('This is a collection of my [HackerRank](https://www.hackerrank.com/) solutions written in Python3. '
             'The goal of this series is to keep the pythonic code as concise and efficient as possible, yet without compromise much of the readability. '
             'It might not be perfect due to the limitation of my ability and skill, so '
             'feel free to make suggestions if you spot something that can be improved.\n\n'
             'The index below is auto-generated. See [update-challenge-list.py](util/update-challenge-list.py) '
             'and [generate-indices.py](util/generate-indices.py).\n\n')
  fout.write('Index\n======\n\n')
  for track in json_root['tracks']:
    fout.write('* [%s](#%s) (%d/%d)\n' % (track['title'], anchor_from_title(track['title']), track['finish-count'], track['count']))
  fout.write('\n')
  for track in json_root['tracks']:
    fout.write(track['title'] + '\n------\n\n')
    for chapter in track['chapters']:
      fout.write('* [%s](#%s) (%d/%d)\n' % (chapter['title'], anchor_from_title(chapter['title']), chapter['finish-count'], chapter['count']))
    fout.write('\n')
    for chapter in track['chapters']:
      fout.write('### %s\n' % chapter['title'])
      row = ['\\#', 'Challenge', 'Difficulty', 'Points', 'Hit Rate', 'Python 3','Time','Space']
      fout.write(' | '.join(row) + '\n')
      fout.write('|'.join([':---:'] * len(row)) + '\n')
      for challenge in chapter['challenges']:
        fout.write(' | '.join(challenge['table-row']) + '\n')
      fout.write('\n')
