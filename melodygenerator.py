# Importing python's "random" module

import random

# Generating random file name:

filename = 'Melody ' + str(random.randint(0, 999999)) + '.xml'


# Listing the keys and their associated chords (ignoring 7ths and diminished chords), via guitar-chords.org

#####Need to add minor keys here as well, as well as augmented/diminished even

key_and_triads_dictionary = {
'A' : ('A_maj', 'B_min', 'C_sharp_min', 'D_maj', 'E_maj', 'F_sharp_min'),
'A_sharp' : ('A_sharp_maj', 'C_min', 'D_min', 'D_sharp_maj', 'F_maj', 'G_min'),
'B' : ('B_maj', 'C_sharp_min', 'D_sharp_min', 'E_maj', 'F_sharp_maj', 'G_sharp_min'),
'C' : ('C_maj', 'D_min', 'E_min', 'F_maj', 'G_maj', 'A_min'),
'C_sharp' : ('C_sharp_maj', 'D_sharp_min', 'F_min', 'F_sharp_maj', 'G_sharp_maj', 'A_sharp_min'),
'D' : ('D_maj', 'E_min', 'F_sharp_min', 'G_maj', 'A_maj', 'B_min'),
'D_sharp' : ('D_sharp_maj', 'F_min', 'G_min', 'G_sharp_maj', 'A_sharp_maj', 'C_min'),
'E' : ('E_maj', 'F_sharp_min', 'G_sharp_min', 'A_maj', 'B_maj', 'C_sharp_min'),
'F' : ('F_maj', 'G_min', 'A_min', 'A_sharp_maj', 'C_maj', 'D_min'),
'F_sharp' : ('F_sharp_maj', 'G_sharp_min', 'A_sharp_min', 'B_maj', 'C_sharp_maj', 'D_sharp_min'),
'G' : ('G_maj', 'A_min', 'B_min', 'C_maj', 'D_maj', 'E_min'),
'G_sharp' : ('G_sharp_maj', 'A_sharp_min', 'C_min', 'C_sharp_maj', 'D_sharp_maj', 'F_min'),
}

#Below is a dictionary of diatonic triads, as these are notes that generally sound nice together. Have not yet implemented sevens, or augmented or diminished chords, or the occasional disharmony
triads_and_notes_dictionary = {
'A_maj': ('A','C#', 'E'),
'A_min' : ('A', 'C', 'E'),
'A_sharp_maj' : ('A#', 'D', 'F'),
'A_sharp_min' : ('A#','C#', 'F'),
'B_maj' : ('B', 'D#', 'F#'),
'B_min' : ('B', 'D', 'F#'),
'C_maj' : ('C', 'E', 'G'),
'C_min' : ('C', 'D#', 'G'),
'C_sharp_maj' : ('C#', 'E#', 'G#'),
'C_sharp_min' : ('C#', 'E', 'G#'),
'D_maj' : ('D', 'F#', 'A'),
'D_min' : ('D', 'F', 'A'),
'D_sharp_maj' : ('D#', 'G', 'A#'),
'D_sharp_min' : ('D#', 'F#', 'A#'),
'E_maj' : ('E', 'G#', 'B'),
'E_min' : ('E', 'G', 'B'),
'F_maj' : ('F', 'A', 'C'),
'F_min' : ('F', 'G#', 'C'),
'F_sharp_maj' : ('F#', 'A#', 'C#'),
'F_sharp_min' : ('F#', 'A', 'C#'),
'G_maj' : ('G', 'B', 'D'),
'G_min' : ('G', 'A#', 'D'),
'G_sharp_maj' : ('G#', 'C', 'D#'),
'G_sharp_min' : ('G#', 'B', 'D#'),
}


# Constructing melody
overall_key = random.sample(('A', 'A_sharp', 'B', 'C', 'C_sharp', 'D', 'D_sharp', 'E', 'F', 'F_sharp', 'G', 'G_sharp'), 1)[0]

#insrument randomisation has not been implemented
instrument = random.sample(('guitar', 'piano', 'harpsichord', 'lute'), 1)

#time signature randomisation has not been implemented
time_signature = random.sample(('4/4', '3/4'), 1)

number_of_bars = random.randint(8, 16)

