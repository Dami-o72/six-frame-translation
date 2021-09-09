amino_acids = {'aaa':'LYS','aac':'ASN','aag':'LYS','aat':'ASN','aca':'THR',
               'acc':'THR','acg':'THR','act':'THR','aga':'ARG','agc':'SER',
               'agg':'ARG','agt':'SER','ata':'ILE','atc':'ILE','atg':'MET',
               'att':'ILE','caa':'GLN','cac':'HIS','cag':'GLN','cat':'HIS',
               'cca':'PRO','ccc':'PRO','ccg':'PRO','cct':'PRO','cga':'ARG',
               'cgc':'ARG','cgg':'ARG','cgt':'ARG','cta':'LEU','ctc':'LEU',
               'ctg':'LEU','ctt':'LEU','gaa':'GLU','gac':'ASP','gag':'GLU',
               'gat':'ASP','gca':'ALA','gcc':'ALA','gcg':'ALA','gct':'ALA',
               'gga':'GLY','ggc':'GLY','ggg':'GLY','ggt':'GLY','gta':'VAL',
               'gtc':'VAL','gtg':'VAL','gtt':'VAL','taa':'***','tac':'TYR',
               'tag':'***','tat':'TYR','tca':'SER','tcc':'SER','tcg':'SER',
               'tct':'SER','tga':'***','tgc':'CYS','tgg':'TRP','tgt':'CYS',
               'tta':'LEU','ttc':'PHE','ttg':'LEU','ttt':'PHE' }

def load_fasta(f):
    seq_title = f.readline()

# initialise input sequence string 
    s =''

# accumulate sequence line by line

    while True:
        seq_line = f.readline()
    # DEBUG    print len(seq_line.strip().lower())
        if seq_line == '':
            break
        else:
            s += seq_line.strip().lower()
        
    print(seq_title,'\n contains %d bases\n\n' % len(s))
    return (seq_title,s)

input_file = input('Please enter file name: ')
try:
    print('I found your file!')
    my_f = open(input_file, 'r')
except:
    print('I couldnt find your file, using myoglobin instead in 2 seconds')
    my_f = open('myoglobin.seq', 'r')
    import time
    time.sleep(2)

title, sequence = load_fasta(my_f)
print(sequence)
        
    
def translate(sequence):
    frame = []
    while len(sequence) >2 :
        codon = sequence[0:3]
        m = amino_acids[codon]
        frame.append(m)
    
        sequence = sequence[3:]
    return(frame)


F1 = translate(sequence )
F2 = translate (sequence[1:] )
F3 = translate(sequence[2:])


def complement(sequence):
    complement_dict = {'a':'t','c':'g','t':'a','g':'c'}
    #complement_base for a in sequence
    complementary = ''
    for i in sequence:
        complementary = complementary + complement_dict[i]
    return complementary

#complementary strand 
comp_strand = complement(sequence)
#print (comp_strand)

#complementary strand will be reversed so that it will be in the correct orientation...
#...when presented later
reverse_comp_strand = comp_strand[::-1]
#print(reverse_comp_strand)


F4 = translate(reverse_comp_strand )[::-1]
F5 = translate(reverse_comp_strand[1:])[::-1]
F6 = translate(reverse_comp_strand[2:])[::-1]


dashes = '----:----|' * 6


#the join function connects strings togther 
sequence_disp = ''.join(sequence) 
comp_strand_disp = ''.join(comp_strand)

F1_disp = ''.join(F1)
F2_disp = ''.join(F2)
F3_disp = ''.join(F3)

F4_disp = ''.join(F4)
F5_disp = ''.join(F5)
F6_disp = ''.join(F6)


#this section provides choices for which frame to print
frame_choice = input('which frame would you like printed: 6, 5,4,3,2,1??')
if frame_choice == '6':
    for i in range (0,len(sequence),60):
        print(F1_disp[i:i+60] + ' Frame 1')
        print(' ' + F2_disp[i:i+60] + ' Frame 2')
        print('  ' + F3_disp[i:i+60] + ' Frame 3')
        print(sequence_disp[i:i+60])
        print(dashes, i+60)
        print(comp_strand_disp[i:i+60])
        print(F4_disp[i:i+60] + ' Frame 4')
        print(' ' + F5_disp[i:i+60] + ' Frame 5')
        print('  ' + F6_disp[i:i+60] + ' Frame 6')
        print('')

elif frame_choice == '5':
    for i in range (0,len(sequence),60):
        print(F1_disp[i:i+60] + ' Frame 1')
        print(' ' + F2_disp[i:i+60] + ' Frame 2')
        print('  ' + F3_disp[i:i+60] + ' Frame 3')
        print(sequence_disp[i:i+60])
        print(dashes, i+60)
        print(comp_strand_disp[i:i+60])
        print(F4_disp[i:i+60] + ' Frame 4')
        print(' ' + F5_disp[i:i+60] + ' Frame 5')
        print('')
        
elif frame_choice == '4':
    for i in range (0,len(sequence),60):
        print(F1_disp[i:i+60] + ' Frame 1')
        print(' ' + F2_disp[i:i+60] + ' Frame 2')
        print('  ' + F3_disp[i:i+60] + ' Frame 3')
        print(sequence_disp[i:i+60])
        print(dashes, i+60)
        print(comp_strand_disp[i:i+60])
        print(F4_disp[i:i+60] + ' Frame 4')
        print('')
        
elif frame_choice == '3':
    for i in range (0,len(sequence),60):
        print(F1_disp[i:i+60] + ' Frame 1')
        print(' ' + F2_disp[i:i+60] + ' Frame 2')
        print('  ' + F3_disp[i:i+60] + ' Frame 3')
        print(sequence_disp[i:i+60])
        print(dashes, i+60)
        print(comp_strand_disp[i:i+60])
        print('')
        
elif frame_choice == '2':
    for i in range (0,len(sequence),60):
        print(F1_disp[i:i+60] + ' Frame 1')
        print(' ' + F2_disp[i:i+60] + ' Frame 2')
        print(sequence_disp[i:i+60])
        print(dashes, i+60)
        print(comp_strand_disp[i:i+60])
        print('')
        
elif frame_choice == '1':
    for i in range (0,len(sequence),60):
        print(F1_disp[i:i+60] + ' Frame 1')
        print(sequence_disp[i:i+60])
        print(dashes, i+60)
        print(comp_strand_disp[i:i+60])
        print('')
        
else:
        print('please choose a frame to print' )
