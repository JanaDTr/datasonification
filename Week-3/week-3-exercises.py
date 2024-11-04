# week-3-exercises.py
# 
# Python Exercises: 
# Variables (declaration, initialization), string concatenation, basic arithmetic, rounding, lists, and user input.
#
# This is how you can add an author attribution and software license within your Python code:
# Author: Louis Goldford
# License: Creative Commons Attribution 4.0 International (CC BY 4.0)
# 
# You are free to:
# - Share: copy and redistribute the material in any medium or format
# - Adapt: remix, transform, and build upon the material for any purpose, even commercially.
#
# Under the following terms:
# - Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. 
#   You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
#
# Full license text: https://creativecommons.org/licenses/by/4.0/
#
# Attribution: This work includes code developed by Dr. Louis Goldford for MHL Data Sonification, Week 3.
#
# To “comment in” or “comment out” lines of code in VS Code:  
# Highlight the line(s) of code you want to change, and then:  
# - on Windows: Press Ctrl + / 
# - on Mac: Press Cmd + /

# Exercise 1: Declare and Initialize a MIDI Note
# middleC = 60
# print(middleC)

# exercise 2
# part1 = "Do Re Mi"
# part2 = "Fa Sol La"
# phrase = part1 + " " + part2
# print(phrase)

# exercise 3
# quarter_note = 1.0
# eighth_note = 0.5
# total_duration = quarter_note + eighth_note
# print(total_duration)
# # you need to make a string from the float in a concatenation with a string
# print("The total duration is: " + str(total_duration))

# exercise 4
# note_duration = 1.2594833739
# rounded_duration = round(note_duration)
# print(rounded_duration)

# exercise 5
# C_major_triad = [60, 64, 67] # C E G
# print(C_major_triad)
# # no indices here like in JS

# exercise 6
# C_note, E_note, G_note = 60, 64, 67
# average_note = (C_note + E_note + G_note) / 3
# print(average_note)

# exercise 7
# round the average of the midi notes
# C_note, E_note, G_note = 60, 64, 67
# average_note = (C_note + E_note + G_note) / 3
# print (round(average_note))

# exercise 8
# first_part = "Do Re Mi Fa"
# second_part = "Sol La Si Do"
# full_scale = first_part + " " + second_part
# print(full_scale)

# exercise 9
# duration1, duration2 = 1.333, 2.666
# total_duration_rounded = round(duration1 + duration2)
# print(total_duration_rounded)

# exercise 10
# import random # import the package "random"
# solfege_scale = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do"]
# random.shuffle(solfege_scale)
# print(solfege_scale)

# exercise 11
# midi_note = int(input("Enter a MIDI note number: ")) # prompt in JS => will be a string
# print(midi_note)

# exercise 12: request 2 note durations from the user and add them
# midi_note1 = int(input("Enter a first MIDI note number: ")) 
# midi_note2 = int(input("Enter a second MIDI note number: ")) 
# print(midi_note1 + midi_note2)

# exercise 13
# solfege1 = input("Enter the first syllable (like Do): ")
# solfege2 = input("Enter the second syllable (like Re): ")
# solfege_phrase = solfege1 + " " + solfege2
# print(solfege_phrase)

# exercise 14
# tempo = int(input("Enter the tempo in BMP: "))
# beat_duration = 60000 / tempo
# four_beat_duration = beat_duration * 4
# print(four_beat_duration)

# exercise 15
# beat_duration = float(input("Enter the beat duration in ms: "))
# bpm = 60000 / beat_duration
# print(bpm)

# exercise 16
import time
bpm = int(input("Enter a tempo in bpm: "))
interval_in_s = 60 / bpm

time.sleep(0)
print("Tick 1")
time.sleep(interval_in_s)
print("Tick 2")
time.sleep(interval_in_s)
print("Tick 3")
time.sleep(interval_in_s) # does one line at a time <=> JS
print("Tick 4")