# Generating a dictionary of each note
# note: dictionary is arranged like this: 'note_x_y (where x is the bar, y is the note (numbered left to right))' : (pitch, octave, duration, singlet/doublet/triplet)

notes_dictionary = {}

#working out note sequence
    
note_length_dictionary = {
'quaver' : 12,
'crotchet' : 24,
'dotted crotchet' : 36,
'minim' : 48,
'dotted minim' : 72,
'semibreve' : 96,
}
    
bar_sequence_dictionary = {}


#staircase_dictionary is not yet functional, this is for use when I wish to preference certain note progression patterns over others
staircase_dictionary = {
'2_C' : 1 ,
'2_C#' : 2 ,
'2_D' : 3 ,
'2_D#' : 4 ,
'2_E' : 5 ,
'2_F' : 6 ,
'2_F#' : 7 ,
'2_G' : 8 ,
'2_G#' : 9 ,
'2_A' : 10 ,
'2_A#' : 11 ,
'3_B' : 12 ,
'3_C' : 13 ,
'3_C#' : 14 ,
'3_D' : 15 ,
'3_D#' : 16 ,
'3_E' : 17 ,
'3_F' : 18 ,
'3_F#' : 19 ,
'3_G' : 20 ,
'3_G#' : 21 ,
'3_A' : 22 ,
'3_A#' : 23 ,
'3_B' : 24 ,
'4_C' : 25 ,
'4_C#' : 26 ,
'4_D' : 27 ,
'4_D#' : 28 ,
'4_E' : 29 ,
'4_F' : 30 ,
'4_F#' : 31 ,
'4_G' : 32 ,
'4_G#' : 33 ,
'4_A' : 34 ,
'4_A#' : 35 ,
'4_B' : 36 ,
'5_C' : 37 ,
'5_C#' : 38 ,
'5_D' : 39 ,
'5_D#' : 40 ,
'5_E' : 41 ,
'5_F' : 42 ,
'5_F#' : 43 ,
'5_G' : 44 ,
'5_G#' : 45 ,
'5_A' : 46 ,
'5_A#' : 47 ,
'5_B' : 48 ,
'6_C' : 49 ,
'6_C#' : 50 ,
'6_D' : 51 ,
'6_D#' : 52 ,
'6_E' : 53 ,
'6_F' : 54 ,
'6_F#' : 55 ,
'6_G' : 56 ,
'6_G#' : 57 ,
'6_A' : 58 ,
'6_A#' : 59 ,
'6_B' : 60
}


#Initialising the triad value
triad = random.sample(key_and_triads_dictionary[overall_key], 1)[0]

#this timing mechanism excludes ties (could just append to the last note of each bar?)

for n1 in range(1, number_of_bars + 1):
    
    print
    print 'Bar' + str(n1) 
    print
    
    number = 96

    blah_bars = []

    while number > 0:


        if number == 96:
    	    blah = random.sample(('quaver', 'quaver', 'quaver', 'quaver', 'quaver', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'dotted crotchet', 'minim', 'dotted minim', 'semibreve'), 1)[0]

        elif number == 84:
    	    blah = random.sample(('quaver', 'quaver', 'quaver', 'quaver', 'quaver', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'dotted crotchet', 'minim', 'dotted minim'), 1)[0]

        elif number == 72:
    	    blah = random.sample(('quaver', 'quaver', 'quaver', 'quaver', 'quaver', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'dotted crotchet', 'minim', 'dotted minim'), 1)[0]

        elif number == 60:
    	    blah = random.sample(('quaver', 'quaver', 'quaver', 'quaver', 'quaver', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'dotted crotchet', 'minim'), 1)[0]

        elif number == 48:
    	    blah = random.sample(('quaver', 'quaver', 'quaver', 'crotchet', 'crotchet', 'dotted crotchet', 'minim'), 1)[0]

        elif number == 36:
    	    blah = random.sample(('quaver', 'quaver', 'quaver', 'crotchet', 'crotchet', 'crotchet', 'dotted crotchet'), 1)[0]

        elif number == 24:
    	    blah = random.sample(('quaver', 'quaver', 'quaver', 'crotchet', 'crotchet',), 1)[0]

        elif number == 12:
    	    blah = 'quaver'

        number -= note_length_dictionary[blah]

        blah_bars.append(blah)

    random.shuffle(blah_bars)

    bar_sequence_dictionary['bar_' + str(n1)] = blah_bars


    for n2 in range(1, len(bar_sequence_dictionary['bar_' + str(n1)]) + 1):

        if n2 == 1:
            triad = random.sample((random.sample(key_and_triads_dictionary[overall_key], 1)[0], triad, triad, triad), 1)[0]
            
        else:
            triad = random.sample((random.sample(key_and_triads_dictionary[overall_key], 1)[0], notes_dictionary['note_' + str(n1) + '_' + str(n2-1)][5], notes_dictionary['note_' + str(n1) + '_' + str(n2-1)][5], notes_dictionary['note_' + str(n1) + '_' + str(n2-1)][5], notes_dictionary['note_' + str(n1) + '_' + str(n2-1)][5]), 1)[0]
           
        print triad

