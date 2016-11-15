import speech_recognition as sr
import ply.lex as lex


# Write the result of the voice to file
def write(formula):
    open("pl.txt", "w").write(formula)


def format(x):
    if 'cosine' in x.lower():
        write('np.cos(x)')
    elif 'sine' in x.lower():
        write('np.sin(x)')
    elif 'absolute' in x.lower():
        write('np.abs(x)')
    elif 'squareroot' in x.lower():
        write('np.sqrt(x)')
    elif 'cubic' in x.lower():
        write('x**3')
    elif 'squared' in x.lower():
        write('x**2')
    else:
        if '' not in x.lower():
            write('x')

# Parse Data
def parseData(input):
    result = ""
    flag = True
    if 'from' not in input:
        array = input.split()
        result += array[0] + " "
        for word in array:
            if word != array[0]:
                result += word
    else:
        array = input.split()
        result += array[0] + " "
        for word in array:
            if word != array[0]:
                if word != 'from' and flag:
                    print 'if'
                    result += word
                elif not flag:
                    print 'elif'
                    if 'to' in word:
                        result += " " + word
                    else:
                        result += word
                else:
                    print 'else'
                    result += " " + word
                    flag = False
    return result

# Filter the voice
def filter(input):
    if 'close' in input.lower():
        return 'CLOSE'
    elif 'stop' in input.lower():
        return 'STOP'
    else:
        return parseData(input.lower())


####################################################################
#                     Voice Recognition                            #
####################################################################
def voicerecognition(y):
    # obtain audio from the microphone
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Say Something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            value = r.recognize_google(audio)
            if str is bytes:
                voice = u"{}".format(value).encode("utf-8")

            print "You said: %s" % voice
            # input of the lexer
            data = filter(voice)
            if data == 'CLOSE' or data == 'STOP':
                break
            y.input(data.upper())
            while True:
                tok = lexer.token()
                x = lexer.lexdata
                if not tok:
                    break  # No more input
                format(x)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))

####################################################################
#                            LEXER                                 #
####################################################################

tokens = (
    'GRAPH',
    'CLOSE',
    'STOP',
    'SINE',
    'ABS',
    'SQR',
    'CUBIC',
    'ROOT',
    'CUBICR',
    'COS',
    )

# Regular expression rules for tokens
t_GRAPH = r'GRAPH'
t_STOP = r'STOP'
t_CLOSE = r'CLOSE'
t_SINE = r'SINEOFX'
t_ABS = r'ABSOLUTEVALUEOFX'
t_SQR = r'XSQUARED'
t_CUBIC = r'XCUBIC'
t_ROOT = r'SQUAREROOTOFX'
t_CUBICR = r'CUBICROOTOFX'
t_COS = r'COSINEOFX'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    t.lexer.skip(len(t.value))
    format("")

lexer = lex.lex()
voicerecognition(lexer)