#        if n1 != 1 and n2 != 1:
#            staircase_variable = int(random.normalvariate(staircase_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][0]) + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][1])][0], 10))
#
#            pitch
#
#        else:
#            octave = random.sample((2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6), 1)[0]
#            
#            pitch = random.sample(triads_and_notes_dictionary[triad], 1)[0]

        octave = random.sample((2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6), 1)[0]
           
        pitch = random.sample(triads_and_notes_dictionary[triad], 1)[0]
        
        duration = str(note_length_dictionary[bar_sequence_dictionary['bar_' + str(n1)][n2-1]])

        #need to have a mechanism that adds a rest to the end of the bar if there is a gap

        #d is the multiplicity
        multiplicity = random.sample((1, 1, 1, 1, 1, 2, 2, 3, 3, 4), 1)[0]

        #decides if a rest
        rest = random.sample((0, 0, 0, 0, 0, 0, 1), 1)[0]

        notes_dictionary['note_' + str(n1) + '_' + str(n2)] = (pitch, octave, duration, multiplicity, rest, triad)

#fractions are converted to numbers in MusicXML
duration_to_fraction_dictionary = {
'12' : 'eighth',
'24' : 'quarter',
'36' : 'quarter',
'48' : 'half',
'72' : 'half',
'96' : 'whole'
}
        
#writing the file:

file = open(filename, 'w')
file.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 2.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise>
    <part-list>
    <score-part id="P1">
      <part-name>Music</part-name>
     </score-part>
    </part-list>
  <part id="P1">
""")
  

for n1 in range (1, number_of_bars + 1):
    file.write('   <measure number=\"' + str(n1) + '\">\n')
    
    # Writing the following for only the first bar (don't yet understand why)
    
    if n1 == 1:
        # Need to understand these, need to implement time signatures:

        file.write("""      <print>
        <staff-layout number="2">
          <staff-distance>65.00</staff-distance>
          </staff-layout>
        </print>
      <attributes>
        <divisions>24</divisions>
        <key>
          <fifths>0</fifths>
          </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
          </time>
        <staves>2</staves>
        <clef number="1">
          <sign>G</sign>
          <line>2</line>
          </clef>
        <clef number="2">
          <sign>F</sign>
          <line>4</line>
          </clef>
        </attributes>
""")
    else:
        pass


        
# Using the note dictionary to generate notes

    for n2 in range(1, len(bar_sequence_dictionary['bar_' + str(n1)]) + 1):

        ## Checking whether the note is a rest  
        ## note: rests equivalent to dotted crotchets/dotted minims look like crotchet/minim rests
            
        if str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][4]) == '1':
            file.write('''<note>
        <rest/>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
        </note>
''')
        
        else:
            file.write('''      <note>
        <pitch>
          <step>''' + notes_dictionary['note_' + str(n1) + '_' + str(n2)][0][0] + '''</step>
''')

            if len(notes_dictionary['note_' + str(n1) + '_' + str(n2)][0]) == 2:
                file.write('''          <alter>1</alter>
''')
            
            file.write('''          <octave>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][1]) + '''</octave>
          </pitch>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
''')
        
            
            if len(notes_dictionary['note_' + str(n1) + '_' + str(n2)][0]) == 2:
                file.write('''        <accidental>sharp</accidental>
''')
                
            else:
                file.write('''        <accidental>natural</accidental>
''')

            file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

            if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                file.write('''        <dot/>
''')

            if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                file.write('''        <dot/>                
''')     


            file.write('''        <stem>up</stem>
        <staff>1</staff>
        </note>
''')

        # Taking account of note multiplicity (work in comment below)
        
            # If the note is a doublet
                
            if str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][3]) == '2':
                #second note info
                second_note_pitch = random.sample(triads_and_notes_dictionary[notes_dictionary['note_' + str(n1) + '_' + str(n2)][5]], 1)[0]
                second_note_octave = str(random.sample((2, 3, 3, 4, 4, 4, 4, 5, 5, 6), 1)[0])
                
                file.write('''      <note>
        <chord/>
        <pitch>
          <step>''' + second_note_pitch + '''</step>
''')
          
                if len(second_note_pitch) == 2:
                    file.write('''          <alter>1</alter>
''')
                file.write('''          <octave>''' + second_note_octave + '''</octave>
          </pitch>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
''')
        
                if len(second_note_pitch) == 2:
                    file.write('''        <accidental>sharp</accidental>
''')
                
                else:
                    file.write('''        <accidental>natural</accidental>
''')
                
                file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                    file.write('''        <dot/>                
''')    

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                    file.write('''        <dot/>                
''')             
                
                file.write('''        <stem>down</stem>
        <staff>1</staff>
        </note>
''')
        
            # If the note is a triplet
        
            if str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][3]) == '3':
                #second note info
                second_note_pitch = random.sample(triads_and_notes_dictionary[notes_dictionary['note_' + str(n1) + '_' + str(n2)][5]], 1)[0]
                second_note_octave = str(random.sample((2, 3, 3, 4, 4, 4, 4, 5, 5, 6), 1)[0])
            
                file.write('''      <note>
        <chord/>
        <pitch>
          <step>''' + second_note_pitch + '''</step>
''')
          
                if len(second_note_pitch) == 2:
                    file.write('''          <alter>1</alter>
''')
                file.write('''          <octave>''' + second_note_octave + '''</octave>
          </pitch>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
''')
        
                if len(second_note_pitch) == 2:
                    file.write('''        <accidental>sharp</accidental>
''')
                
                else:
                    file.write('''        <accidental>natural</accidental>
''')

                file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                    file.write('''        <dot/>                
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                    file.write('''        <dot/>                
''')     

                file.write('''        <stem>down</stem>
        <staff>1</staff>
        </note>
''')

                #third note info
                third_note_pitch = random.sample(triads_and_notes_dictionary[notes_dictionary['note_' + str(n1) + '_' + str(n2)][5]], 1)[0]
                third_note_octave = str(random.sample((2, 3, 3, 4, 4, 4, 4, 5, 5, 6), 1)[0])
            
                file.write('''      <note>
        <chord/>
        <pitch>
          <step>''' + third_note_pitch + '''</step>
''')
          
                if len(third_note_pitch) == 2:
                    file.write('''          <alter>1</alter>
''')
                file.write('''          <octave>''' + third_note_octave + '''</octave>
          </pitch>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
''')
        
                if len(third_note_pitch) == 2:
                    file.write('''        <accidental>sharp</accidental>
''')
                
                else:
                    file.write('''        <accidental>natural</accidental>
''')

                file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                    file.write('''        <dot/>                
''')  

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                    file.write('''        <dot/>                
''')

                file.write('''        <stem>down</stem>
        <staff>1</staff>
        </note>
''')

            # If the note is a quartet
        
            if str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][3]) == '4':
                #second note info
                second_note_pitch = random.sample(triads_and_notes_dictionary[notes_dictionary['note_' + str(n1) + '_' + str(n2)][5]], 1)[0]
                second_note_octave = str(random.sample((2, 3, 3, 4, 4, 4, 4, 5, 5, 6), 1)[0])
            
                file.write('''      <note>
        <chord/>
        <pitch>
          <step>''' + second_note_pitch + '''</step>
''')
          
                if len(second_note_pitch) == 2:
                    file.write('''          <alter>1</alter>
''')
                file.write('''          <octave>''' + second_note_octave + '''</octave>
          </pitch>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
''')
        
                if len(second_note_pitch) == 2:
                    file.write('''        <accidental>sharp</accidental>
''')
                
                else:
                    file.write('''        <accidental>natural</accidental>
''')

                file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                    file.write('''        <dot/>                
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                    file.write('''        <dot/>                
''')     

                file.write('''        <stem>down</stem>
        <staff>1</staff>
        </note>
''')

                #third note info
                third_note_pitch = random.sample(triads_and_notes_dictionary[notes_dictionary['note_' + str(n1) + '_' + str(n2)][5]], 1)[0]
                third_note_octave = str(random.sample((2, 3, 3, 4, 4, 4, 4, 5, 5, 6), 1)[0])
            
                file.write('''      <note>
        <chord/>
        <pitch>
          <step>''' + third_note_pitch + '''</step>
''')
          
                if len(third_note_pitch) == 2:
                    file.write('''          <alter>1</alter>
''')
                file.write('''          <octave>''' + third_note_octave + '''</octave>
          </pitch>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
''')
        
                if len(third_note_pitch) == 2:
                    file.write('''        <accidental>sharp</accidental>
''')
                
                else:
                    file.write('''        <accidental>natural</accidental>
''')

                file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                    file.write('''        <dot/>                
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                    file.write('''        <dot/>                
''')         

                file.write('''        <stem>down</stem>
        <staff>1</staff>
        </note>
''')

                #fourth note info
                fourth_note_pitch = random.sample(triads_and_notes_dictionary[notes_dictionary['note_' + str(n1) + '_' + str(n2)][5]], 1)[0]
                fourth_note_octave = str(random.sample((2, 3, 3, 4, 4, 4, 4, 5, 5, 6), 1)[0])
            
                file.write('''      <note>
        <chord/>
        <pitch>
          <step>''' + fourth_note_pitch + '''</step>
''')
          
                if len(fourth_note_pitch) == 2:
                    file.write('''          <alter>1</alter>
''')
                file.write('''          <octave>''' + fourth_note_octave + '''</octave>
          </pitch>
        <duration>''' + str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2]) + '''</duration>
        <voice>1</voice>
''')
        
                if len(fourth_note_pitch) == 2:
                    file.write('''        <accidental>sharp</accidental>
''')
                
                else:
                    file.write('''        <accidental>natural</accidental>
''')

                file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                    file.write('''        <dot/>                
''')

                if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                    file.write('''        <dot/>                
''')     

                file.write('''        <stem>down</stem>
        <staff>1</staff>
        </note>
''')
        
        baseline = random.sample((0,0,1), 1)[0]
        #currently inactive, need to work out "backup" if I'm to do this
        if baseline == 2:
            bass_note_pitch = random.sample(triads_and_notes_dictionary[notes_dictionary['note_' + str(n1) + '_' + str(n2)][5]], 1)[0]
            bass_note_octave = str(random.sample((2, 3, 3, 4, 4, 4, 4, 5, 5, 6), 1)[0])
            bass_note_duration = 48

            file.write('''      <note>
        <pitch>
          <step>''' + bass_note_pitch + '''</step>
''')

            if len(bass_note_pitch) == 2:
                file.write('''          <alter>1</alter>
''')
            file.write('''          <octave>''' + bass_note_octave + '''</octave>
          </pitch>
        <duration>''' + str(bass_note_duration) + '''</duration>
        <voice>2</voice>
''')
        
            if len(bass_note_pitch) == 2:
                file.write('''        <accidental>sharp</accidental>
''')
                
            else:
                file.write('''        <accidental>natural</accidental>
''')

            file.write('''        <type>''' + duration_to_fraction_dictionary[str(notes_dictionary['note_' + str(n1) + '_' + str(n2)][2])] + '''</type>
''')

            if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '36':
                file.write('''        <dot/>                
''')

            if notes_dictionary['note_' + str(n1) + '_' + str(n2)][2] == '72':
                file.write('''        <dot/>                
''')        

            file.write('''        <stem>up</stem>
        <staff>2</staff>
        </note>
''')


    file.write('''      </measure>
''')

file.write('''    </part>
  </score-partwise>''')

# Terminal outputs
    
print
print 'key: ' + overall_key
print
print str(number_of_bars) + ' bars'
print
print filename + ' generated'
